-- PostgreSQL: olemasolevad tabelid → tähtskeem (vaated)
-- fact_muuk:        üks rida = üks müügirida (tellimuse_read)
-- fact_tellimused:  üks rida = üks tellimus
-- tooted.hind = netohind (ilma KM); KM tuleb kategooriad.km_maar (nt 24 → 24%)
-- tooted.kategooria = kategooriad.nimetus (seos nime, mitte ID järgi)

DROP VIEW IF EXISTS fact_tellimused;
DROP VIEW IF EXISTS fact_muuk;
DROP VIEW IF EXISTS dim_toode;
DROP VIEW IF EXISTS dim_klient;
DROP VIEW IF EXISTS dim_aeg;


CREATE VIEW dim_klient AS
SELECT
    klient_id,
    nimi,
    linn,
    CASE
        WHEN linn IN ('Tallinn', 'Tartu') THEN linn
        ELSE 'muu'
    END AS piirkond,
    liitumise_kuupäev,
    EXTRACT(YEAR FROM liitumise_kuupäev)::integer AS liitumise_aasta
FROM kliendid;


CREATE VIEW dim_toode AS
SELECT
    t.toode_id,
    t.nimetus,
    t.hind AS hind_ilma_km,
    ROUND(t.hind * (1 + k.km_maar / 100.0), 2) AS hind_koos_km,
    CASE
        WHEN t.hind < 100 THEN 'odav'
        WHEN t.hind < 500 THEN 'keskmine'
        ELSE 'kallis'
    END AS hinna_klass,
    k.kategooria_id,
    k.nimetus AS kategooria,
    k.osakond,
    k.km_maar,
    (k.km_maar < 24) AS on_soodus_km
FROM tooted t
LEFT JOIN kategooriad k
    ON t.kategooria = k.nimetus;


CREATE VIEW dim_aeg AS
SELECT
    d::date AS kuupäev,
    EXTRACT(YEAR FROM d)::integer AS aasta,
    EXTRACT(QUARTER FROM d)::integer AS kvartal,
    EXTRACT(MONTH FROM d)::integer AS kuu,
    TO_CHAR(d, 'YYYY-MM') AS aasta_kuu,
    EXTRACT(YEAR FROM d)::integer::text
        || '-Q'
        || EXTRACT(QUARTER FROM d)::integer::text AS aasta_kvartal,
    CASE EXTRACT(MONTH FROM d)::integer
        WHEN 1 THEN 'jaanuar'
        WHEN 2 THEN 'veebruar'
        WHEN 3 THEN 'märts'
        WHEN 4 THEN 'aprill'
        WHEN 5 THEN 'mai'
        WHEN 6 THEN 'juuni'
        WHEN 7 THEN 'juuli'
        WHEN 8 THEN 'august'
        WHEN 9 THEN 'september'
        WHEN 10 THEN 'oktoober'
        WHEN 11 THEN 'november'
        WHEN 12 THEN 'detsember'
    END AS kuu_nimi,
    EXTRACT(ISODOW FROM d)::integer AS nadala_paev,
    CASE EXTRACT(ISODOW FROM d)::integer
        WHEN 1 THEN 'esmaspäev'
        WHEN 2 THEN 'teisipäev'
        WHEN 3 THEN 'kolmapäev'
        WHEN 4 THEN 'neljapäev'
        WHEN 5 THEN 'reede'
        WHEN 6 THEN 'laupäev'
        WHEN 7 THEN 'pühapäev'
    END AS nadala_paev_nimi,
    (EXTRACT(ISODOW FROM d) IN (6, 7)) AS on_naidalopp
FROM generate_series(
    DATE '2024-01-01',
    DATE '2026-12-31',
    INTERVAL '1 day'
) AS d;


CREATE VIEW fact_muuk AS
SELECT
    tr.tellimus_rida_id,
    tr.tellimus_id,
    t.klient_id,
    tr.toode_id,
    t.kuupäev,
    t.staatus,
    t.makseviis,
    t.tarneviis,
    CASE WHEN t.staatus = 'Täidetud' THEN 'Täidetud' END AS taidetud,
    CASE WHEN tr.allahindlus_pct > 0 THEN 'allahinnatud' END AS allahinnatud,
    (t.kuupäev - kl.liitumise_kuupäev) AS paevi_liitumisest,
    tr.kogus,
    tr.allahindlus_pct,
    k.km_maar,
    td.hind AS yhiku_hind,
    ROUND(td.hind * tr.kogus, 2) AS rida_enne_allahindlust,
    ROUND(td.hind * tr.kogus * tr.allahindlus_pct / 100.0, 2) AS allahindluse_summa,
    ROUND(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0), 2) AS rida_ilma_km,
    ROUND(
        td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0) * k.km_maar / 100.0,
        2
    ) AS rida_km,
    ROUND(
        td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0) * (1 + k.km_maar / 100.0),
        2
    ) AS rida_koos_km
FROM tellimuse_read tr
INNER JOIN tellimused t
    ON tr.tellimus_id = t.tellimus_id
INNER JOIN tooted td
    ON tr.toode_id = td.toode_id
INNER JOIN kliendid kl
    ON t.klient_id = kl.klient_id
LEFT JOIN kategooriad k
    ON td.kategooria = k.nimetus;


CREATE VIEW fact_tellimused AS
SELECT
    t.tellimus_id,
    t.klient_id,
    t.kuupäev,
    t.staatus,
    t.makseviis,
    t.tarneviis,
    CASE WHEN t.staatus = 'Täidetud' THEN 'Täidetud' END AS taidetud,
    (t.kuupäev - kl.liitumise_kuupäev) AS paevi_liitumisest,
    COUNT(*) AS ridade_arv,
    SUM(tr.kogus) AS tooteid_kokku,
    ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS tellimus_ilma_km,
    ROUND(
        SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0) * k.km_maar / 100.0),
        2
    ) AS tellimus_km,
    ROUND(
        SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0) * (1 + k.km_maar / 100.0)),
        2
    ) AS tellimus_koos_km,
    ROUND(SUM(td.hind * tr.kogus * tr.allahindlus_pct / 100.0), 2) AS allahindluse_summa
FROM tellimused t
INNER JOIN kliendid kl
    ON t.klient_id = kl.klient_id
INNER JOIN tellimuse_read tr
    ON t.tellimus_id = tr.tellimus_id
INNER JOIN tooted td
    ON tr.toode_id = td.toode_id
LEFT JOIN kategooriad k
    ON td.kategooria = k.nimetus
GROUP BY
    t.tellimus_id,
    t.klient_id,
    t.kuupäev,
    t.staatus,
    t.makseviis,
    t.tarneviis,
    kl.liitumise_kuupäev;
