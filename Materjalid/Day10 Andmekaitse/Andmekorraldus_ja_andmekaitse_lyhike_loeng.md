# Andmekorraldus ja andmekaitse andmetarkuses

**Lühike loeng + kaks harjutust**  
Kestus: umbes 45–60 minutit (jutt ~20 min, harjutused ~30 min)  
Tööriistad: töö dokumentatsioon *Liikumisaktiivsuse programmid* ja sama Power BI aruanne (`.pbip`)  
Sihtrühm: Andmetarkuse algajad (analüütik, BI, andmeinsener)

Kogu alljärgnev on **räägitav tekst**. Sulge sulgudes on treeneri märkused.

---

## 1. Kaks asja, mida ei tohi segi ajada (4 min)

Täna on kaks sõna, mis kõlavad sarnased, aga teevad teie laual erinevat tööd.

**Andmekorraldus** on kord andmete ümber. See vastab küsimustele: mis see veerg tähendab, kust ta tuleb, kui hea ta on, kes on omanik, kes tohib aruannet näha. Ilma korralduseta on teil küll Power BI, aga ei ole usaldust. Keegi ei tea, kas „edenemine 78%“ käib 28 rea või 100 rea kohta.

**Andmekaitse** on reeglid siis, kui andmed puudutavad **inimest**. Nimi, e-post, isikukood, kliendi-ID, IP, foto. Siis kehtib Eestis IKÜM ehk GDPR ja isikuandmete kaitse seadus. Siis ei ole küsimus ainult „kas KPI on õige“, vaid „kas meil on alus, kas me võtame liiga palju veerge, kes näeb rida“.

Andmetarkuse koolitusel õpite te päringut, mudelit ja visuaali. Need kaks teemat on sellepärast siin, et teie käsi on andmetel. Jurist kirjutab poliitika. Teie vajutate Refresh, Publish ja Share.

Üks lause, mille võite seinale panna:

> Andmekorraldus teeb andmed kasutatavaks. Andmekaitse teeb kasutamise lubatavaks, kui mängus on inimene.

Tähtis nüanss, mida meie kursuse näide hästi näitab. **Korraldust on vaja ka siis, kui isikuandmeid ei ole.** Avalik asutuste nimekiri, tegevuskava, müügikoond — ikka on vaja omanikku, sõnastikku, allikat ja kvaliteeti. Kaitse tuleb otsa, kui ridu saab inimesega kokku viia.

(Küsige käsi: kes on juba kirjutanud töö dokumentatsiooni peatükke 1–6? Täna me ei alusta tühjalt — me loeme omaenda korda.)

---

## 2. Viis küsimust enne aruannet (6 min)

Te ei pea pähe õppima seadust. Te peate enne Run / Publish / Share küsima viis asja. Need on korralduse ja kaitse ühine kontrollnimekiri.

1. **Miks?** Mis otsust see aruanne toetab? „Juht tahab dashboardi“ ei ole veel vastus. „Kas kava 100 tegevust on töös või auklikud“ on vastus. See on eesmärk. Andmekaitses sama: ilma eesmärgita ei tohi isikuandmeid koguda.
2. **Kust?** Allikas, voog, värskendus. API, Excel, CRM, käsitsi koopia. Iga koopia on uus koht, kus andmed elavad. Andmekaitses: iga koopia on töötlemine.
3. **Mida see veerg tähendab?** Ärisõnastik. Kui „partnerluste arv“ on summa, mitte unikaalsed asutused, ja te ei ütle seda, valetab visuaal. Korraldus on täpne keel. Kaitse vajab sama keelt: kas `customer_id` on inimene või ettevõte.
4. **Kui hea?** Tühjad kuupäevad, 72 rida ilma edenemiseta. Aus aruanne näitab auke, mitte ei täida nulliga. Andmekaitses on see õigsuse põhimõte: vale rida võib inimesele kahju teha.
5. **Kes näeb — ja kas siin on inimene?** Tööala, allalaadimine, ekraanipilt. Kui on inimene, siis veel: kas meil on alus, kas veerud on minimaalsed, kas rida-realt on vaja või piisab koondist.

Teie töö dokumentatsioon on just nende viie küsimuse kirjapanek. Peatükk 1 on miks. Peatükk 3 on mida tähendab. Peatükk 4 on kas inimene. Peatükid 5–6 on kus elab. Peatükk 8 on kui hea.

Kui seda ei ole kirjas, ei ole seda andmekorralduse mõttes olemas. Ja kui on isikuandmed, ei ole seda ka andmekaitse mõttes olemas.

---

## 3. Kaitse teie töölaua peal, lühidalt (5 min)

