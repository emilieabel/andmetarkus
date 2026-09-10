
DROP VIEW IF EXISTS analytics.fact_myyk;
DROP VIEW IF EXISTS analytics.dim_toode;
DROP VIEW IF EXISTS analytics.dim_klient;
DROP VIEW IF EXISTS analytics.dim_aeg;

CREATE OR REPLACE VIEW analytics.dim_klient AS
SELECT
    klient_id,
    nimi AS nimi, --pärast maskeerimiseks repeat('*', length(nimi)) AS nimi,
    linn,
    CASE
        WHEN linn IN ('Tallinn', 'Tartu') THEN linn
        ELSE 'muu'
    END AS piirkond,
    liitumise_kuupäev,
    EXTRACT(YEAR FROM liitumise_kuupäev)::integer AS liitumise_aasta,
    (CURRENT_DATE - liitumise_kuupäev) AS paevi_liitumisest
FROM kliendid;


CREATE OR REPLACE VIEW analytics.dim_toode AS
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


CREATE OR REPLACE VIEW analytics.dim_aeg AS
SELECT 
	TO_CHAR(d, 'YYYYMMDD')::integer AS kuupäev_id, -- UUS: Unikaalne ID sidumiseks faktitabeliga    
	d::date AS kuupäev,
    EXTRACT(YEAR FROM d)::integer AS aasta,
    EXTRACT(QUARTER FROM d)::integer AS kvartal,
    EXTRACT(MONTH FROM d)::integer AS kuu,
    TO_CHAR(d, 'YYYY-MM') AS aasta_kuu,
    EXTRACT(YEAR FROM d)::integer::text
        || '-Q'
        || EXTRACT(QUARTER FROM d)::integer::text AS aasta_kvartal,
    EXTRACT(ISODOW FROM d)::integer AS nadala_paev,
    (EXTRACT(ISODOW FROM d) IN (6, 7)) AS on_naidalopp
FROM generate_series(
    DATE '2024-01-01',
    DATE '2026-12-31',
    INTERVAL '1 day'
) AS d;

CREATE OR REPLACE VIEW analytics.fact_myyk AS
SELECT
    t.tellimus_id,
    tr.toode_id, 
    t.klient_id,
    t.kuupäev,
    TO_CHAR(t.kuupäev, 'YYYYMMDD')::integer AS kuupäev_id, 
    t.staatus,
    t.makseviis,
    t.tarneviis,
    CASE WHEN t.staatus = 'Täidetud' THEN 'Täidetud' END AS taidetud,
    (t.kuupäev - kl.liitumise_kuupäev) AS paevi_liitumisest,
    tr.kogus AS kogus, 
    
    -- 1. Summa algse täishinnaga (enne allahindlust ja ilma KM-ta)
    ROUND(SUM(td.hind * tr.kogus), 2) AS rida_tais_summa_ilma_km,
    
    -- 2. UUS: Summa, kus allahindlus on maha arvatud (ilma KM-ta)
    ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS rida_allahindlusega_ilma_km,
    
    -- 3. Allahindluse summa ise (rahaline võit)
    ROUND(SUM(td.hind * tr.kogus * tr.allahindlus_pct / 100.0), 2) AS allahindluse_summa,
    
    -- 4. Käibemaksu summa (arvutatud juba allahinnatud summalt)
    ROUND(
        SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0) * k.km_maar / 100.0),
        2
    ) AS rida_km,
    
    -- 5. Lõplik summa kliendile (allahindlus maha arvatud + KM juurde liidetud)
    ROUND(
        SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0) * (1 + k.km_maar / 100.0)),
        2
    ) AS rida_koos_km
    
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
    tr.toode_id, 
    t.klient_id,
    t.kuupäev,
    t.staatus,
    t.makseviis,
    t.tarneviis,
    kl.liitumise_kuupäev,
    tr.kogus;
