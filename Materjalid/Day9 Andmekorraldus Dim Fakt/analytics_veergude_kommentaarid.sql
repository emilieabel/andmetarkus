-- Tähtskeemi vaadete kommentaarid (PostgreSQL)
-- Skeem: analytics
-- Käivita pärast vaadete loomist. Kirjeldused on mõeldud kataloogile,
-- Power BI Description väljale ja inimesele, kes kell 17.40 küsib
-- «mis see veerg ka jälle oli».
--
-- Siin on ainult veerud, millel on lõks, päritolu või arvutusreegel.
-- Ilmselgeid nimesid (linn, aasta, kuu) ei kommenteerita.
-- Apostroof tekstis: kaks ülakoma ('') — muidu Postgres arvab, et string on läbi.

COMMENT ON VIEW analytics.dim_klient IS
'Inimene, mitte ostukorv. Üks rida = üks klient_id. Nime siit juhtlauale ära lohista — kaks inimest võivad kanda sama nime.';

COMMENT ON COLUMN analytics.dim_klient.klient_id IS
'See number ON inimene. Poes elavad kaks Kati Lepikut (id 5 ja 25). GROUP BY nimi teeb neist ühe müütilise supermüügiga Kati. Liide faktiga käib alati siit, mitte nimest.';

COMMENT ON COLUMN analytics.dim_klient.piirkond IS
'Ei ole omavalitsus ega maakond. Tallinn ja Tartu hoiavad oma nime; kõik ülejäänu on ''muu'', et sõõrik ei näeks välja nagu confetti. Kui keegi küsib ''miks Viljandit ei ole'' — sellepärast.';

COMMENT ON COLUMN analytics.dim_klient.liitumise_kuupäev IS
'Päev, mil klient meie nimekirja tekkis. See ei ole esimene ost. Keegi võib liituda jaanuaris ja osta alles mais — või mitte kunagi (kliendid 31–35 ootavad siiani).';

COMMENT ON COLUMN analytics.dim_klient.liitumise_aasta IS
'Liitumise aasta, juba INTEGER-ina. Selleks, et keegi ei teeks Power Query-s Date.Year neljas kohas erineva nimega.';


COMMENT ON VIEW analytics.dim_toode IS
'Riiul: mis me müüme, mis see nimekirjas maksab, kelle osakond vastutab. Müüdud hind elab faktis, mitte siin.';

COMMENT ON COLUMN analytics.dim_toode.nimetus IS
'ERPis on nimedel kombeks paljuneda: riiulinimi, kassa 20-täheline kleeps, kampaania pealkiri, tarneetikett. See veerg on tooted.nimetus — kataloogi / arverea nimi, see mida inimene arvel ära tunneb. Mitte kassateksti, mitte URL-slugi.';

COMMENT ON COLUMN analytics.dim_toode.hind_ilma_km IS
'Hinnakirja netohind (tooted.hind). See on palve, mitte tulu. Tegelik raha pärast soodustust tuleb fact_myyk.rida_allahindlusega_ilma_km.';

COMMENT ON COLUMN analytics.dim_toode.hind_koos_km IS
'Sama hinnakiri, kategooria KM peale maalitud. Vitriini ja kassasildi jaoks. Käibeks ära summeeri — muidu müüd riiulihindu, mitte oste.';

COMMENT ON COLUMN analytics.dim_toode.hinna_klass IS
'Meie kodune sortiment, mitte ERP väli: alla 100 odav, alla 500 keskmine, ülejäänu kallis. Kui turundus tahab piiri 79.99 peale, muudetakse ÜKS CASE — mitte üheksa aruannet.';

COMMENT ON COLUMN analytics.dim_toode.kategooria_id IS
'Tuli kaasa kategooriad-tabelist. Operatiivne seos on ikka nimega: tooted.kategooria = kategooriad.nimetus, sest keegi ei jõudnud välisvõtit ära teha. Ära ''paranda'' seda Power BI-s ID peale, kui allikas nime kasutab.';

COMMENT ON COLUMN analytics.dim_toode.kategooria IS
'Kategooria NIMI (kategooriad.nimetus), mitte number. Sama sõne mis tooted.kategooria. Kui kirjapilt allikas muutub, katkeb seos enne, kui keegi ID-d igatsema hakkab.';

COMMENT ON COLUMN analytics.dim_toode.osakond IS
'Riiuli peremees majas (nt IT, Köök). Üks osakond peab mitu kategooriat. Küsimus ''kes müüs kõige rohkem'' käib siia, mitte kategooria peale — muidu võidab see, kes kategooriad kõige peenemaks lõikas.';

COMMENT ON COLUMN analytics.dim_toode.km_maar IS
'Protsent kategooriad.km_maar-st: tavaliselt 24, Mängud ja Mööbel 22. See ei ole raha. Raha on fact_myyk.rida_km.';

COMMENT ON COLUMN analytics.dim_toode.on_soodus_km IS
'Tõene, kui km_maar < 24. Lipp selleks, et keegi ei kirjutaks seda võrdlust DAX-is kolmandat korda valesti.';


COMMENT ON VIEW analytics.dim_aeg IS
'Kalender, mitte müük. Iga kuupäev on olemas ka siis, kui sel päeval ei müüdud midagi — muidu joongraafik hüppab aukudest üle ja keegi peab seda ''tugevaks nädalavahetuseks''.';