Kui andmestikus **on** isikuandmed, jätke meelde kolm pidurit. Täna ei ole 3-tunnine õigusloeng; need kolm piisavad, et te ei teeks kõige tavalisemat viga.

**Pidur 1 — ära võta liiga palju.** `SELECT *` ja „igaks juhuks isikukood mudelisse“ on korralduse ja kaitse ühine viga. Võtke veerud, mida visuaal tegelikult kasutab.

**Pidur 2 — koond enne rida.** Juhtimisvaade on tavaliselt maakond, staatus, kuu. Nimi ja e-post on erand, mitte vaikevaade. Power BI-s: mida visuaal näitab ja mida Exceli allalaadimine annab, võivad olla kaks eri asja. Kontrollige mõlemat.

**Pidur 3 — ära jaga laialt.** „Kõik, kellel on link“ ja tööala „kogu asutus“ on üks klikk. See klikk on andmekaitseotsus. Ka avalike andmete puhul küsige: kas me avaldame Service’isse ja kellele.

Eestis kehtib IKÜM otse. Järelevalvaja on Andmekaitse Inspektsioon. Teie ei ole tavaliselt vastutav töötleja — seda on asutus —, aga teie olete käsi, mis teeb päringu ja avaldab aruande.

Kui te ei ole kindlad, kas rida on isikuandmed, kohtlege seda isikuandmetena ja küsige järele. Hall ala on ohtlikum kui selge jah.

---

## 4. Power BI on korralduse ja kaitse masin (4 min)

Power BI ei ole „ainult visuaalid“. Iga valik seal on korraldus või kaitse.

- **Mudeli veerud.** Mis on peidus, mis on tarbijale näha. Tehniline võti võib olla peidus — hea korraldus. Isikukood, mis on peidus, aga tuleb Exportiga välja — halb kaitse.
- **Mõõdikud explitsiitselt.** Teie kokkulepe: ei implitsiitset summat. See on korraldus: arvutusreegel on kirjas, mitte hiireõnnetus.
- **Andmekvaliteedi KPI-d.** Aus auk on parem vale keskmisest. See on korraldus ja õigsus.
- **Info-leht / kataloog mudelis.** Mudel räägib ise, mis tabelid ja mõõdikud on. See on korraldus aruande sees, mitte ainult Wordis.
- **Tööala ja Publish.** Kes näeb, kes saab alla laadida. See on kaitse kättesaadavus.
- **Refresh.** Iga värskendus on uus töötlemine. Allikas peab olema see, mis dokumendis kirjas.

Kursuse näide *Liikumisaktiivsuse programmid* on hea just sellepärast, et isikuandmeid seal ei ole. Te saate harjutada korda ilma inimese andmeid riskeerimata. Siis küsime: mis muutuks, kui samasugusesse aruandesse tuleks inimeste e-post.

(Siit harjutused. Ärge lühendage harjutusi, kui aeg on kitsas — lühendage juttu.)

---

## Harjutus 1 · Töö dokumentatsioon (15 min)

**Fail:** `Liikumisaktiivsuse_programmid_too_dokumentatsioon.md`  
**Tööviis:** paarides. Kirjutage lühikesed vastused (mitte essee).

Avage dokument. Ärge lugege kõike — otsige vastuseid.

1. **Omanik ja teie roll.** Kes on andmestiku omanik / teabevaldaja (ptk 1 ja 4)? Kes olete teie selles ahelas — vastutav töötleja, volitatud töötleja või kasutaja? Miks see vahe on oluline?
2. **Eesmärk.** Ühe lausega: mis uurimisprobleemi aruanne lahendab? Kas see eesmärk on piisavalt konkreetne, et teaksite, milliseid veerge *mitte* importida?
3. **Ärisõnastik.** Valige kaks mõistet peatükist 3, mille vale tähendus rikuks KPI-d (vihje: edenemine %, partnerluste arv, poliitikameetmete arv). Öelge, mis läheks valesti.
4. **Andmekaitse peatükk.** Kas selles töös on isikuandmete töötlemine? Mis alusel see järeldus tehti? Mis **muutuks peatükis 4**, kui API-s oleks iga tegevuse juures kontaktisiku nimi, e-post ja telefon?
5. **Minikaart.** Täitke kuus lahtrit oma sõnadega, dokumendist:

| Väli | Teie vastus |
|---|---|
| Omanik | |
| Eesmärk | |
| Allikas | |
| Kus koopia elab | |
| Kas isikuandmed? | |
| Mida me teadlikult *ei* teinud | |

