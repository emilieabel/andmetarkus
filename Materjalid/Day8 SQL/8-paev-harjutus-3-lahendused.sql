-- 8. päev · JOIN · Harjutus 3 lahendused
-- Andmestik: originaal + _uued
-- Tase 1: kõik staatused, kui ülesanne ei küsi teisiti
-- Tase 2: tulu = staatus Täidetud, pärast allahindlust
-- Valem: hind × kogus × (1 − allahindlus_pct / 100)


-- =============================================================================
-- TASE 1
-- =============================================================================

-- 1. Toote nimetus ja müügisumma pärast allahindlust
SELECT td.nimetus,
       ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS summa
FROM tellimuse_read tr
INNER JOIN tooted td ON tr.toode_id = td.toode_id
GROUP BY td.nimetus
ORDER BY summa DESC;


-- 2. Sama, ainult kategooria Telefonid
SELECT td.nimetus,
       ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS summa
FROM tellimuse_read tr
INNER JOIN tooted td ON tr.toode_id = td.toode_id
WHERE td.kategooria = 'Telefonid'
GROUP BY td.nimetus
ORDER BY summa DESC;


-- 3. Müük kategooriate kaupa
SELECT td.kategooria,
       ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS summa
FROM tellimuse_read tr
INNER JOIN tooted td ON tr.toode_id = td.toode_id
GROUP BY td.kategooria
ORDER BY summa DESC;


-- 4. Tellimuse ID, toote nimetus, kogus
SELECT tr.tellimus_id, td.nimetus, tr.kogus
FROM tellimuse_read tr
INNER JOIN tooted td ON tr.toode_id = td.toode_id
ORDER BY tr.tellimus_id;


-- 5. Sama, kogus > 1
SELECT tr.tellimus_id, td.nimetus, tr.kogus
FROM tellimuse_read tr
INNER JOIN tooted td ON tr.toode_id = td.toode_id
WHERE tr.kogus > 1
ORDER BY tr.tellimus_id;


-- =============================================================================
-- TASE 2
-- =============================================================================

-- 1. Viis klienti, kõige rohkem tulu (Täidetud, pärast allahindlust)
--    klient_id on vajalik: kaks Kati Lepikut
SELECT k.klient_id, k.nimi,
       ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS tulu
FROM kliendid k
INNER JOIN tellimused t ON k.klient_id = t.klient_id
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
INNER JOIN tooted td ON tr.toode_id = td.toode_id
WHERE t.staatus = 'Täidetud'
GROUP BY k.klient_id, k.nimi
ORDER BY tulu DESC
LIMIT 5;


-- 2. Osakond, kes on kõige rohkem müünud (Täidetud neto)
SELECT kat.osakond,
       ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS netokaive
FROM tellimused t
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
INNER JOIN tooted td ON tr.toode_id = td.toode_id
INNER JOIN kategooriad kat ON td.kategooria = kat.nimetus
WHERE t.staatus = 'Täidetud'
GROUP BY kat.osakond
ORDER BY netokaive DESC;


-- 3. Tühistatud tellimuste summa
--    COUNT DISTINCT tellimus_id = tellimused, mitte read
SELECT COUNT(DISTINCT t.tellimus_id) AS tuhistatud_tellimusi,
       ROUND(SUM(td.hind * tr.kogus * (1 - tr.allahindlus_pct / 100.0)), 2) AS summa
FROM tellimused t
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
INNER JOIN tooted td ON tr.toode_id = td.toode_id
WHERE t.staatus = 'Tühistatud';


-- 4. Ootel tellimuste allahindlus linnade kaupa
SELECT k.linn,
       ROUND(SUM(td.hind * tr.kogus * tr.allahindlus_pct / 100.0), 2) AS allahindlus
FROM kliendid k
INNER JOIN tellimused t ON k.klient_id = t.klient_id
INNER JOIN tellimuse_read tr ON t.tellimus_id = tr.tellimus_id
INNER JOIN tooted td ON tr.toode_id = td.toode_id
WHERE t.staatus = 'Ootel'
GROUP BY k.linn
ORDER BY allahindlus DESC;