COMMENT ON COLUMN analytics.dim_aeg.kuupäev_id IS
'Täisarv kujul YYYYMMDD (nt 20260315). Faktiga liimitakse SIIT, mitte kuupäeva-tüüpi veerust. Integersõbralik tähtskeem: vähem vaidlusi ajavööndi ja kellaaja 00:00 üle.';

COMMENT ON COLUMN analytics.dim_aeg.aasta_kuu IS
'Tekst ''2026-03''. Slicer, mis sorteerib nagu aeg, mitte nagu tähestik (muidu tuleb aprill enne jaanuari ja keegi teeb slaidile vale järelduse).';

COMMENT ON COLUMN analytics.dim_aeg.aasta_kvartal IS
'Tekst ''2026-Q1''. Sama mõte mis aasta_kuu, kvartali graafiku jaoks.';

COMMENT ON COLUMN analytics.dim_aeg.nadala_paev IS
'ISO nädalapäev: 1 = esmaspäev, 7 = pühapäev. Exceli WEEKDAY() alustab kuskilt mujalt ja teeb pühapäevast esimese. Ära sega neid.';

COMMENT ON COLUMN analytics.dim_aeg.on_naidalopp IS
'Laupäev või pühapäev. Pood võib müüa, ladu ei pruugi komplekteerida. Filter ''kas nädalavahetus sõi meie tarneaja'' elab siin.';


COMMENT ON VIEW analytics.fact_myyk IS
'Tera: üks rida = üks müügirida (tellimus + toode). See EI OLE tellimus. COUNT(*) siit on ridade arv; tellimuste arv on DISTINCT tellimus_id.';

COMMENT ON COLUMN analytics.fact_myyk.klient_id IS
'Kes ostis. Nime siin meelega ei ole: muidu isikuandmed korduksid igal real ja kaks Kati Lepikut sulaksid GROUP BY nimi peal kokku. Tee täht: siit → dim_klient.klient_id.';

COMMENT ON COLUMN analytics.fact_myyk.kuupäev_id IS
'Tellimuse kuupäev täisarvuna YYYYMMDD. Osutab dim_aeg-ile, mitte laokella ekraanile ega makseterminali kviitungiajale.';

COMMENT ON COLUMN analytics.fact_myyk.staatus IS
'Toorstaatus tellimused.staatus-est (Täidetud, Ootel, Tühistatud, …). Kasulik tühistamiste osakaalu jaoks. Käibe filtriks kasuta taidetud — muidu unustab keegi ühe staatuse ära.';

COMMENT ON COLUMN analytics.fact_myyk.taidetud IS
'''Täidetud'' või tühi. Spikker: käive loeb AINULT ridu, kus siin on Täidetud. Ootel ja tühistatud on lootused ja kahetsused, mitte tulu.';

COMMENT ON COLUMN analytics.fact_myyk.tarneviis IS
'Kuidas kraam majast välja läks (Pakiautomaat, kuller, …). Kolmerealine tellimus on ikka ÜKS tarne. Loenda DISTINCT tellimus_id, mitte ridu — muidu võidab see viis, millega osteti mitu asja korraga.';

COMMENT ON COLUMN analytics.fact_myyk.kogus IS
'Tükid sellel real. Ei ole tellimuste arv ja ei ole eurod. ''Mida osteti rohkem, odavat või kallist?'' käib SIIT, mitte käibest — muidu võidab diivan alati hiire üle.';

COMMENT ON COLUMN analytics.fact_myyk.rida_tais_summa_ilma_km IS
'Mis kassa oleks laulnud, kui keegi poleks sooduskoodi leiutanud. Neto, enne allahindlust, ilma KM. Võrdluseks ''kui palju me ära andsime'', mitte käibeks.';

COMMENT ON COLUMN analytics.fact_myyk.rida_allahindlusega_ilma_km IS
'SEE number. Pärast allahindlust, ilma KM. Käive = SUM(see), kus taidetud = Täidetud. Kui kaks käivet ei klapi, alusta siit, mitte Power Queryst.';

COMMENT ON COLUMN analytics.fact_myyk.allahindluse_summa IS
'Raha, mille me kliendile kinkisime (täishind miinus soodushind), neto. Positiivne number. See ei ole miinusmärgiga käive — ära lahuta seda kaks korda.';

COMMENT ON COLUMN analytics.fact_myyk.rida_km IS
'KM, arvutatud juba allahinnatud netolt, toote kategooria määraga. Riigile. Mitte meile.';

COMMENT ON COLUMN analytics.fact_myyk.rida_koos_km IS
'Mis klient selle rea eest tegelikult välja käis (kui tellimus lõpuni jõudis): soodustus maha, KM peale. Ilus kassatõde. Käibe definitsioon see ei ole.';


-- Kontroll: mis kataloogis nüüd kirjas on
SELECT
    n.nspname AS skeem,
    c.relname AS vaade,
    a.attname AS veerg,
    col_description(a.attrelid, a.attnum) AS kommentaar
FROM pg_attribute a
JOIN pg_class c ON c.oid = a.attrelid
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'analytics'
  AND c.relkind = 'v'
  AND a.attnum > 0
  AND NOT a.attisdropped
  AND col_description(a.attrelid, a.attnum) IS NOT NULL
ORDER BY c.relname, a.attnum;
