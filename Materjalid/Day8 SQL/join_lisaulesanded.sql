-- Lisaülesanded JOIN-päevaks (pole 8. päeva slaididel)
-- Andmed: originaal + tellimused_uued + tellimuse_read_uued + kliendid_uued
-- Tulu = täidetud read, pärast soodustust:
--   hind * kogus * (1 - allahindlus_pct / 100.0)


-- 1. Tooted KM-määraga 22. Kuva nimetus, hind, km_maar.
SELECT
    t.nimetus,
    t.hind,
    k.km_maar
FROM tooted t
INNER JOIN kategooriad k
    ON t.kategooria = k.nimetus
WHERE k.km_maar = 22;


-- 2. Tühistatud tellimuste arv ostja nime kaupa.
SELECT
    k.nimi,
    COUNT(*) AS tyhistatud
FROM kliendid k
INNER JOIN tellimused t
    ON k.klient_id = t.klient_id
WHERE t.staatus = 'Tühistatud'
GROUP BY k.nimi
ORDER BY tyhistatud DESC, k.nimi;


-- 3. Kliendid, kellel pole ühtegi tellimust (LEFT JOIN + tühi pool).
SELECT
    k.nimi,
    k.linn
FROM kliendid k
LEFT JOIN tellimused t
    ON k.klient_id = t.klient_id
WHERE t.tellimus_id IS NULL;


-- 4. Iga kliendi tellimuste arv, ka need, kellel on 0.
--    COUNT(t.tellimus_id) annab 0; COUNT(*) annaks ekslikult 1.
SELECT
    k.klient_id,
    k.nimi,
    COUNT(t.tellimus_id) AS tellimuste_arv
FROM kliendid k
LEFT JOIN tellimused t
    ON k.klient_id = t.klient_id
GROUP BY k.klient_id, k.nimi
ORDER BY tellimuste_arv, k.nimi;


-- 5. Täidetud tellimused: ostja linn ja müüdud kogus kokku.
SELECT
    k.linn,
    SUM(tr.kogus) AS kogus
FROM kliendid k
INNER JOIN tellimused t ON k.klient_id = t.klient_id
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
WHERE t.staatus = 'Täidetud'
GROUP BY k.linn
ORDER BY kogus DESC;


-- 6. Apple Pay: ostja nimi, toote nimetus, kogus.
SELECT
    k.nimi,
    td.nimetus,
    tr.kogus
FROM kliendid k
INNER JOIN tellimused t ON k.klient_id = t.klient_id
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
INNER JOIN tooted td ON tr.toode_id = td.toode_id
WHERE t.makseviis = 'Apple Pay';


-- 7. Mitu erinevat toodet on linna kaupa ostetud.
SELECT
    k.linn,
    COUNT(DISTINCT tr.toode_id) AS tooteid
FROM kliendid k
INNER JOIN tellimused t ON k.klient_id = t.klient_id
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
GROUP BY k.linn
ORDER BY tooteid DESC;


-- 8. Täidetud müük pärast soodustust, aasta ja osakonna kaupa.
SELECT
    EXTRACT(YEAR FROM t.kuupäev)::integer AS aasta,
    kat.osakond,
    ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS myyk
FROM tellimused t
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
INNER JOIN tooted td ON tr.toode_id = td.toode_id
INNER JOIN kategooriad kat ON td.kategooria = kat.nimetus
WHERE t.staatus = 'Täidetud'
GROUP BY EXTRACT(YEAR FROM t.kuupäev), kat.osakond
ORDER BY aasta, kat.osakond;


-- 9. Allahindlus eurodes osakondade kaupa (täidetud). Suuremad ees.
SELECT
    kat.osakond,
    ROUND(SUM(td.hind * tr.kogus * tr.allahindlus_pct / 100.0), 2) AS allahindlus
FROM tellimused t
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
INNER JOIN tooted td ON tr.toode_id = td.toode_id
INNER JOIN kategooriad kat ON td.kategooria = kat.nimetus
WHERE t.staatus = 'Täidetud'
GROUP BY kat.osakond
ORDER BY allahindlus DESC;


-- 10. Linnad, kus täidetud tellimusi on rohkem kui 8.
SELECT
    k.linn,
    COUNT(*) AS tellimusi
FROM kliendid k
INNER JOIN tellimused t
    ON k.klient_id = t.klient_id
WHERE t.staatus = 'Täidetud'
GROUP BY k.linn
HAVING COUNT(*) > 8
ORDER BY tellimusi DESC;
