# -*- coding: utf-8 -*-
"""Slaidid: avamine + seadusandlus andmetöö rollides + 1. paus."""

S1 = [
{
    "type": "title",
    "kicker": "ANDMETARKUS  ·  PÄEV 10",
    "title": "Andmekaitse andmetöös",
    "subtitle": "Kuidas rakendada seadusandlust, põhimõtteid, lõimitud kaitset\nja andmekaitsespetsialisti koostööd analüütiku, BI ja andmeinseneri laual.",
    "meta": "3-tunnine loeng  ·  Eesti õigusruum: IKÜM + IKS  ·  rollid: analüütik, BI, andmeinsener",
    "notes": (
        "[TRENERILE · 3 tundi · kogu jutt on notes’is]\n"
        "Ajakava: ava 12 min · seadusandlus andmetöös 38 · paus 10 · põhimõtted päringus/mudelis/aruandes 40 · "
        "paus 10 · lõimitud/vaikimisi disain 32 · DPO koostöö 28 · kokkuvõte 10. "
        "Kui arutelu venib, lühenda näiteid, mitte harjutusi. Esinejavaade: F5. See ei ole juriidiline nõu.\n\n"
        "Tere! Tere tulemast Andmetarkuse kursuse andmekaitse päevale.\n\n"
        "Minu nimi on [NIMI]. Täna ei ole eesmärk teha teist juriste. Eesmärk on, et te oskaksite andmekaitset "
        "rakendada selles töös, mida te sellel kursusel õpite: päring, andmete puhastus, mudel, aruanne, "
        "andmevoog, jagamine.\n\n"
        "Teist saavad või juba on andmeanalüütikud, BI-analüütikud, andmeinsenerid, aruandjad, keegi, kes "
        "„käib SQL-ist korra läbi“. Just teie käed puudutavad kõige rohkem ridu. Jurist kirjutab poliitika. "
        "Teie teete SELECT-i, liidate tabeleid, avaldate töölauda, tõmbate CSV-d, panete andmed järve või "
        "andmeaita. Seadus jõuab inimeseni teie töö kaudu.\n\n"
        "Neli teemat jäävad samaks: seadusandlus, põhimõtted, lõimitud ja vaikimisi andmekaitse, "
        "andmekaitsespetsialisti roll. Aga me räägime neid keeles, milles te tegelikult töötate: veerg, "
        "võti, liitmine, värskendus, õigused, väljavõte, testkeskkond.\n\n"
        "Ma ei anna täna juriidilist nõu teie asutuse konkreetse andmekogu kohta. Kui on päris juhtum, "
        "on koht Andmekaitse Inspektsioon, teie andmekaitsespetsialist või jurist. Täna ehitame harjumuse: "
        "enne „kuidas selle tabeli kätte saan“ küsida „kelle andmed need on ja miks ma neid vajan“.\n\n"
        "Lähme õpieesmärkide juurde."
    ),
},
{
    "type": "content",
    "kicker": "AVA  ·  12 minutit",
    "title": "Mida te täna oskate oma töölaua peal",
    "bullets": [
        "öelda, millal päring, mudel või aruanne sisaldab isikuandmeid",
        "eristada, kes on vastutav töötleja, kui teie värskendate andmestikku või avaldate raporti",
        "rakendada seitset põhimõtet SELECT-is, andmemudelis ja jagamises",
        "kavandada vaikimisi koond, rollipõhine vaade ja surev väljavõte",
        "teada, millal kutsuda andmekaitsespetsialist enne uue liitmise või avaldamise tegemist",
    ],
    "callout": "Andmetarkus ilma andmekaitseta on ohtlik osavus.",
    "notes": (
        "Vaadake neid viit rida. See on tänane leping.\n\n"
        "Esiteks: te ei küsi ainult „kas see on KPI“. Te küsite, kas selles faktitabelis, dimensioonis või "
        "allalaadimises on inimesi. Paljud lekked ei alga häkkerist, vaid aruandest, milles oli nimi, "
        "isikukood või kliendikood, ja link oli liiga avatud.\n\n"
        "Teiseks: teie ei ole automaatselt „vastutav töötleja“. Tavaliselt on seda asutus või ettevõte. "
        "Aga teie olete selle käed. Kui te avaldate Power BI tööalasse, kuhu pääseb kogu maja, olete teie "
        "teinud töötlemise otsuse kättesaadavuse kohta. Seda peab oskama nimetada.\n\n"
        "Kolmandaks: seitse põhimõtet ei ole poster seinal. Need on küsimused enne päringut: kas mul on "
        "alus, kas eesmärk on selge, kas ma võin SELECT * asemel võtta kuus veergu, kas väljavõte sureb.\n\n"
        "Neljandaks: lõimitud ja vaikimisi kaitse tähendab teie keeles mudeli disaini. Koond on vaikevaade. "
        "Rida-realt on erand. Testis ei ole toodangu isikukoode.\n\n"
        "Viiendaks: andmekaitsespetsialist ei ole pidur, kelle eest projekti peita. Ta on see, kellele te "
        "näitate andmevoo joonist enne, kui liidate kliendid, veebilogi ja palga.\n\n"
        "[KÜSI] Kes teist juba kirjutab päringuid, teeb Power BI-d, Exceli mudeleid või andmevooge? "
        "Tõstke käsi. — Täpselt. Täna räägime teie tööriistadest, mitte üldisest „ärge jagage paroole“ loengust."
    ),
},
{
    "type": "content",
    "title": "Tänane ajakava  ·  3 tundi",
    "bullets": [
        "0:00–0:12    Avamine: miks just andmetöötaja laual",
        "0:12–0:50    I  Seadusandlus teie päringus ja andmevoos",
        "0:50–1:00    Paus",
        "1:00–1:40    II  Seitse põhimõtet: SQL, mudel, aruanne, jagamine",
        "1:40–1:50    Paus",
        "1:50–2:22    III  Lõimitud ja vaikimisi kaitse andmeplatvormis",
        "2:22–2:50    IV  Kuidas analüütik DPO-ga koostööd teeb",
        "2:50–3:00    Kokkuvõte: esmaspäeva kontrollnimekiri",
    ],
    "spacing": 8,
    "size": 20,
    "notes": (
        "Kolm tundi, neli plokki, kaks pausi.\n\n"
        "Esimene plokk on seadus, aga mitte rida-realt. Me teeme kaardi: IKÜM, IKS, AKI — ja tõlgime need "
        "kohe teie töösse. Mis on isikuandmed dim_customeris. Mis on töötlemine, kui värskendus jookseb öösel. "
        "Kes on kes, kui andmed on lakehouse’is ja aruanne on teenuses.\n\n"
        "Teine plokk on põhimõtted. See on süda. Iga põhimõte saab näite: SELECT *, vale liitmine, vana CSV, "
        "avalik link, dokumenteerimata andmestik.\n\n"
        "Kolmas on disain: kuidas ehitada kaitse mudelisse ja vaikimisi õigustesse, mitte kleebisena lõppu.\n\n"
        "Neljas: millal teie rollis on DPO kohustuslik asutusele, ja kuidas teie teda kasutate — mitte kuidas "
        "temast saab jurist.\n\n"
        "Harjutused on andmetöö stsenaariumid. Palun olge pausidelt täpselt tagasi."
    ),
},
{
    "type": "content",
    "title": "Kolm rolli, sama seadus — erinev käsi",
    "bullets": [
        "andmeanalüütik: päring, ühendamine, väljavõte, järeldus inimese või segmendi kohta",
        "BI-analüütik: semantilne mudel, visuaal, tööala, allalaadimine, ridade turve",
        "andmeinsener: toru, järv, ait, õigused, test vs toodang, varukoopiad, logid",
        "seadus ei küsi ametinimetust — ta küsib, mida te andmetega teete",
        "kõik kolm saavad teha nii kaitse sisse kui ka vaikselt suure lekke",
    ],
    "notes": (
        "Andmetarkuse kursusel ei ole te ainult „üks amet“. Mõni teist jääb analüütikuks, mõni teeb "
        "juhtimisaruandeid, mõni ehitab torusid. Seadus ei tee vahet pealkirjal. Ta teeb vahet toimingul.\n\n"
        "Analüütik on see, kes küsib uue küsimuse ja läheb andmete kallale. Oht: liita kolm allikat, sest "
        "oskate, mitte sest tohib. Oht: tõmmata täispilt „et vaatan kodus“.\n\n"
        "BI-analüütik teeb selle nähtavaks. Oht: mudelis on veerud, mida visuaal ei näita, aga Exceli "
        "allalaadimine näitab. Oht: tööala on „kogu asutus“, sest nii on lihtsam. Oht: ekraanipilt koolitusse.\n\n"
        "Andmeinsener otsustab, kus andmed elavad ja kes neile ligi pääseb. Oht: toodangu koopia testis. "
        "Oht: varukoopia ilma samade õigusteta. Oht: logides on päringud koos isikukoodiga, ja logidele "
        "pääseb pool IT-st.\n\n"
        "Täna räägime kõigile kolmele. Kui näide on Power BI, tõlkige see oma tööriista. Kui näide on SQL, "
        "tõlkige DAX-i või Pythonisse. Põhimõte on sama.\n\n"
        "Kuldreegel ruumis: räägime põhimõtetest ja näidistabelitest, mitte kolleegi palgast ega päris "
        "kliendi isikukoodist."
    ),
},
{
    "type": "exercise",
    "badge": "SOOJENDUS",
    "time": "4 minutit  ·  käed üles, kogu rühm",
    "title": "Mida teie andmetöö juba teeb inimestega?",
    "bullets": [
        "päring või eksport, kus on nimi, e-post, kliendi- või töötaja ID",
        "Power BI / Excel / Looker, mida keegi teine saab avada või alla laadida",
        "kahe tabeli liitmine (klient + müük, töötaja + puudumine, logi + konto)",
        "andmete koopia: CSV, notebook, testkeskkond, isiklik OneDrive",
        "„vaatan korra, kas need klapivad“ ilma kirjaliku eesmärgita",
    ],
    "notes": (
        "[SOOJENDUS, umbes 4 minutit]\n\n"
        "Tõstke käsi, kui see kehtib teie töö või õpingute kohta viimase kuu jooksul.\n\n"
        "Esimene: olete teinud päringu või ekspordi, kus on inimese tunnus. — See on isikuandmete töötlemine. "
        "Mitte „ainult analüüs“.\n\n"
        "Teine: olete avaldanud või jaganud aruannet. — Kättesaadavus on artikli 25 vaikimisi küsimus. "
        "Kes näeb, on juba andmekaitseotsus.\n\n"
        "Kolmas: olete liitnud tabeleid. — Uus ühendamine võib olla uus eesmärk ja uus profiil. Seadus "
        "ei kiida automaatselt heaks seda, et teie oskate JOIN-i.\n\n"
        "Neljas: koopia. Analüütiku kõige tavalisem variandirisk. Ametlik baas võib olla turvaline; teie "
        "allalaadimiste kaust ei ole.\n\n"
        "Viies: uudishimu. „Vaatan, kas klapib.“ Ilma eesmärgita isikuandmete uudistamine on halb harjumus, "
        "mitte andmetarkus.\n\n"
        "Kui käsi käis mitu korda üles, olete täpselt õiges loengus. Andmekaitse ei ole HR-i teema kuskil "
        "kõrval. See on teie sprint, teie backlog, teie merge."
    ),
},
{
    "type": "quote",
    "title": "Teie ei küsi ainult „kas mudel töötab?“.\nTe küsite „kelle elu see rida on?“",
    "subtitle": "Iga päring, värskendus, liitmine ja allalaadimine on töötlemine.",
    "notes": (
        "See on tänase päeva põhisõnum.\n\n"
        "Andmetarkuse kursusel õpite te tegema asju, mis on võimsad: puhastada, ühendada, visualiseerida, "
        "automatiseerida. Võim ilma piirideta on oht. Rida andmebaasis ei ole „datapunkt“. Kui sealt saab "
        "inimese kätte, on see kellegi eraelu, palk, ost, tervis, asukoht või töötulemus.\n\n"
        "Seadus ei keela analüüsi. IKÜM ütleb ise, et isikuandmete kaitse ei ole absoluutne. Te võite ja "
        "peate andmeid kasutama otsuste jaoks. Aga te peate oskama öelda miks, millisel alusel, kui kitsalt, "
        "kui kaua, kes näeb, ja kuidas te seda hiljem tõendate.\n\n"
        "Kui te ühe harjumuse koju viite, siis see: enne kui kirjutate SELECT, kirjutate mõõdiku või "
        "avaldame töölauda, nimetage inimene, kelle rida see on — klient, töötaja, õpilane, patsient — "
        "ja nimetage otsus, mida see rida toetab. Kui te ei oska, ärge jookske päringut.\n\n"
        "Läheme seadusandluse juurde, kohe teie tööriistade keeles."
    ),
},
{
    "type": "section",
    "kicker": "OSA I  ·  umbes 38 minutit",
    "title": "Seadusandlus teie päringus ja andmevoos",
    "subtitle": "IKÜM  ·  IKS  ·  AKI  ·  tõlgitud: tabel, mudel, värskendus, tööala, väljavõte",
    "notes": (
        "Esimene plokk: mis reeglid Eestis kehtivad, ja mida need tähendavad, kui teie käsi on andmetel.\n\n"
        "Me ei loe paragrahve järjest. Me teeme kiire kaardi — põhiseadus, IKÜM, IKS, AKI — ja siis "
        "tõlgime iga mõiste andmetöö keelde. Pärast seda oskate te öelda, kas teie dim-tabel on isikuandmed, "
        "kas öine värskendus on töötlemine, ja kelle poole minna, kui link läks valeks.\n\n"
        "Alustame lühidalt õiguspildist, siis kohe näidetest, mis teie ekraanil tegelikult on."
    ),
},
{
    "type": "cards",
    "title": "Kolm nime, mis peavad teie sõnavaras olema",
    "cards": [
        ("IKÜM  ·  GDPR",
         "Määrus (EL) 2016/679. Kehtib otse alates 25.05.2018.\n\nKehtib teie päringule, mudelile ja aruandele, kui seal on isikuandmeid — ka siis, kui andmed on „ainult analüüsiks“."),
        ("IKS",
         "Isikuandmete kaitse seadus. Eesti täpsustused.\n\nMuuhulgas AKI pädevus, lapse nõusolek 13, erijuhud. Teie asutuse kohustused tulevad mõlemast."),
        ("AKI",
         "Andmekaitse Inspektsioon. Järelevalve, juhendid, kaebused, rikkumisteated.\n\nKui aruanne lekib või vale fail läheb välja, tiksub tihti 72 tundi nende suunas."),
    ],
    "notes": (
        "Kolm lühendit, siis liigume edasi — me ei jää ajalukku.\n\n"
        "IKÜM on Euroopa määrus. Määrus kehtib otse. Te ei saa öelda „meie Eesti firmas GDPR ei kehti, "
        "sest me teeme ainult sisemisi aruandeid“. Kui töötlete isikuandmeid, kehtib. Analüüs, BI, ETL "
        "ei ole erand.\n\n"
        "IKS on Eesti seadus, mis täidab kohad, mille Euroopa jätab riigile: kuidas AKI töötab, 13-aastase "
        "nõusolek infoühiskonna teenustes, ajakirjandus, teadusuuring, avaliku sektori erisused. "
        "Avalikus sektoris puutute kokku ka avaliku teabe seadusega: juht tahab aruannet avalikuks, teie "
        "näete, et tabelis on nimed. See pinge on just teie laual.\n\n"
        "AKI on järelevalve. Nende juhendid on praktilised. Esimene soovitus andmetöötajale: aki.ee on "
        "sõber. Teine: kui lekib, ärge vaadake kõrvale.\n\n"
        "Põhiseaduse § 26 — eraelu puutumatus — on vundament. Teie tabel on selle põhiõiguse praktiline "
        "koht. Õigus ei ole absoluutne: maks, ravi, statistika, leping võivad andmeid nõuda. Küsimus on "
        "kuidas, mitte kas andmed üldse tohivad eksisteerida."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 4 punkt 1  ·  teie tabelites",
    "title": "Isikuandmed ei ole ainult „nimi“ veerg",
    "bullets": [
        "otsene: nimi, isikukood, e-post, telefon, foto, hääl",
        "kaudne: customer_id, employee_id, seadme-ID, IP, küpsis, asukohalogi",
        "liitmine teeb tuvastatavaks: haruldane amet + vald; n=1 ruut aruandes",
        "pseudonüüm (klient_8821) on ikka isikuandmed, kui võti on olemas",
        "juriidilise isiku registrikood ei ole; juhatuse liige samas reas on",
    ],
    "notes": (
        "Isikuandmed on teave tuvastatud või tuvastatava inimese kohta. Andmetöös on see tähtis, sest teie "
        "tabelites on harva veerg nimega „isikuandmed“. Seal on võtmed.\n\n"
        "Customer_id teie CRM-is on isikuandmed, kui selle taga on inimene. Employee_nr palgamudelis samuti. "
        "IP veebilogis võib olla, eriti teenuseosutajale või kui logi liidetakse kontoga. Küpsise-ID, "
        "seadme sõrmejälg, asukohapunktid — kaudne tuvastamine.\n\n"
        "Eestis on liitmine eriti ohtlik, sest rahvastik on väike. Te eemaldate nime, jätate ameti ja valla — "
        "Kihnus on üks naisarst. Power BI ruudus n=1 on tuvastamine, mitte statistika.\n\n"
        "Kui te asendate nime koodiga ja tõlketabel on kõrval või lakehouse’is, on see pseudonüüm. IKÜM "
        "kehtib edasi. Anonüümne on ainult pöördumatu olukord, kus teie ega keegi teine mõistlike pingutustega "
        "inimest kätte ei saa. „Eemaldasime nime“ ei ole anonüümimine.\n\n"
        "OÜ registrikood ei ole isikuandmed. FIE on hallim. Töötaja nimi müügi edetabelis on isikuandmed — "
        "lubatud võib olla, aga see ei ole vaba tsoon.\n\n"
        "Teie tööküsimus enne mudeli koostamist: milliste veergude või kombinatsioonidega saab inimese kätte? "
        "Kahtluse korral kohtle isikuandmetena."
    ),
},
{
    "type": "content",
    "title": "Kus isikuandmed teie platvormil tegelikult elavad",
    "bullets": [
        "allikas: CRM, ERP, eKool, personal, logid, kliendikaart, piletisüsteem",
        "toru: staging, järv, ait, semantilne mudel — koopia on uus töötlemine",
        "tarbimine: aruanne, Excel, CSV, API, notebook, masinõppe tunnus",
        "vari: allalaadimised, e-posti manused, „lõplik_v3.xlsx“, isiklik ketas",
        "aeg: varukoopia 2018. aastast on ikka isikuandmed",
    ],
    "callout": "Kõige ohtlikum ei ole alati toodangu baas. See on teie varjufail.",
    "notes": (
        "Andmeinsenerid mõtlevad kihtides. Andmekaitse peab ka nii mõtlema.\n\n"
        "Allikas võib olla hästi hallatud: õigused, logid, leping. Siis teie toru kopeerib samad read "
        "stagingusse, Parquet’isse, mudelisse. Iga koopia on töötlemine. Iga kiht, kus õigused on laiemad "
        "kui allikas, on regressioon. Klassikaline viga: operatiivsüsteemis näeb kliendi aadressi kolm "
        "inimest; andmejärves näeb sada, sest „analüütikutel on vaja“.\n\n"
        "Tarbimiskiht on BI ja analüütiku kodu. Visuaal võib näidata tulpa; allalaadimine näitab ridu. "
        "Notebookis on täispilt, sest „mudel õpib paremini“.\n\n"
        "Vari on andmetarkuse tegelik epidemioloogia. Projekt sai otsa, CSV jäi Teams-kausta. Keegi saatis "
        "manuse. Keegi tõmbas koju, sest VPN oli aeglane. Need failid ei ole „mitteametlikud, seega seadus "
        "ei kehti“. Seadus kehtib. Need on lihtsalt halvemini kaitstud.\n\n"
        "Varukoopia: Apotheka loo üks õppetund oli, et vanad koopiad on ikka andmed. „See on arhiiv“ ei "
        "vähenda isikukoodi ohtu. Unustatud fail on kaitsmata fail.\n\n"
        "Kui te esmaspäeval ühe kaardi joonistate, joonistage: allikas → toru → mudel → aruanne → allalaadimine "
        "→ vari. Iga nool tahab peremeest, eesmärki ja õigusi."
    ),
},
{
    "type": "exercise",
    "time": "6 minutit  ·  paarides",
    "title": "Kas see artefakt on isikuandmed?",
    "bullets": [
        "1) dim_customer: CustomerKey, Email, BirthDate",
        "2) fact_sales koond: müük maakonna ja kuu kaupa",
        "3) fact_sales + müüja nimi visuaali teljel",
        "4) veebilogi: timestamp, IP, path — veel kontota",
        "5) HR-kuubik: puudumise põhjus + osakond, n=3",
        "6) „anonüümne“ küsitlus 12 vastajat, amet + vald",
        "7) testbaas: toodangu koopia, isikukoodid sees",
        "8) Power BI allalaadimine Excelisse „ainult vaatamiseks“",
    ],
    "notes": (
        "[HARJUTUS 6 min]\n\n"
        "Töötage paarides. Iga rea juurde: jah, ei või oleneb. Ärge avage veel vastuseid. Küsimus ei ole "
        "„kas meil on ilus KPI“, vaid „kas inimese saab kätte — otseselt või koos muu infoga, mis analüütikul "
        "tavaliselt on“.\n\n"
        "Kui jääte rea 4 (IP) või 6 (küsitlus) juurde kinni, on see hea — need on hallid. Märkige „oleneb“ "
        "ja kirjutage, millest oleneb.\n\n"
        "Pärast kuut minutit koguge kolm-neli rida valjusti, siis avage vastuste slaid. Ma ei oota täiuslikku "
        "skoori. Ma ootan, et te hakkaksite artefakti vaadates küsima tuvastatavuse, mitte veeru pealkirja järgi."
    ),
},
{
    "type": "content",
    "kicker": "HARJUTUSE VASTUSED",
    "title": "Artefaktid — lühike lahendus",
    "bullets": [
        "1 jah · 2 tavaliselt ei, kui üheski ruudus ei ole n=1",
        "3 jah — töötaja on tuvastatav; edetabel on isikuandmete töötlus",
        "4 oleneb; IP + muu info või hilisem liitmine kontoga = jah",
        "5 jah, ja võib olla eriliik (tervis), plus väike n",
        "6 sageli jah — Eesti väike, amet+vald pudelikael",
        "7 jah — test ei muuda andmeid mitteisikuteks",
        "8 jah — allalaadimine on uus koopia ja uus kättesaadavus",
    ],
    "size": 20,
    "notes": (
        "Kiiresti üle.\n\n"
        "Üks: jah. E-post ja sünniaeg on klassika; võti teeb ühendamise lihtsaks.\n\n"
        "Kaks: koond maakonna ja kuu kaupa on tavaliselt statistika. Aga Hiiumaa pluss üks tehing võib olla "
        "üks klient. Filtrid tapavad koondi.\n\n"
        "Kolm: müüja nimi teljel on töötaja isikuandmed. Võib olla õigustatud töösuhtes, aga vajab alust, "
        "kitsast ringi ja eesmärki. See ei ole „lihtsalt müügigraafik“.\n\n"
        "Neli: paljad logid on hall ala. Sideettevõttele on IP kliendi tunnus. Teie analüütikas, kui te "
        "liidete logi kontole, on see selge jah. Juba enne liitmist võib olla tuvastatav.\n\n"
        "Viis: puudumise põhjus on tihti tervis. Eriliik. Kolm inimest osakonnas — teate, kes on kes.\n\n"
        "Kuus: „anonüümne küsitlus“ on andmetarkuse sagedane enesepettus.\n\n"
        "Seitse: testkeskkond täiskoopiaga on toodangu risk laiema ligipääsuga. Inseneri teema.\n\n"
        "Kaheksa: „ainult vaatamiseks“ ei ole õiguslik kategooria. Fail, mis saab kettale, saab edasi minna.\n\n"
        "Kui teie paar vaidleks ridade 2, 4 või 6 üle, on see hea. Hall ala on teie tegelik töö."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 4 punkt 2",
    "title": "Töötlemine = teie tavaline tööpäev",
    "bullets": [
        "päring, sortimine, puhastus, imputeerimine, liitmine, agregatsioon",
        "andmevoo käivitus, mudeli värskendus, cache, import",
        "aruande avamine, jagamine, allalaadimine, ekraanipilt, saatmine",
        "säilitamine järves, varukoopias, versiooniajaloos, prügikastis",
        "kustutamine on ka töötlemine — ja peab päriselt ära kustutama",
    ],
    "notes": (
        "Inimesed ütlevad: „ma ei töötle, ma ainult vaatan / ainult hoian / ainult värskendan“. Seaduse "
        "keeles on töötlemine igasugune toiming.\n\n"
        "Teie tööpäev on töötlemise kataloog. SELECT on päring. Power Query samm on muutmine. Liitmine on "
        "ühendamine. Värskendus on kogumine ja salvestamine. Jagamine on edastamine. Versiooniajalugu on "
        "säilitamine. Kui te kustutate aruande, aga andmestik elab teenuses edasi, ei ole te kustutanud.\n\n"
        "See ei ole keelatud. See on nimetatav. Keelatud on töötlemine ilma aluseta ja põhimõtteid rikkudes.\n\n"
        "Praktiline järeldus: iga automatiseeritud toru on korduv töötlemine. Kui te panete ajastatud "
        "värskenduse, olete otsustanud, et see töötlus toimub iga öö. Keegi peab teadma, millisel eesmärgil "
        "ja millise tähtajaga.\n\n"
        "Teine järeldus: „ma tegin koopia, et kiiremini töötada“ on teadlik uus töötlus. Valige keskkond, "
        "mis on lepinguga kaetud, mitte isiklik Gmail ja USB."
    ),
},
{
    "type": "cards",
    "title": "Kes on kes, kui teie avaldate aruande",
    "cards": [
        ("Andmesubjekt",
         "Rida tabelis: klient, töötaja, õpilane, kasutaja.\n\nTema õigused kehtivad ka teie analüütika vastu."),
        ("Vastutav töötleja",
         "Asutus või ettevõte, kes otsustab miks ja kuidas.\n\nMitte teie isiklikult — aga teie otsused (keda lasta tööalasse) on tema nimel."),
        ("Volitatud töötleja",
         "Pilveteenus, Microsoft 365, lattuait, küsitluskeskkond, väline ETL.\n\nArt 28 leping peab olema. Ärge visake CSV-d esimesele tööriistale."),
        ("Teie",
         "Töötaja otseses alluvuses.\n\nTe ei ole „kolmas isik“. Te olete töötleja käsi. Hooletus jääb asutuse vastutuseks — ja teie tööjäljeks."),
    ],
    "notes": (
        "Rollid on andmeplatvormil kerged sassi minema, sest tehniliselt „andmed on Azures“.\n\n"
        "Vastutav töötleja on see, kes otsustab eesmärgi. Kool, haigla, e-pood, ministeerium. Serveri asukoht "
        "ei vabasta. „Meie Fabric on Iirimaal“ ei muuda kooli mittevastutavaks.\n\n"
        "Volitatud töötleja töötab teie asutuse nimel. Power BI teenus, Snowflake, palgafirm, küsitluskeskkond. "
        "Peab olema leping: mis andmeid, mis otstarve, allhankijad, kustutamine. Andmeinsener: ärge ühendage "
        "uut SaaS-i isikuandmetega enne, kui hanget ja lepingut on vaadatud. Analüütik: ärge kleepige "
        "isikuandmeid avalikku ChatGPT-sse — see võib olla edastamine volitamata töötlejale.\n\n"
        "Kaasvastutus tuleb ette, kui kaks asutust otsustavad koos, näiteks ühine haridusaruanne. Siis peab "
        "olema kokkulepe, kes mida teeb.\n\n"
        "[KÜSI] Kui teie avaldate aruande tööalasse „kogu ettevõte“: kes otsustas kättesaadavuse? Tavaliselt "
        "teie, asutuse nimel. See on täpselt see koht, kus analüütik teeb andmekaitseotsuse ilma seda "
        "märkamata."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 6  ·  analüütika alus",
    "title": "„Juht tahab dashboardi“ ei ole õiguslik alus",
    "bullets": [
        "leping: ainult andmed, ilma milleta teenust/töösuhet ei saa täita",
        "juriidiline kohustus: seadus nõuab aruannet (maks, tervisekassa, haridus)",
        "avalik ülesanne: asutus täidab seaduses antud ülesannet",
        "õigustatud huvi: sage eraettevõtte analüütikas — vajab kaalumist ja dokumenti",
        "nõusolek: harva hea alus sisemisele BI-le; peab olema vaba ja tagasivõetav",
        "uus liitmine / uus profiil = kontrolli, kas vana alus katab uue eesmärgi",
    ],
    "notes": (
        "See on seadusploki nurgakivi andmetöötajale.\n\n"
        "Iga isikuandmete töötlus vajab artikli 6 alust. „Juht käskis“, „nõnda on alati tehtud“, „meil on "
        "andmed juba olemas“ ei ole alused.\n\n"
        "Operatiivne töötlus — palga maksmine, paki saatmine, e-retsept — on sageli leping või seadus. "
        "Analüütika on tihti teine eesmärk. Kliendi aadress tarneks ei anna automaatselt luba teha temast "
        "turundusprofiili või käitumismudelit. Töötaja puudumise kanne palgaarvestuseks ei anna luba teha "
        "osakonna „tervise edetabelit“.\n\n"
        "Eraettevõttes on analüütika sagedane alus õigustatud huvi: mõistlik äriline vajadus, mis ei kaalu "
        "üle inimese õigusi. See nõuab kaalumist kirjas: mis kasu, mis oht, kas saaks koondiga, kas inimene "
        "võiks oodata. Inimesel on õigus esitada vastuväide. Avalikus sektoris on sagedamini avalik ülesanne "
        "või seadus — „meil on õigustatud huvi“ ei ole asutuse imevits.\n\n"
        "Nõusolekut ärge küsige, kui te tegelikult töötlete lepingu või seaduse tõttu. Ja ärge ehitage BI-d "
        "nõusoleku peale, kui töötaja ei saa tegelikult keelduda — see ei ole vaba.\n\n"
        "Teie tööreegel: enne uue veeru, uue allika või uue liitmise lisamist küsige, milline kuuest alusest "
        "selle katab. Kui ükski ei kata, ärge lisage. Kui katab, aga eesmärk on uus, rääkige DPO või juristiga."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 9  ·  teie kuubikus",
    "title": "Eriliik ei ole ainult „haigla andmebaas“",
    "bullets": [
        "tervis: diagnoos, ravim, apteegi ostuajalugu, haigusleht, erivajadus",
        "biomeetria: näotuvastus uksel, hääl, sõrmejälg — ka logides",
        "usk, ametiühing, poliitika, seksuaalelu — ärge koguge „igaks juhuks“",
        "vaba tekst (märkused, pileti sisu, vestlus) on eriliigi tagauks",
        "reegel on keeld; analüüs ainult tugeva erandi ja rangema turvega",
    ],
    "callout": "Kui näete tervist, puudumise põhjust või näotuvastust — peatuge.",
    "notes": (
        "Analüütikud arvavad, et eriliik on „meditsiinitöötajate teema“. Tegelikult tuleb see teie mudelisse "
        "külgukse kaudu.\n\n"
        "Apteegi ostuajalugu võib AKI käsitluses olla terviseandmed. Haiguslehe tunnus HR-kuubikus on tervis. "
        "Kooli „tugimeetme“ lipp võib olla erivajadus. Klienditeeninduse vaba tekst: „klient on rase, tarne "
        "ukse taha“. See üks veerg saastab kogu faktitabeli.\n\n"
        "Eriliigi töötlus on reeglina keelatud. Erandid on kitsad: ravi, seadus, selge nõusolek, oluline "
        "avalik huvi jne. „Juht tahab näha, kes haigestub kõige rohkem“ ei ole erand.\n\n"
        "Praktika teie rollides: ärge tooge eriliiki semantilisse mudelisse, mida kasutab turundus või "
        "kogu juhtkond. Eraldage. Maskeerige testis. Kui projekt on ulatuslik, on peaaegu kindlasti vaja "
        "mõjuhinnangut ja DPO-d.\n\n"
        "Süüteoandmed on artiklis 10. Ärge Google'ist „taustakontrolli“ ja pange see HR-analüüsi.\n\n"
        "Kui teie pipeline’i sisendis on vaba tekst, küsige, kas seal võib olla tervis või muu eriliik. "
        "Kui võib, on see disainiprobleem, mitte „hiljem filtrime“."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artiklid 12–22  ·  teie andmekaart",
    "title": "Inimene küsib oma andmeid — kas teie järv oskab vastata?",
    "bullets": [
        "juurdepääs: „mis andmeid te minust peate?“  ·  vastus üldjuhul 1 kuu",
        "parandamine ja kustutamine peavad jõudma koopiatesse, mitte ainult allikasse",
        "vastuväide otseturundusele / õigustatud huvile — mudel peab oskama välja jätta",
        "automatiseeritud otsus (skoor, keeld) — erireeglid, kui inimeseta",
        "kui teie ei tea, kus read elavad, ei suuda asutus õigust täita",
    ],
    "notes": (
        "Andmesubjekti õigused tunduvad „klienditoe teema“. Tegelikult on see andmeinseneri ja analüütiku "
        "kataloogiprobleem.\n\n"
        "Kui inimene küsib: mis andmeid te minust peate, peab asutus ühe kuu jooksul vastama. Keegi tuleb "
        "teie juurde: kus ta on? Kui vastus on „me ei tea, meil on kaksteist järve, kolm mudelit ja hunnik "
        "CSV-sid“, on vastutus põhimõte katki ja tähtaeg läheb.\n\n"
        "Parandamine allikas ei aita, kui teie ait hoiab vana dimensiooni ilma uuenduseta, või kui analüütiku "
        "väljavõte elab OneDrive’is. Kustutamine samuti: „õigus olla unustatud“ ei ole absoluutne — seadus "
        "võib säilitamist nõuda — aga kus te tohib kustutada, peab kustutus jõudma torusse, mudelisse ja "
        "varjudesse.\n\n"
        "Otseturunduse keeld peab olema tunnus, mida teie kampaaniaaruanne austab, mitte kiri, mida turundus "
        "unustab.\n\n"
        "Skoorid ja mudelid: kui laen või töökuulutus keelatakse ainult masinaga, on erireeglid. Andmetarkuse "
        "ajastul see ainult kasvab.\n\n"
        "Teie praktiline kohustus: andmestikel on omanik ja kirjeldus. Ilma andmekaardita ei ole õigusi "
        "võimalik täita. See on andmekaitse ja andmehaldus ühes."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM art 33–34  ·  teie tööala ja kaust",
    "title": "Leke andmetöös ei ole ainult häkkimine",
    "bullets": [
        "vale tööala, „kõik kellel on link“, vale e-posti aadress, printer, ekraanipilt",
        "kadunud sülearvuti, lunavara, vale RLS, testbaas avatud liiga laiale ringile",
        "kui oht inimesele: teavita AKI-t viivitamata, võimaluse korral 72 h teadasaamisest",
        "kõrge oht (tervis, isikukoodid, palgad) — teavita ka inimesi",
        "öelge kohe juhile ja DPO-le; ärge „parandage vaikselt“ üle nädalavahetuse",
    ],
    "notes": (
        "Andmetöötaja lekke tüüppilt ei ole Hollywood. See on: keegi avaldas aruande valesse tööalasse; "
        "keegi kopeeris palgafaili chatti; RLS ei töötanud filtriga; notebooki commit läks reposse; "
        "praktikant sai lingi „vaata, kui ilus“.\n\n"
        "Rikkumine on konfidentsiaalsuse, tervikluse või käideldavuse kadu. Vale inimene nägi. Andmeid "
        "muudeti. Lunavara lukustas.\n\n"
        "72 tundi algab teadasaamisest. Reede õhtul avastatud vale link ei oota esmaspäeva. Öelge kohe.\n\n"
        "Dokumenteerige ka need juhud, kus otsustate mitte teavitada — seadus nõuab rikkumiste registrit. "
        "„Tundus väike“ peab olema hinnang, mitte unustus.\n\n"
        "Volitatud töötleja (pilveteenus, väline insener) peab teid kiiresti teavitama — see kuulub lepingusse. "
        "Kui teie olete see väline, ärge oodake, kuni klient ise avastab."
    ),
},
{
    "type": "content",
    "kicker": "NÄIDE EESTIST  ·  AKI 2025, kohus 2026",
    "title": "Allium UPI / Apotheka — õppetunnid teie rollile",
    "bullets": [
        "üle 750 000 inimese; ostuajalugu kui võimalik terviseandmed",
        "vanad varukoopiad + nõrk hügieen (jagatud paroolid, nõrk logimine)",
        "AKI: muu hulgas art 5 konfidentsiaalsus, art 25 lõimitud/vaikimisi, art 32 turve",
        "3 mln € trahv; 2026 Harju maakohus jättis jõusse (vaidlus võib jätkuda)",
        "teie tõlge: unustatud koopia, eriliik, liiga laiad õigused, puuduv jälg",
    ],
    "notes": (
        "Ma toon ühe Eesti näite, et see ei jääks „Iirimaa ja Facebooki asjaks“.\n\n"
        "2024. aasta alguses lekkis Apotheka lojaalsusprogrammi andmeid üle 750 000 inimese kohta. Lisaks "
        "nimele ja isikukoodile ostuajalugu — ravimid, rasedustestid, kuulmis- ja nahatooted. AKI käsitles "
        "seda terviseandmetena. 2025 määrati Allium UPI-le 3 miljoni euro trahv; 2026 septembris jättis "
        "Harju maakohus trahvi jõusse. Ettevõte on rääkinud edasisest vaidlusest. Me ei ole kohtunikud. "
        "Me võtame avalikust järelevalvest õppetunni.\n\n"
        "Andmeinsener: varukoopiad on andmed; logimine ja rollid ei ole ilu. Jagatud administraatorikonto "
        "on täpselt see, mida teie platvormil ei tohi olla.\n\n"
        "Analüütik: ostuajalugu ei ole „lihtsalt faktitabel“. See võib olla eriliik. Ärge tõmmake täispilti "
        "sest „saab ilusa mudeli“.\n\n"
        "BI: kes pääseb, kes laeb alla, kas vanad andmestikud elavad teenuses edasi ilma peremeheta.\n\n"
        "See näide seob kogu tänase: seadus, konfidentsiaalsuse põhimõte, artikkel 25, vastutus. Tuleme "
        "tagasi.\n\n"
        "Enne pausi kokkuvõte."
    ),
},
{
    "type": "content",
    "kicker": "OSA I  ·  KOKKUVÕTE",
    "title": "Seadus teie laual, kuues lauses",
    "bullets": [
        "IKÜM kehtib otse ka „ainult analüüsile“; IKS täiendab; AKI valvab",
        "võti, logi, n=1 ja liitmine võivad olla isikuandmed",
        "päring, värskendus, jagamine, koopia, kustutus = töötlemine",
        "asutus on vastutav; teie olete käsi; pilv on tihti volitatud töötleja",
        "dashboardi soov vajab artikli 6 alust; eriliik on pidur",
        "kui te ei tea, kus read elavad, ei saa te õigusi ega 72 tundi pidada",
    ],
    "callout": "Pärast pausi: seitse põhimõtet kui SQL-i, mudeli ja jagamise kontrollnimekiri.",
    "notes": (
        "Esimene plokk kinni.\n\n"
        "Te ei pea paragrahve pähe. Te peate oskama oma artefakti kohta öelda: kas siin on inimene, mis "
        "toiming see on, kes vastutab, mis alus, kas on eriliik, kas me oskame inimesele vastata, mida "
        "teeme kui lekib.\n\n"
        "[KÜSI 2 min] Tüüpilised küsimused:\n"
        "— Kas töö e-post on isikuandmed? Jah.\n"
        "— Kas koond KPI on? Tavaliselt ei, kuni filter viib n=1-ni.\n"
        "— Kas surnud kliendi rida? IKÜM kaitseb elavaid; praktiliselt hoidke sama distsipliini ja küsige "
        "juristilt, kui on arhiiv.\n\n"
        "Paus kümme minutit. Tagasi [KELLAAEG]. Järgmine on kõige praktilisem: põhimõtted teie päringus."
    ),
},
{
    "type": "break",
    "title": "Paus  ·  10 minutit",
    "subtitle": "Järgmine: seitse põhimõtet SQL-is, mudelis, aruandes ja jagamises.",
    "notes": (
        "[PAUSE 10 min]\n\n"
        "Öelge kellaaeg tahvlile. Ärge laske pausil üle 12 minuti minna.\n\n"
        "Kui keegi küsib „kas meil tohib seda aruannet teha“, ärge andke asutuse-põhist juriidilist nõu. "
        "Öelge: pärast pausi tulevad seitse küsimust, millega saate ise esimese filtri teha; lõplikuks "
        "vastuseks on DPO või AKI.\n\n"
        "Alustage, kui enamus on ruumis. Üks lause: järgmine plokk on teie igapäevane kontrollnimekiri, "
        "mitte teooria."
    ),
},
]