**Arutelu (3 min, kogu rühm).** Koguge kaks asja: (a) kas keegi arvas, et asutuse nimi on isikuandmed; (b) mida paarid kirjutasid küsimusse 4 — mis muutuks. Treeneri suund: asutuse nimi ei ole isikuandmed; kontaktisiku nimi oleks. Siis oleks vaja alust, minimeerimist, võib-olla peidetud veerge ja kitsamat jagamist. Korralduse ülejäänud peatükid jääksid ikka vajalikuks.

---

## Harjutus 2 · Sama töö Power BI-s (15 min)

**Fail:** `Liikumisaktiivsuse programmid.pbip`  
Avage Desktopis. Kui aruanne ei avane, tehke harjutus 2B paberil / dokumendi ptk 5, 6, 8 ja 11.7 järgi.

### 2A · Mudel ja Info (kui PBIP avaneb)

1. **Mudeli vaade.** Nimetage fakt ja kolm dimensiooni. Miks on `activity_id` ja `lead_org_id` peidetud? Kas peitmine on korraldus, kaitse või mõlemad?
2. **Leht Info.** Mis kasu on sellest, et mudel dokumenteerib end ise (`INFO.VIEW`)? Kellele see leht on — juht või andmetöötaja?
3. **Leht Edenemine.** Leidke mõõdikud puuduva edenemise, puuduva kuupäeva ja tähtaja kohta. Miks on aus näidata 72 tühja rida, mitte „keskmine kogu kava peale“? Seostage see dokumentatsiooni hoiatusega (ptk 8 ja 10.2).
4. **Mõõdiku lõks.** Leidke visuaal või KPI, mis räägib *partnerlustest* või *poliitikameetmete arvust*. Kas see on unikaalsed asutused/meetmed või ridade summa? Kas aruande pealkiri ütleb selle kasutajale?

### 2B · Publish ja „mis siis, kui“ (kõik teevad, ka kui mudel ei avane)

Kujutage kaks olukorda. Kirjutage igaühe kohta kolm klikki või reeglit, mis te **muudaksite**.

**Olukord A — praegune aruanne (avalik kava, asutused, ei isikuandmeid).**  
Te avaldate Power BI Service’isse. Mida ütleb dokumentatsioon säilitamise ja avaldamise kohta (ptk 4.4)? Kellele te tööala annaksite: ainult rühm, kogu kool, avalik link? Kas Export Excelisse on vaja?

**Olukord B — sama aruanne, aga külge on liidetud inimeste tabel:** tegevuse kontaktisiku nimi, isiklik e-post, telefon.  
Mis muutub: veerud mudelis, vaikevaade (koond vs rida), RLS, Export, ekraanipilt koolitusse, kas Info-lehel peab olema kirjas „siin on isikuandmed“, kas peatükk 4 tuleb ümber kirjutada?

**Arutelu (3 min).** Treeneri suund olukorrale A: avalik teave ei tähenda, et *teie koopia* peab olema avalik link kogu internetile; dokument hoiatab Service’i eest. Olukord B: peitke või ärge tooge isikuveerge juhtimisvaatesse; koond staatuse järgi jääb; Export kinni või eraldi koond-andmestik; ekraanipilt ilma nimedeta; dokumentatsiooni ptk 4 muutub „jah, isikuandmed, alus, minimeerimine“.

---

## Lõpetus (2 min)

Kui te täna kaks asja meelde jätate, siis need.

Esiteks: **dokumentatsioon ei ole kodutöö pärast aruannet.** See on kord, ilma milleta te ei tea, mida te mõõdate. Viis küsimust — miks, kust, mida tähendab, kui hea, kes näeb — on andmekorraldus.

Teiseks: **kui ridu saab inimesega kokku viia, tuleb pidur.** Vähem veerge, koond enne rida, kitsas jagamine. Power BI-s on need klikid, mitte poster seinal.

Esmaspäeva 15 minutit: võtke *üks* oma andmestik või aruanne ja täitke sama minikaart mis harjutuses 1. Kui te ei oska öelda, kas on isikuandmed, on see juba leid.

Allikad, kui tarvis: teie töö dokumentatsioon; aki.ee; IKÜM; isikuandmete kaitse seadus. See lühiloeng ei ole juriidiline nõu.

---

## Treenerile: ajakava

| Aeg | Mis |
|---|---|
| 0:00–0:04 | Kaks mõistet |
| 0:04–0:10 | Viis küsimust |
| 0:10–0:15 | Kolm pidurit |
| 0:15–0:19 | Power BI kui masin |
| 0:19–0:34 | Harjutus 1 (dokument) + arutelu |
| 0:34–0:52 | Harjutus 2 (Power BI) + arutelu |
| 0:52–0:55 | Lõpetus |

Kui ainult 30 minutit: jätke jutu osast pidurid lühikeseks ja tehke harjutus 1 täielikult plus olukord B harjutusest 2.
