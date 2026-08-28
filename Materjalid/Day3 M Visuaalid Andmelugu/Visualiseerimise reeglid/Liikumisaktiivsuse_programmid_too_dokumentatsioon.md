# Töö dokumentatsioon

**Aruanne:** Liikumisaktiivsuse programmid.pbip  
**Andmeallikas:** Eesti liikumisaktiivsuse tegevuskava avalik API (`https://app.liigume.ee/api`)  
**Tööriist:** Microsoft Power BI (PBIP / TMDL)  
**Andmete seis:** API vastus 28.08.2026 (100 tegevust; viimati muudetud allikas 18.–30.06.2026)  
**Keel / kultuur:** et-EE

---

## Sisukord

1. [Ettevõtte ja uurimisprobleemi tutvustus](#1-ettevõtte-ja-uurimisprobleemi-tutvustus)
2. [Grupitöö plaan](#2-grupitöö-plaan)
3. [Ärisõnastik](#3-ärisõnastik)
4. [Andmekaitse kirjeldus](#4-andmekaitse-kirjeldus--mis-alustel-andmeid-töödeldakse)
5. [Andmemudel, andmesõnastik](#5-andmemudel-andmesõnastik)
6. [Andmeallikad ja andmevoog](#6-andmeallikad-ja-andmevoog)
7. [Näidisandmestiku loomine, hankimine, import](#7-näidisandmestiku-loomine-hankimine-andmestiku-import)
8. [Andmete kvaliteedi kontroll](#8-andmete-kvaliteedi-kontroll)
9. [Andmete töötlemine](#9-andmete-töötlemine)
10. [Andmete analüüs](#10-andmete-analüüs)
11. [Kirjeldav raport / analüüs](#11-kirjeldav-raport--analüüs)
12. [Andmelugu, järeldused](#12-andmelugu-järeldused)

---

## 1. Ettevõtte ja uurimisprobleemi tutvustus

### 1.1 Organisatsioon

Andmestiku omanik ja tegevuskava seire platvormi haldaja on **SA Liikumisharrastuse kompetentsikeskus** (LHKK, liigume.ee). Keskuse asutas 2022. aasta sügisel Eesti Olümpiakomitee, et arendada ja koordineerida liikumisharrastust üleriigiliselt. Missioon on olla liikumispöörde eestvedaja, visioon aastaks 2035 — **Euroopa liikuvaim rahvas**.

Tegevuskava ise ei ole ühe asutuse siseprojekt. 2022. aasta sügisel algatasid kultuuri-, sotsiaal- ning haridus- ja teadusministrid valdkondadeülese koostöö; koostamist vedas **Kultuuriministeerium**. 2023. aastal valmis ühine **liikumisaktiivsuse tegevuskava**, mis tugineb arengustrateegiale „Eesti 2035“ ja spordipoliitika alusdokumendile **Sport 2030** (eesmärk: aastaks 2030 liigub ja spordib vähemalt kaks kolmandikku elanikest). Aastatel 2024–2025 liitusid kava kaitse- ja transpordivaldkond (sh Eesti rattastrateegia 2040).

Struktuurilt järgib kava Maailma Terviseorganisatsiooni ülemaailmset kehalise aktiivsuse tegevuskava **WHO GAPPA 2018–2030** (*Global Action Plan on Physical Activity*) nelja strateegilist suunda ja 20 poliitikameedet.

### 1.2 Miks see teema on oluline

Liikumisaktiivsus Eestis on alla tervisesoovituste:

| Näitaja | Väärtus | Allikas (LHKK / tegevuskava avalik vaade) |
|---|---|---|
| Täiskasvanud, kes tegelevad liikumisharrastuse või spordiga rohkem kui kord nädalas | 44% | liigume.ee/tegevuskava |
| 15-aastased, kes on vähemalt viiel päeval nädalas kehaliselt aktiivsed | 37% | samas |
| Vanemaealised (55+), kes on aktiivsed rohkem kui 2 päeval nädalas | 19% | samas |
| 4. klassi lapsed, kes on ülekaalulised või rasvunud | 34% | samas |
| Ajateenijad, kes sooritavad kehalise võimekuse testi teenistuse alguses positiivselt | 31% | samas |
| Tervena elada jäänud aastad (2024) | mehed 56,8; naised 60,6 | Statistikaamet, tsiteeritud tegevuskavas |

WHO soovitab täiskasvanutel liikuda vähemalt 2,5–5 tundi nädalas mõõduka intensiivsusega. Enamik elanikkonnast seda ei täida. Madal kehaline aktiivsus suurendab krooniliste haiguste riski ja lühendab tervena elatud aastaid.

### 1.3 Uurimisprobleem

Tegevuskava on rulluv dokument (praegu 100 avalikku tegevust, periood kuni 2030) ja seda seiratakse veebirakenduses app.liigume.ee. Avalik vaade näitab tegevusi kaardina, kuid **ei anna analüütikule koondpilti**: kui suur osa kavast on tehtud, milline WHO suund on üle- või alakaetud, kes tegelikult juhib elluviimist, kui hästi on täidetud edenemine ja indikaatorid ning kus on andmeaugud.

**Uurimisküsimused**

1. Kui kaugel on 100 tegevuse portfell staatuse, tüübi ja ajaperioodi järgi?
2. Kuidas jaguneb vastutus asutuste ja WHO GAPPA suundade vahel?
3. Kas kõik 20 poliitikameedet on tegevustega kaetud ja millised sihtrühmad on fookuses?
4. Kui usaldusväärne on seireandmestik (kuupäevad, edenemise %, indikaatorid, partnerid)?

**Töö eesmärk.** Koostada Power BI aruanne, mis muudab avaliku API andmed juhtimislaadseks ülevaateks: mahud, võrgustik, poliitikakate ja andmekvaliteet ühes mudelis.

**Sihttarbijad.** Tegevuskava koordinatsioon (LHKK, Kultuuriministeerium), ministeeriumide ja ametite kontaktisikud, kursuse hindajad. Aruanne on õppetöö analüütiline prototüüp, mitte LHKK ametlik seirearuanne.

---

## 2. Grupitöö plaan

Töö jagunes neljaks etapiks, mis vastavad andmeprojekti elutsüklile. Iga etapp lõppes kontrollitava tulemiga (Power Query päring, TMDL-mudel, aruande leht või see dokumentatsioon).

### 2.1 Tööjaotus teemade kaupa

| Etapp | Sisu | Tulem |
|---|---|---|
| A. Probleem ja mõisted | Ettevõtte taust, uurimisküsimused, ärisõnastik, andmekaitse alused | ptk 1–4 |
| B. Andmed ja mudel | API ühendus, Power Query, tähemudel, mõõdikud | ptk 5–9, Semantic Model |
| C. Visuaalid | Viis aruandelehte, teema, filtrid, Info-leht | Report |
| D. Analüüs ja lugu | Kirjeldav statistika, andmelugu, järeldused | ptk 10–12 |

### 2.2 Ajagraafik (loogiline järjekord)

| Järjekord | Tegevus | Sõltuvus |
|---|---|---|
| 1 | API otspunktide kaardistamine (`activities`, `organizations`, `policies`) | — |
| 2 | Toorandmete laadimine ja skeemi kirjeldamine | 1 |
| 3 | Kvaliteedikontroll (tühjad kuupäevad, edenemine, mitu-mitmele väljad) | 2 |
| 4 | Tähemudeli koostamine (fakt + 3 dimi + mõõdikud) | 3 |
| 5 | DAX-mõõdikud (ülevaade, edenemine, võrgustik, poliitika, andmekvaliteet) | 4 |
| 6 | Aruandelehed Ülevaade → Organisatsioonid → Poliitikad → Edenemine → Info | 5 |
| 7 | Iseend dokumenteeriv mudel (`INFO.VIEW`) Info-lehel | 5–6 |
| 8 | Kirjeldav analüüs ja andmelugu | 6 |

### 2.3 Tööriistad ja kokkulepped

- **Power BI Desktop** (DevMode, PBIP), kultuur `et-EE`.
- **Import-režiim**, värskendus käsitsi (*Home → Refresh*), andmeallika autentimine *Anonymous*.
- Nimed eesti keeles tarbijale (veerud, mõõdikud), tehnilised võtmed inglise keeles (`activity_id`, `lead_org_id`).
- Mitu-mitmele seoseid ei modelleerita: partnerid, meetmed, sihtrühmad ja indikaatorid jäävad tegevuse reale ühele väljale.
- Implicit measures on keelatud (`discourageImplicitMeasures`) — kõik koondarvud on explitsiitsed DAX-mõõdikud.

### 2.4 Riskid ja leevendus

| Risk | Mõju | Leevendus |
|---|---|---|
| API muutub või on kättesaamatu | Aruanne ei värskene | Dokumenteeritud otspunktid; struktuur on stabiilne JSON |
| Edenemise % puudub enamikul ridadel | KPI on kallutatud | Eraldi mõõdik „Tegevused ilma edenemiseta“; keskmine ainult täidetud ridadel |
| Partnerid/meetmed ühel tekstiväljal | Ei saa unikaalset partnerit filtrerida | Arvuveerud (`Partnerite arv`, `Meetmete arv`) ja selged visuaalipealkirjad |
| Grupiliikmete nimed ei ole selles failis fikseeritud | Hindamisel rollijaotus | Täiendada esilehele nimed ja allkirjad enne esitamist |

---

## 3. Ärisõnastik

Mõisted, mida aruandes ja mudelis kasutatakse. Tehniline andmesõnastik on peatükis 5.

| Mõiste | Tähendus selles töös |
|---|---|
| **Liikumisaktiivsuse tegevuskava** | Valdkondadeülene, rulluv riiklik kava kehalise aktiivsuse tõstmiseks elukaareüleselt (alates 2023, seire kuni 2030). |
| **Tegevus (activity)** | Üks kirje kavas: projekt, programm, uuring, kampaania või õigusruumi muudatus. Mudelis üks rida tabelis `fact_activity`. |
| **Tegevuse tüüp** | Kaks väärtust: *Eesti projektid ja programmid* või *Teadus ja innovatsioon*. |
| **Staatus** | Elluviimise seis: *Pole alustatud*, *Töös*, *Tehtud*. Järjestus 1–3. |
| **Edenemine %** | Tegevuse valmidus 0–100. Paljudel ridadel puudub. |
| **Indikaator** | Tegevuse alameesmärk nime ja staatusega (*Ootel*, *Pooleli*, *Lõpetatud*, *Mõõdik*). |
| **Sihttulemus** | Lühike kirjeldus, mida tegevuse lõpuks oodatakse. |
| **Periood** | Kavandatud ajavahemik tekstina (nt `2025–2027`) või väärtus *Pidev* (lõputa algatus). |
| **Juhtorganisatsioon** | Asutus, kes vastutab elluviimise eest (`lead_org_id` → `dim_organization`). |
| **Partner** | Kaasatud asutus. API-s loend `partner_ids`; mudelis komadega tekst `Partnerid`. |
| **Organisatsiooni tüüp** | *Ministeerium*, *Riigiamet*, *Riigiasutus*, *MTÜ*, *Ülikool*, *KOV*, *Muu*. |
| **WHO suund (GAPPA)** | Neli strateegilist suunda: aktiivne ühiskond, keskkond, inimene, struktuurid. |
| **Poliitikameede** | GAPPA 20 meedet (koodid 1.1–4.5). Tegevusel võib olla mitu meedet. |
| **Sihtrühm** | API väärtused: *Lapsed ja noored*, *Elukaareülene*, *Keskkond*, *Teadus ja innovatsioon*. |
| **Partnerlus** | Üks seos tegevuse ja partnerasutuse vahel; mõõdik `Partnerluste arv` liidab need kokku. |
| **Pidev tegevus** | Algatus ilma kindla lõputa; tihti puuduvad algus- ja lõppkuupäev. |
| **Tähtaeg ületatud** | Lõppkuupäev on möödas, kuid staatus ei ole *Tehtud*. |
| **LHKK** | SA Liikumisharrastuse kompetentsikeskus. |
| **Sport 2030** | Eesti spordipoliitika alusdokument; kvantitatiivne siht kahele kolmandikule elanikest. |

### WHO GAPPA neli suunda (allikas: `policies`, `is_direction = 1`)

| Kood | Suund mudelis | Fookus |
|---|---|---|
| 1 | Loome aktiivset ühiskonda | Sotsiaalsed normid, teadlikkus, kampaaniad, hoiakud |
| 2 | Loome aktiivset keskkonda | Ruum, taristu, liiklusohutus, avalik ruum |
| 3 | Loome aktiivset inimest | Programmid, haridus, tervis, sihtrühmade võimalused |
| 4 | Loome aktiivseid struktuure | Juhtimine, andmed, teadus, rahastus, eestkoste |

---

## 4. Andmekaitse kirjeldus – mis alustel andmeid töödeldakse?

### 4.1 Milliseid andmeid töödeldakse

Töödeldakse **avalikke haldusandmeid** tegevuskava kohta: asutuste nimed, tegevuste pealkirjad, staatused, kuupäevad, poliitikameetmed, sihtrühmade sildid. Andmestikus **ei ole** füüsiliste isikute nimesid, isikukoode, kontaktandmeid, terviseandmeid ega muid GDPR eriliigilisi isikuandmeid (IKÜM art 9).

API on avalik ja autentimata (`Anonymous`). Sama sisu on nähtav veebis app.liigume.ee.

### 4.2 Kas tegemist on isikuandmetega?

**Isikuandmete kaitse üldmäärus (IKÜM / GDPR) kohaldub isikuandmetele** (art 2 ja 4). Asutuste (juriidiliste isikute) nimed, lühendid ja tüübid ei ole isikuandmed. Tegevuste kirjeldused on poliitika- ja programmitasandi tekstid.

Kui mõnes vabatekstiväljas (*Sihttulemus*, *Tegevus*) esineks juhuslikult isikunimi, oleks tegemist avaliku ametitegevuse kontekstiga, mitte varjatud töötlemisega. Selles API väljavõttes sellist vajadust ei ilmnenud; analüüs kasutab koondnäitajaid.

**Järeldus:** käesoleva aruande andmestik ei ole isikuandmete töötlemine IKÜM mõttes. Alljärgnev õiguslik raamistik on siiski kirjas, sest tegemist on avaliku sektori teabega ja õppetöö dokumendiga.

### 4.3 Õiguslikud alused (kui raamistik laiendada)

| Alus | Rakendus siin |
|---|---|
| **Avaliku teabe seadus (AvTS)** | Tegevuskava on avalik teave; kättesaadavus veebis on teabevaldaja valik. Analüüs kasutab juba avalikustatud teavet. |
| **IKÜM art 6 lg 1 p e** | Avaliku ülesande täitmine (tegevuskava seire) on teabevaldaja, mitte üliõpilasrühma alus. |
| **IKÜM art 6 lg 1 p f** | Õigustatud huvi: õppetöö ja avaliku poliitika analüüs, kui isikuandmeid siiski esineks; huvi kaalub üles minimaalse riive, sest andmed on juba avalikud. |
| **IKÜM art 89 / õppetöö** | Andmeid kasutatakse ainult kursuse analüüsi ja aruande koostamiseks, mitte profiilianalüüsiks ega turunduseks. |
| **Andmete minimeerimine (art 5)** | Imporditakse ainult analüüsiks vajalikud väljad; peidetud on tehnilised võtmed. |

### 4.4 Töötlemise põhimõtted praktikas

1. **Eesmärgipiirang.** Andmeid kasutatakse tegevuskava seire visualiseerimiseks õppetöös.
2. **Säilitamine.** Koopia elab Power BI import-mudelis kohalikus `.pbip` projektis. Pilve avaldamist (Power BI Service) selles töös ei nõuta; kui avaldataks, tuleks kontrollida, et aruanne jääb sama avaliku teabe piiresse.
3. **Edastamine.** Kolmandatele isikutele isikuandmeid ei edastata. API päringud lähevad LHKK serverisse TLS-ühendusega.
4. **Turvalisus.** Autentimist ei kasutata, sest allikas on avalik. Salajasi võtmeid projektis ei ole.
5. **Puuduvad eriliigilised andmed.** Terviseuuringute *viited* (`research_ids`) on identifikaatorid, mitte uuritavate isikute kirjed.
6. **Vastutav töötleja avalikus ruumis** on teabevaldaja (LHKK / tegevuskava koordineerivad ministeeriumid). Üliõpilased on selles töös andmete **kasutajad**, mitte uue isikuandmete kogu loojad.

---

## 5. Andmemudel, andmesõnastik

### 5.1 Mudeli tüüp

Semantiline mudel on **tähemudel (star schema)**: keskel fakt `fact_activity` (üks rida = üks tegevus), ümber kolm dimensiooni.

```
dim_direction  1──<  fact_activity  >──1  dim_organization
                      │
                      │ Alguskuupäev  (aktiivne)
                      │ Lõppkuupäev   (mitteaktiivne)
                      ▼
                   dim_date
```

Lisaks kaks arvutatud kataloogtabelit aruande Info-lehele (`dim_measure_info`, `dim_mudeli_objekt`) ja mõõdikute konteiner `_Measures`.

**Seosed**

| Seos | From | To | Aktiivne | Kardinaalsus |
|---|---|---|---|---|
| fact_activity_to_dim_direction | `who_direction_id` | `direction_id` | jah | m:1 |
| fact_activity_to_dim_organization | `lead_org_id` | `organization_id` | jah | m:1 |
| fact_activity_to_dim_date | `Alguskuupäev` | `Kuupäev` | jah | m:1 |
| fact_activity_end_to_dim_date | `Lõppkuupäev` | `Kuupäev` | ei | m:1 |

Auto Date/Time on välja lülitatud. Kalender on eraldi tabel `CALENDAR(2023-01-01, 2030-12-31)`.

**Teadlik lihtsustamine.** Partnerid, poliitikameetmed, sihtrühmad ja indikaatorid ei ole sildtabelid. Need on tegevuse real **denormaliseeritud tekst** (komad / semikoolonid) plus loendurid. Seoseid mitu-mitmele ei ole. See hoiab mudeli lihtsa, kuid tähendab, et unikaalset partnerit või meedet ei saa viilutada nagu dimensiooni — aruande pealkirjad ütlevad selle kasutajale otse.

### 5.2 Tabelid

| Tabel | Roll | Ridu (allikas) | Partitsioon |
|---|---|---|---|
| `fact_activity` | Fakt: tegevused | 100 | Power Query, import |
| `dim_organization` | Juhtorganisatsioonid | 51 | Power Query, import |
| `dim_direction` | WHO suunad (`is_direction = 1`) | 4 | Power Query, import |
| `dim_date` | Kalender | 2023–2030 | DAX `CALENDAR` |
| `_Measures` | Kõik DAX-mõõdikud | 1 dummy-rida | arvutatud |
| `dim_measure_info` | Mõõdikute kataloog | `INFO.VIEW.MEASURES` | arvutatud |
| `dim_mudeli_objekt` | Tabelite/veergude kirjeldused | `INFO.VIEW` | arvutatud |

### 5.3 Andmesõnastik — `fact_activity`

| Veerg | Tüüp | Kirjeldus |
|---|---|---|
| activity_id | täisarv, PK, peidetud | Tegevuse identifikaator |
| lead_org_id | täisarv, peidetud | Juhtorganisatsiooni FK |
| who_direction_id | täisarv, peidetud | WHO suuna FK |
| Tegevuse nr | täisarv | Järjekorranumber kavas |
| Kood | tekst | Nt `TEG-2026-001` |
| Tegevus | tekst | Täisnimi |
| Lühinimi | tekst | Lühike nimi |
| Tegevuse tüüp | tekst | Projekt/programm või teadus |
| Periood | tekst | Ajavahemik või *Pidev* |
| Alguskuupäev | kuupäev | Seos `dim_date` |
| Lõppkuupäev | kuupäev | Mitteaktiivne seos `dim_date` |
| Staatus | tekst | Pole alustatud / Töös / Tehtud |
| Staatuse järjekord | täisarv, peidetud | 1 / 2 / 3 / 9 |
| Sihttulemus | tekst | Oodatav tulemus |
| Juhtorganisatsioon | tekst | Denormaliseeritud nimi |
| Juhtorg lühend | tekst | Lühend |
| Juhtorg tüüp | tekst | Asutuse liik |
| Partnerid | tekst | Nimed, komadega |
| Poliitikameetmed | tekst | Kood + nimi, komadega |
| Sihtrühmad | tekst | Komadega |
| Indikaatorid | tekst | `nimi (staatus)`, semikooloniga |
| Edenemine protsent | täisarv | 0–100, sageli tühi |
| Partnerite arv | täisarv, peidetud | `List.Count(partner_ids)` |
| Meetmete arv | täisarv, peidetud | `List.Count(policy_ids)` |
| Indikaatorite arv | täisarv, peidetud | Indikaatorite loenduri pikkus |
| Lõpetatud indikaatorite arv | täisarv, peidetud | Staatus = Lõpetatud |
| Uuringute arv | täisarv, peidetud | `research_ids` pikkus |
| Sihtrühmade arv | täisarv, peidetud | Sihtrühmade loenduri pikkus |
| Kestus päevades | täisarv | Lõpp − algus, kui mõlemad olemas |

Hierarhia: **Tegevuse tüüp ja staatus**.

### 5.4 Andmesõnastik — dimensioonid

**dim_organization**

| Veerg | Kirjeldus |
|---|---|
| organization_id | PK |
| parent_organization_id | Ülemasutuse id (peidetud) |
| Organisatsioon | Nimi |
| Lühend | Lühend |
| Organisatsiooni tüüp | Liik |
| Peaorganisatsioon | Ülemasutuse nimi, kui teada |

Hierarhia: **Organisatsiooni tüüp → Organisatsioon**.

**dim_direction**

| Veerg | Kirjeldus |
|---|---|
| direction_id | PK (sama id mis policies-tabelis) |
| Suuna kood | 1–4 |
| Suund | Nimi |
| Kirjeldus | Suuna pikk tekst |

**dim_date:** Kuupäev, Aasta, Kuu nr/Kuu, Kvartal nr/Kvartal, Aasta-kuu. Hierarhia **Aasta → Kvartal → Kuu**.

### 5.5 Mõõdikud (`_Measures`)

| Kaust | Mõõdik | Loogika |
|---|---|---|
| 1. Ülevaade | Tegevuste arv | `COUNTROWS(fact_activity)` |
| | Tehtud / Töös / Alustamata tegevused | `CALCULATE` staatuse filtriga |
| | Tehtud % | Tehtud / kõik |
| 2. Edenemine | Keskmine edenemine % | `AVERAGE(Edenemine protsent) / 100` (ainult täidetud read) |
| | Indikaatorite arv | `SUM` |
| | Lõpetatud indikaatorid | `SUM` |
| | Lõpetatud indikaatorite % | jagatis |
| | Keskmine kestus päevades | `AVERAGE(Kestus päevades)` |
| 3. Võrgustik | Organisatsioonide / Juhtorganisatsioonide arv | `DISTINCTCOUNT(lead_org_id)` |
| | Partnerluste arv | `SUM(Partnerite arv)` |
| 4. Poliitika | Poliitikameetmete arv | `SUM(Meetmete arv)` — kirjeid, mitte unikaalseid meetmeid |
| | Sihtrühmade arv | `SUM(Sihtrühmade arv)` |
| 5. Andmekvaliteet | Tegevused ilma partnerita | `Partnerite arv = 0` |
| | Tegevused ilma kuupäevata | `ISBLANK(Alguskuupäev)` |
| | Tegevused ilma edenemiseta | `ISBLANK(Edenemine protsent)` |
| | Tähtaeg ületatud | lõpp < TÄNA ja staatus ≠ Tehtud |

---

## 6. Andmeallikad ja andmevoog

### 6.1 Allikad

Kolm REST JSON otspunkti, Power Query *shared expressions*:

| Expression | URL | Sisaldus |
|---|---|---|
| Activities Source | `https://app.liigume.ee/api/activities` | 100 tegevust (pesad: partner_ids, policy_ids, indicators, target_groups, research_ids) |
| Organizations Source | `https://app.liigume.ee/api/organizations` | 51 asutust |
| Policies Source | `https://app.liigume.ee/api/policies` | 24 rida: 4 suunda + 20 meedet |

Lisallikas: DAX-kalender, mitte välisest failist.

Avalik veebivaade samale sisule: [app.liigume.ee](https://app.liigume.ee/). Taust: [liigume.ee/tegevuskava](https://liigume.ee/tegevuskava/).

### 6.2 Andmevoog

```
app.liigume.ee
        │  HTTPS, Anonymous
        ▼
Power Query (M)
  ├─ Activities Source ─┐
  ├─ Organizations Source ├─ ühendused, lookup, arvutusveerud, ümbernimetus, tüübid
  └─ Policies Source ───┘
        │
        ▼
Import semantic model (täht)
  fact_activity ── dim_organization
        ├── dim_direction
        └── dim_date
        │
        ▼
DAX mõõdikud + INFO.VIEW kataloogid
        │
        ▼
Aruanne (5 lehte)
  Ülevaade | Organisatsioonid | Poliitikad | Edenemine | Info
```

Värskendamine: Power BI Desktopis *Refresh*. Iga värskendus laadib kogu JSON uuesti (import, mitte DirectQuery).

### 6.3 Tegevuse JSON-i peamised väljad (toores)

`id`, `nr`, `code`, `name`, `name_short`, `activity_type`, `period`, `start_date`, `end_date`, `status`, `progress_pct`, `target_outcome`, `description`, `target_groups[]`, `who_direction_id`, `lead_org_id`, `partner_ids[]`, `policy_ids[]`, `research_ids[]`, `indicators[{id,name,status}]`, `read_more_link`, `last_modified_time`.

---

## 7. Näidisandmestiku loomine, hankimine, andmestiku import

### 7.1 Hankimine

Andmestikku ei genereeritud käsitsi ega Excelis. See on **tootmislähedane avalik API**, mida LHKK kasutab tegevuskava rakenduses. Õppetöö jaoks on see näidisandmestik: piiratud maht (100 rida), stabiilne skeem, puuduvad isikuandmed.

Hankimise sammud:

1. Kontrollida otspunkte brauseris või `GET` päringuga.
2. Power BI-s *Get data → Web* (või olemasolevad expressions) aadressidele `/api/activities`, `/api/organizations`, `/api/policies`.
3. Autentimine: Anonymous.
4. `Json.Document` → `Table.FromRecords`.

### 7.2 Import Power BI-sse

- Failivorming: **PBIP** (kaustad `.Report` ja `.SemanticModel`), mitte üks `.pbix`.
- Režiim: **Import**.
- Päringute järjekord mudelis: `fact_activity`, `dim_organization`, `dim_direction`, seejärel kolm Source expression’it.
- Organisatsioonid ja poliitikad puhverdatakse (`Table.Buffer`) enne tegevuste lookup’e, et vältida korduvaid API-kutseid samas värskenduses.

### 7.3 Miks mitte sünteetiline näidis

Sünteetilised andmed ei paljastaks tegelikke seireauke (72 rida ilma edenemiseta, 38 ilma alguskuupäevata, meetmete ebaühtlane kate). Uurimisprobleem on just **päris kava seiret lugeda**.

---

## 8. Andmete kvaliteedi kontroll

Kontroll tehti toor-JSON-il (28.08.2026) ja on mudelis korduvkasutatav nelja andmekvaliteedi mõõdikuga. Aruande leht **Edenemine** näitab neid KPI-dena.

### 8.1 Täielikkus

| Kontroll | Tulemus (n = 100) | Märkus |
|---|---|---|
| Tegevusi | 100 | Vastab avaliku vaate numbrile |
| Staatus täidetud | 100% | Kolm lubatud väärtust, muid ei ole |
| Tüüp täidetud | 100% | Kaks lubatud väärtust |
| WHO suund olemas | 100% | Kõik neli suunda esindatud |
| Juhtorganisatsioon olemas | 100% | 22 unikaalset juhti |
| Sihtrühm olemas | 100% | Igal real vähemalt üks |
| Poliitikameede olemas | 100% | Igal real vähemalt üks id |
| Indikaator olemas | 100% | Kokku 285 indikaatorit |
| Alguskuupäev puudub | **38** | Kõik 38 on perioodiga *Pidev* |
| Lõppkuupäev puudub | **41** | Seotud pidevate / avatud tegevustega |
| Edenemine % puudub | **72** | Täidetud ainult 28 real |
| Partnereid pole | **22** | `partner_ids` tühi loend |
| Tähtaeg ületatud | **0** | Möödunud lõpuga ridu, mis pole *Tehtud*, ei ole |

### 8.2 Vastuolud ja formaadid

- **Perioodi tekst ei ole ühtne.** Enamik kasutab en-kriipsu (`2025–2026`), mõni sidekriipsu (`2023-2025`, `2025-2026`), üks väärtus on ainult `2026`. Filtreerimine perioodi stringi järgi on habras; analüüs kasutab kuupäevi ja staatust.
- **Pidev vs kuupäev.** 41 tegevust on *Pidev*; neist 38-l puudub alguskuupäev. Kalendriga seotud visuaalid (algusaasta joon) jätavad need read vahele — see on oodatav, mitte viga mõõdikus.
- **Edenemine vs staatus.** 19 *Tehtud* rida on kõik edenemisega 100. Ülejäänud 9 täidetud edenemist on *Töös* (10–66%). 58-st *Töös* tegevusest enamikul edenemist pole — seire on staatusepõhine, mitte protsendipõhine.
- **Mitu väärtust ühel väljal.** Partner, meede, sihtrühm ja indikaator ei ole 1NF. Unikaalset meedet ei saa usaldusväärselt `CONTAINSSTRING` filtriga lugeda (osaliselt kattuvad nimed). Aruanne näitab neid tabeleid teadlikult „mitu väärtust ühel väljal“.
- **Poliitikameetmete arv mõõdikus** on *kirjete summa* (üks tegevus mitme meetmega suurendab arvu), mitte 20-st unikaalsest meetmest kaetud hulk. Unikaalseid meetmeid tegevustel on 17 (vt ptk 10).

### 8.3 Viidete terviklikkus

- Kõik `lead_org_id` ja `who_direction_id` väärtused leiti vastavatest allikatest (left join ei jätnud tühja juhtnime).
- `partner_ids` ja `policy_ids` lookup kasutab `Record.FieldOrDefault` — tundmatu id jääks vahele, mitte ei katkestaks värskendust.

### 8.4 Kvaliteedi järeldus mudelile

Andmestik on **struktuurselt korras** (võtmed, staatused, suunad) ja **sisuliselt auklik seireväljadel** (kuupäev, edenemine). Aruanne ei peida auke: need on eraldi KPI-d, mitte „puhas“ keskmine kogu 100 kohta.

---

## 9. Andmete töötlemine

Töötlus toimub Power Query M-keeles importimisel. Alljärgnev on `fact_activity` partitsiooni loogika lühidalt.

### 9.1 Ühendamised

1. Tegevused ⟕ organisatsioonid `lead_org_id = id` → `Juhtorganisatsioon`, `Juhtorg lühend`, `Juhtorg tüüp`.
2. `partner_ids` → nimed läbi organisatsioonide kaardi → `Partnerid`.
3. `policy_ids` → `policy_code + policy_measure` → `Poliitikameetmed`.
4. `target_groups` loend → unikaalsed, komadega `Sihtrühmad`.
5. `indicators` objektid → `nimi (staatus)`, semikooloniga `Indikaatorid`.

`dim_organization`: self-join `parent_organization_id` → `Peaorganisatsioon`.  
`dim_direction`: `policies` read, kus `is_direction = 1`.

### 9.2 Tuletatud veerud

| Veerg | Reegel |
|---|---|
| Partnerite / Meetmete / Indikaatorite / Uuringute / Sihtrühmade arv | vastava loendi pikkus (`null` = 0) |
| Lõpetatud indikaatorite arv | indikaatorid, mille `status = "Lõpetatud"` |
| Kestus päevades | `Duration.Days(end − start)`, kui mõlemad olemas |
| Staatuse järjekord | Pole alustatud=1, Töös=2, Tehtud=3, muu=9 |

### 9.3 Nime- ja tüübimuutused

Ingliskeelsed API väljad ümber eesti tarbijanimedeks (`name` → `Tegevus`, `start_date` → `Alguskuupäev` jne). Tüübid: täisarv, tekst, kuupäev.

### 9.4 Mida ei tehtud (teadlikult)

- Ei eemaldatud ridu (100 tegevust jäävad kõik alles).
- Ei täidetud puuduvaid kuupäevi ega edenemist vaikeväärtusega (moonutaks seiret).
- Ei normaliseeritud mitu-mitmele sildtabeliteks (lihtsuse ja aruande loetavuse huvides).
- Ei parandatud perioodi kirjapilku allikas (jääb kvaliteedileiuks).

### 9.5 DAX-töötlus pärast importi

- Kalendritabel.
- Mõõdikud filtrikontekstiga (`CALCULATE`, `DIVIDE`).
- `INFO.VIEW.MEASURES` / `TABLES` / `COLUMNS` — mudeli dokumentatsioon aruande sees, mitte eraldi Wordi käsitsi nimekiri.

---

## 10. Andmete analüüs

Analüüs on **kirjeldav** (sagedused, osakaalud, katvus). Põhjuse-tagajärje mudelit ega regressiooni ei ehitata: n = 100 on kogu avalik kava, mitte valim rahvastikust. Arvud on API seisuga 28.08.2026.

### 10.1 Mida mõõdetakse

| Küsimus | Meetod | Mõõdik / väli |
|---|---|---|
| Kui suur on portfell ja kui valmis see on? | Loendused, osakaal | Tegevuste arv, staatus, Tehtud % |
| Kas teadus vs programmid erinevad? | Risttabel | Tegevuse tüüp × staatus |
| Milline GAPPA suund kannab koormust? | Loendus suuna järgi | dim_direction |
| Kes juhib? | Loendus lead_org järgi | Juhtorganisatsioon |
| Kas kõik 20 meedet on kasutusel? | Unikaalsed policy_ids | võrdlus policies-loendiga |
| Kellele tegevused on suunatud? | Sihtrühmade sagedus | target_groups |
| Kas seire on täidetud? | Puuduvate väärtuste määr | andmekvaliteedi mõõdikud |
| Kui pikad on dateeritud tegevused? | Keskmine kestus | 59 rida, millel algus ja lõpp |

### 10.2 Arvutusreeglid, mis mõjutavad tõlgendust

- **Keskmine edenemine** ei jaga 72 tühja rida nulliks; DAX `AVERAGE` jätab tühjad välja. Tulemus ~78% kirjeldab ainult 28 rida, mitte kogu kava.
- **Poliitikameetmete arv** aruandes = 105 kirjet (summa tegevuste meetmete loenduritest), mitte 17 unikaalset meedet.
- **Partnerluste arv** = 176 (summa), unikaalseid partner-id-sid on 39.
- Kalendrivaated kasutavad **alguskuupäeva**; lõpp on mudelis olemas, kuid seos on mitteaktiivne.

### 10.3 Võrdlusalused

| Võrdlus | Kasutus |
|---|---|
| Sport 2030 (2/3 elanikest liigub) | Probleemi taust, mitte selle 100 rea KPI |
| WHO GAPPA 4 suunda × 20 meedet | Katvuse kontroll: millised meetmed on tühjad |
| Staatuse jaotus 19 / 58 / 23 | Tööde portfelli „tervis“ |
| Avaliku vaate 100 tegevust | Ridade arvu kokkusobivus |

---

## 11. Kirjeldav raport / analüüs

### 11.1 Portfell tervikuna

100 tegevusest **58 on töös, 23 alustamata, 19 tehtud** (tehtud osakaal **19,0%**). See ei tähenda, et kava on „19% valmis“: 41 tegevust on *Pidevad* (neist 35 töös) ja kava ulatub 2030. aastani. Tehtud rida on oodatult väike rulluva kava keskel.

**Tüüp.** 83 tegevust on Eesti projektid ja programmid, 17 teadus ja innovatsioon. Teadusest on tehtud 6 (35%), programmidest 13 (16%). Alustamata ridu on peaaegu ainult programmide seas (22 vs 1).

| Tüüp | Pole alustatud | Töös | Tehtud | Kokku |
|---|---:|---:|---:|---:|
| Eesti projektid ja programmid | 22 | 48 | 13 | 83 |
| Teadus ja innovatsioon | 1 | 10 | 6 | 17 |
| **Kokku** | **23** | **58** | **19** | **100** |

### 11.2 WHO suunad — struktuurid ülekaalus

| Suund (who_direction_id) | Tegevusi | Pole alustatud | Töös | Tehtud |
|---|---:|---:|---:|---:|
| Loome aktiivseid struktuure (14) | **47** | 10 | 28 | 9 |
| Loome aktiivset inimest (8) | 22 | 1 | 16 | 5 |
| Loome aktiivset keskkonda (16) | 19 | 9 | 8 | 2 |
| Loome aktiivset ühiskonda (22) | **12** | 3 | 6 | 3 |

Peaaegu pooled tegevused on suunal **struktuurid** (juhtimine, andmed, teadus, rahastus). **Aktiivne ühiskond** (hoiakud, kampaaniad) on kõige õhem. Keskkonnasuunal on suhteliselt palju alustamata ridu (9/19).

### 11.3 Juhtorganisatsioonid ja võrgustik

22 unikaalset juhtorganisatsiooni. Enim tegevusi juhib:

| Juht | Tegevusi (ligikaudu) |
|---|---:|
| Transpordiamet | 20 |
| SA Liikumisharrastuse kompetentsikeskus | 18 |
| Kliimaministeerium | 14 |
| Kultuuriministeerium | 8 |
| Tervise Arengu Instituut | 6 |
| HTM, Kaitseressursside Amet, Sotsiaalministeerium | 5+5+5 |

Transpordi ja kliima osakaal peegeldab rattastrateegia ja elukeskkonna liitumist kavaga 2024–2025. LHKK on nii kava „omaniku“ lähedane koordinaator kui ka sage juht.

Partnerlusi on **176** (78 tegevusel vähemalt üks partner, keskmiselt ~2,3; maksimum 7). **22 tegevust on ilma partnerita.** Unikaalseid partner-id-sid 39; organisatsioonide registris on 51 asutust (osa on ainult partner või ainult register, mitte juht).

### 11.4 Poliitikameetmed ja sihtrühmad

Tegevused viitavad **17 unikaalsele meetmele** 20-st GAPPA meetmest. Meetmekirjeid kokku 105 (keskmiselt 1,05 unikaalset meedet… tegelikult mitu id-d real; summa loenduritest). Kõige sagedasemad id-d:

| Meede | Suund | Tegevusi |
|---|---|---:|
| 4.1 Tugevdada poliitikat, juhtimist ja valitsemist | struktuurid | 16 |
| 4.2 Parandada ja lõimida andmesüsteeme | struktuurid | 11 |
| 4.3 Arendada teadus- ja arendustegevust | struktuurid | 11 |
| 1.4 Tugevdada tööjõu suutlikkust | ühiskond | 10 |
| 4.5 Arendada uuenduslikke rahastamismehhanisme | struktuurid | 9 |
| 3.1 Tugevdada liikumisõpetust ja koolipõhiseid programme | inimene | 9 |

**Ilma ühegi tegevuseta (28.08.2026):**

- 1.2 Kaasnevate hüvede tutvustamine  
- 1.3 Pakkuda suuremahulisi liikumisüritusi  
- 4.4 Laiendada eestkostetegevust  

Need kolm on just teadlikkuse, massiürituste ja eestkoste meetmed — kooskõlas sellega, et suund „aktiivne ühiskond“ on tegevuste arvult väikseim.

**Sihtrühmad** (sildid tegevustel; tegevusel võib olla mitu, siin API järgi valdavalt üks): Keskkond 31, Lapsed ja noored 30, Teadus ja innovatsioon 21, Elukaareülene 18. Vanemaealistele eraldi silti API-s ei ole (GAPPA meede 3.4 „Parandada eakate võimalusi“ esineb vaid 1 korral).

### 11.5 Aeg, kestus, indikaatorid

Algusaasta (62 dateeritud rida): 2023: 14, 2024: 8, 2025: 17, 2026: 15, 2027: 8, puudub: 38.

59 tegevusel on nii algus kui lõpp; keskmine kestus **1126 päeva** (~3,1 aastat), vahemik 364–2191 päeva. Lühikesed on ühe aasta projektid, pikad ulatuvad 2023–2028 / 2025–2030.

Indikaatoreid 285 (keskmiselt 2,85 tegevuse kohta, max 6). Staatused: Lõpetatud 109 (38,2%), Pooleli 73, Ootel 55, Mõõdik 48. Lõpetatud indikaatorite osakaal on kõrgem kui tehtud tegevuste osakaal — indikaator saab valmis enne kogu tegevuse sulgemist või *Pidev* tegevus kogub lõpetatud alameesmärke.

Uuringuviiteid (`research_ids`) on 161 kirjet 57 tegevusel.

### 11.6 Seirekvaliteet arvu keeles

| Näitaja | Arv | Osakaal |
|---|---:|---:|
| Ilma edenemise %-ta | 72 | 72% |
| Ilma alguskuupäevata | 38 | 38% |
| Ilma partnerita | 22 | 22% |
| Tähtaeg ületatud | 0 | 0% |
| Edenemine täidetud | 28 | 28% |
| Täidetud ridade keskmine edenemine | 78,3% | ainult need 28 |

**Tõlgendus.** Tähtaegu ei ole „ületatud“ andmestiku reeglite järgi. Seevastu edenemise protsent ei ole kasutuskõlblik kogu kava KPI — 72 tühja rida teeks iga „kogu keskmise“ valeks. Õige juhtimisnäitaja on **staatus** pluss **indikaatorite lõpetatus**, mitte keskmine %.

### 11.7 Aruande lehed (kuidas arvud on visuaalides)

| Leht | Küsimus, millele vastab | Peamised visuaalid |
|---|---|---|
| **Ülevaade** | Kui palju, mis staatuses, mis suunal, mis aastal? | KPI-d (tegevuste arv, tehtud osakaal, pole alustatud), tulbad tüübi/staatuse/suuna järgi, joon algusaasta järgi, filtreeritav loend |
| **Organisatsioonid** | Kes juhib, kui tihe on võrgustik? | Juhtide ja partnerluste KPI-d, tulbad juhi ja org. tüübi järgi, rollide tabel, „ilma partnerita“ |
| **Poliitikad** | Millised meetmed ja sihtrühmad? | Maatriks suund × staatus, meetmete ja sihtrühmade tabelid (mitu väärtust ühel väljal) |
| **Edenemine** | Kui kaugel ja kui puhas on seire? | Keskmine edenemine, indikaatorid, tähtaeg, puuduvad kuupäevad/edenemine, tegevuste tabel |
| **Info** | Kuidas mudel töötab? | INFO.VIEW kataloogid, leiud toorandmetest, allikad ja värskendus |

Ühine navigatsioon ja filtrid: WHO suund, tegevuse tüüp, algusaasta, staatus, juhtorganisatsioon. Nupp **Tühista filtrid** (järjehoidja). Teema: `LiikumineTheme` (taust `#F5F5F5`, aktsent türkiis `#2EC4B6`).

---

## 12. Andmelugu, järeldused

### 12.1 Lugu ühe lausega

Eesti liikumisaktiivsuse kava on 2026. aasta suveks **suur koostööportfell, mis ehitab peamiselt süsteeme** — juhtimist, andmeid, teadust ja taristu poliitikat —, samal ajal kui **inimeste hoiakute ja massilise osalemise suund on kõige õhem ning seireprotsent on enamiku ridade peal tühi**.

### 12.2 Kolm peatükki

**1. Kava on elus, mitte „valmis“.**  
58 tegevust töös ja 41 pidevat kirjet on rulluva kava normaalne kuju, mitte mahajäämus. 19 tehtud rida (sh seadusemuudatused, uuringud, 2023. aasta ühekordsed algatused) näitavad, et midagi on juba lukku löödud. Sport 2030 siht (kaks kolmandikku elanikest liigub) ei ole selle tabeli ridade arv; see on ühiskonna tulemus, mida need 100 rida peaksid aitama. Portfell on vahend.

**2. Raskuskese on struktuuridel, mitte ühiskonnal.**  
47 tegevust suunal „aktiivsed struktuurid“ versus 12 suunal „aktiivne ühiskond“ ei ole juhus. Kolm tühja GAPPA meedet (kaasnevate hüvede tutvustamine, suuremahulised liikumisüritused, eestkoste) on samast perest. Transpordiamet ja Kliimaministeerium juhivad mahult, sest rattastrateegia ja ruum on kavaga liitunud. See on tugevus (poliitika ulatub tervisest tänavaruumini) ja risk: kui struktuurid täituvad, aga kampaaniad, üritused ja eestkoste jäävad katmata, võib kava jääda „asutuste kava“, mitte inimeste harjumuste kava.

**3. Seiret saab juhtida staatuse, mitte protsendiga.**  
Edenemise % on täidetud 28 real ja need read on keskmiselt 78% peal — hea, aga valim on kallutatud (kõik 19 tehtut on 100). 72 tühja rida tähendab, et „keskmine edenemine kogu kavas“ oleks vale lugu. Kuupäevad puuduvad pidevatel tegevustel süsteemselt, mitte juhuslikult. Tähtaeg ületatud = 0 ütleb, et staatust uuendatakse vähemalt lõpu saabudes. Järelevalve jaoks on ausamad signaalid: **alustamata ridu keskkonnasuunal (9/19)**, **22 tegevust ilma partnerita**, **indikaatorite 38% lõpetatus** ja **kolm katmata meedet**.

### 12.3 Soovitused (andmetest, mitte poliitikaeelistusest)

1. **Täita või loobuda edenemise %-st.** Kas muuta väli kohustuslikuks *Töös* ridadel või eemaldada see KPI-st avalikus aruandes, et mitte jätta muljet 78% valmidusest.
2. **Pidevatele tegevustele anda vähemalt alguskuupäev** (nt kava kinnitamise aasta), et ajatelg ei kaotaks 38% portfellist.
3. **Katta või teadlikult kõrvale jätta meetmed 1.2, 1.3 ja 4.4** — praegu on auk dokumenteerimata.
4. **Normaliseerida partnerid ja meetmed** järgmises mudeliversioonis (sildtabelid), kui eesmärk on filtreerida „kõik Transpordiameti partnerlused“ või „kõik 3.4 tegevused“ ilma tekstiväljata.
5. **Jälgida keskkonnasuuna alustamata rida** — see on ainus suund, kus alustamata on peaaegu sama suur kui töös.

### 12.4 Töö piirangud

- Andmed on hetkeseis, mitte ajajada (last_modified on kitsas aken juunis 2026). Trendijoone „aasta“ on tegevuse *algusaasta*, mitte seirekuu.
- Mitu-mitmele lamedus piirab võrgustikuanalüüsi (nt graaf „kes kellega“).
- Sihtrühmade sildid ei kattu 1:1 GAPPA sihtrühmadega (puudu nt eakad, naised, maaelanikud eraldi).
- Aruanne ei mõõda elanike tegelikku liikumist (selleks on TAI / Turu-uuringud / EHIS) — ainult kava elluviimise kirjeid.
- Grupiliikmete nimed tuleb esilehele lisada enne ametlikku esitamist.

### 12.5 Kokkuvõte

Power BI aruanne **Liikumisaktiivsuse programmid** teeb avalikust API-st loetava seirevaate: 100 tegevust, tähemudel, neli analüüsilehte ja aus andmekvaliteedi vaade. Peamine sõnum juhtidele: **kava töötab asutuste ja struktuuride kihil; ühiskonna ja seireprotsendi kiht on veel auklik.** Järgmine otsus ei ole „kas Power BI töötab“, vaid kas tühjad meetmed ja tühjad edenemised on teadlik valik või seirevõlg.

---

## Lisad

### A. Aruande failid

- `Liikumisaktiivsuse programmid.pbip`
- `Liikumisaktiivsuse programmid.SemanticModel/` (TMDL)
- `Liikumisaktiivsuse programmid.Report/` (lehed, teema, järjehoidja)

### B. Allikad

- SA Liikumisharrastuse kompetentsikeskus, [Meist](https://liigume.ee/meist/), [Tegevuskava](https://liigume.ee/tegevuskava/)
- Avalik rakendus [app.liigume.ee](https://app.liigume.ee/) ja API `/api/activities`, `/api/organizations`, `/api/policies`
- WHO, *Global Action Plan on Physical Activity 2018–2030*
- Eesti spordipoliitika alusdokument Sport 2030; arengustrateegia Eesti 2035
- Avaliku teabe seadus; isikuandmete kaitse üldmäärus (EL) 2016/679
