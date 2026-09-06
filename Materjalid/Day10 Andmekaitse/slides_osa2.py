# -*- coding: utf-8 -*-
"""Slaidid: põhimõtted andmetöös + 2. paus."""

S2 = [
{
    "type": "section",
    "kicker": "OSA II  ·  umbes 40 minutit",
    "title": "Andmekaitse põhimõtted teie töölaua peal",
    "subtitle": "IKÜM artikkel 5  ·  seitse küsimust enne päringut, mudelit, aruannet ja jagamist",
    "notes": (
        "Tere tagasi. Esimene pool oli kaart: seadus, isikuandmed, rollid, alus. Nüüd kompass.\n\n"
        "Artikkel 5 on lühike ja see on kogu andmekaitse süda. Me ei õpi seda posterina. Me õpime seda "
        "kui kontrollnimekirja, mille te käite läbi enne SELECT-i, enne uue mõõdiku lisamist, enne "
        "tööala õiguste klikki, enne CSV eksporti.\n\n"
        "Iga põhimõtte juures on analüütiku, BI ja inseneri näide. Siis harjutus nelja stsenaariumiga. "
        "See osa on see, mida te esmaspäeval päriselt kasutate."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 5",
    "title": "Seitse põhimõtet kui töökorraldus",
    "bullets": [
        "1  seaduslikkus, õiglus, läbipaistvus  —  kas alus ja aus eesmärk on olemas?",
        "2  eesmärgi piirang  —  kas see päring on sama otsuse jaoks?",
        "3  minimeerimine  —  kas SELECT * / kõik veerud mudelis on vaja?",
        "4  õigsus  —  kas liitmine tabab õiget inimest?",
        "5  säilitamise piirang  —  millal see väljavõte sureb?",
        "6  usaldusväärsus ja konfidentsiaalsus  —  kes näeb ja kes laeb alla?",
        "7  vastutus  —  kas suudan seda näidata, mitte ainult lubada?",
    ],
    "size": 18,
    "spacing": 8,
    "notes": (
        "Seitse, mitte kuus. Kuus esimest on kuidas töödelda. Seitsmes on suuda tõendada.\n\n"
        "Rütm, mis jääb meelde: seaduslikult. Ainult selleks otstarbeks. Nii vähe veerge kui võimalik. "
        "Õige inimene. Mitte igavesti. Õigete inimeste ees. Ja kirjas.\n\n"
        "Kui te unustate artiklinumbrid, jätke need seitse küsimust. Need mahuvad sprinti valmis-definitsiooni, "
        "pull requesti mallile või aruande avaldamise checklistile. See ei ole bürokraatia. See on sama distsipliin, "
        "mida te juba kasutate andmekvaliteedi jaoks — lihtsalt küsimus on „kelle rida“.\n\n"
        "Analüütik kuuleb neid enne päringut. BI-analüütik enne Publish. Andmeinsener enne, kui uus allikas "
        "torusse ühendatakse. Sama seadus, kolm nuppu.\n\n"
        "Võtame ükshaaval. Palun ärge pange veel sülearvutit tööle — see osa on see, mida te esmaspäeval kasutate."
    ),
},
{
    "type": "content",
    "title": "1. Seaduslikkus, õiglus, läbipaistvus",
    "bullets": [
        "alus artiklist 6 peab katma just selle analüüsi, mitte ainult allika olemasolu",
        "õiglus: ära tee varjatud profiili, ära kasuta kaameraandmeid kohvipausi mõõtmiseks",
        "läbipaistvus: inimene saaks aru, kui küsiks — ka sisemise aruande puhul",
        "andmetöös: ära peida veergu „igaks juhuks“; ära üllata juhti ega töötajat",
    ],
    "notes": (
        "Seaduslikkus viitab alusele, millest rääkisime. Kui kliendiandmed on lepingu jaoks, ei ole see "
        "automaatselt alus teha neist käitumisskoor kogu personalile vaatamiseks.\n\n"
        "Õiglus on see, mida tehniline inimene unustab. Te võite formaalselt midagi tohtida, aga teha "
        "ebausalt. Näide: logid on „turbe jaoks“, aga te mõõdate, kes kui kaua dokumenti luges, ja teete "
        "edetabeli. Näide: küsitlus „töökeskkond“, aga vastuseid kasutatakse koondamise otsuses.\n\n"
        "Läbipaistvus andmetöös: privaatsusteade peab katma analüütika, kui te teete midagi, mida inimene "
        "ei oska oodata. Sisemises BI-s tähendab see ka, et töötaja teab, millised töötulemuse aruanded "
        "juhil on — mitte et te ehitate varjatud jälgimist.\n\n"
        "[KÜSI] Kus teie töös sünnib analüüs, millest andmesubjekt ei teaks? Tihti: liidetud logid, "
        "HR-i „inimese 360“, kliendi skoor. Need on kohad, kus läbipaistvus ja alus tuleb enne koodi paika."
    ),
},
{
    "type": "content",
    "title": "2. Eesmärgi piirang — JOIN ei ole uus luba",
    "bullets": [
        "operatiivne allikas ≠ automaatne luba igaks analüüsiks",
        "uus küsimus, uus liitmine, uus sihtrühm = kontrolli eesmärk uuesti",
        "klassika: tarneandmed → turundusprofiil; haigusleht → „tervisekampaaniate“ nimekiri",
        "statistikaks ja arenduse testimiseks on omad reeglid — need ei ole „tee mis tahad“",
    ],
    "notes": (
        "Eesmärgi piirang on analüütiku kiusatuse vastane põhimõte.\n\n"
        "Te oskate liita. Seepärast tahab iga uus äriline küsimus uut JOIN-i. Seadus küsib: kas see on "
        "ikka seesama eesmärk, millega andmed koguti, või uus? Uus eesmärk vajab uut alust või selget "
        "ühilduvust. Ühilduvus ei ole „meil on huvi“.\n\n"
        "Näited teie laual. Kliendi tarneaadress on leping. Sama aadressi kasutamine, et arvutada "
        "„elustiili segment“ ja müüa kolmandale, on teine eesmärk. Töötaja puudumine palgaarvestuseks "
        "on seadus/leping. Sama rea viimine turundusele „tervisepakettideks“ on eesmärgi rikkumine ja "
        "sageli eriliik.\n\n"
        "Andmeinsener: ärge looge üht hiigeltabelit „kõik inimese kohta“, millest igaüks ammutab oma "
        "küsimuse. See arhitektuur on eesmärgi piirangu vaenlane. Eraldage domeenid: klienditeenindus, "
        "HR, tervis, turundus.\n\n"
        "BI: uus aruanne uuele publikule on uus kättesaadavus ja tihti uus eesmärk. „Paneme sama andmestiku "
        "ka müügile“ võib olla lubatud, võib mitte.\n\n"
        "Enne iga uut päringut: mis otsust see toetab? Kui ei oska vastata, ärge jookske isikuandmetel."
    ),
},
{
    "type": "content",
    "title": "3. Minimeerimine — SELECT * on andmekaitseotsus",
    "bullets": [
        "võtke veerud, mida mõõdik või visuaal tegelikult kasutab",
        "ärge tooge isikukoodi, täisaadressi, vaba teksti „igaks juhuks“ mudelisse",
        "eelistage koondit, valimit, vanuserühma, maakonda — mitte rida",
        "analüütikas: kas vaja 100% populatsiooni või piisab valimist?",
        "insener: ärge kopeerige kogu allikat järve, kui 12 välja piisab",
    ],
    "notes": (
        "Minimeerimine on teie lemmik, sest see on konkreetne ja parandab ka mudeli kiirust.\n\n"
        "SELECT * allikast, kuhu on aastate jooksul kogunenud 80 veergu, on „igaks juhuks kogumine“ "
        "toru kujul. AKI ütleb otse: igaks juhuks kogumine on ebaseaduslik. Andmeid, mida teil ei ole, "
        "ei saa lekkida — ja teie aruanne on ka kiirem.\n\n"
        "BI: ärge tooge semantilisse mudelisse veerge, mida ükski visuaal ei kasuta. Keegi laeb Excelisse "
        "ja saab isikukoodid kätte. Peida veerg ei ole minimeerimine, kui allalaadimine selle ikkagi annab.\n\n"
        "Analüütik: kas juht vajab nime või vanuserühma? Kas tarneks on vaja tänavat või piisab maakonnast "
        "logistikakaardil? Kas treeningandmeteks on vaja täispopulatsiooni?\n\n"
        "Vaba tekst on minimeerimise vaenlane number kaks. Märkused, pileti sisu, chat — sinna kirjutatakse "
        "tervis ja pere. Kui eesmärk ei nõua, ärge võtke.\n\n"
        "Isikukood on Eestis tulirelv. Ärge pange seda vaikeväljaks. Ühendamiseks kasutage sisemist võtit; "
        "isikukood jäägu kitsasse, logitud tsooni.\n\n"
        "Mini-arutelu järgmisel slaidil."
    ),
},
{
    "type": "exercise",
    "badge": "MINI-ARUTELU",
    "time": "4 minutit  ·  kogu rühm",
    "title": "Juht tahab: „kes on meie e-poe kliendid?“",
    "bullets": [
        "tabelis: nimi, isikukood, e-post, telefon, aadress, sugu, sünniaeg,",
        "viimane ost, summa, tarneviis, kliendikaardi nr, märkused (vaba tekst)",
        "millised veerud jäävad juhtimisaruandesse, millised koondiks, millised välja?",
        "kas „märkused“ võib saastada kogu mudeli eriliigiga?",
        "kellele rida-realt vaade üldse lubatud on?",
    ],
    "notes": (
        "[MINI-ARUTELU 4 min]\n\n"
        "Eesmärk on udune — see on osa õppetunnist. Suunake:\n"
        "— Paluge eesmärk täpsustada: vanus, maakond, kordusost, käive? Ilma selleta kogute liiga palju.\n"
        "— Isikukood juhtkonna aruandesse ei kuulu. Vanuserühm piisab.\n"
        "— Nimi ei ole vaja, kui küsimus on segment, mitte võlg.\n"
        "— Aadress → maakond, kui ei saadeta pakki sellest aruandest.\n"
        "— Märkused: jah, tagauks eriliigile. Ärge tooge BI-sse.\n"
        "— Rida-realt: näiteks võlgade tiim kitsa RLS-iga, mitte „kogu juhtkond“.\n\n"
        "Tänage. Õppetund: minimeerimine algab eesmärgi täpsustamisest, mitte veergude kustutamisest lõpus."
    ),
},
{
    "type": "content",
    "title": "4. Õigsus — vale JOIN on vale inimene",
    "bullets": [
        "mustad andmed rikuvad analüüsi; vale isikuandme rikub inimese elu",
        "nimepõhine liitmine Eestis on ohtlik — nimesid on vähe",
        "vale võlg, vale hinne, vale diagnoos, vale kordusostu skoor",
        "parandus allikas peab jõudma aita, mudelisse ja väljavõtetesse",
        "ärge avaldage „tõde“, kui ühenduse kindlus on 70%",
    ],
    "notes": (
        "Te teate juba, et praht sisse, praht välja. Seadus lisab: praht isikuandmetes on õigusrikkumine, "
        "mitte ainult kehv KPI.\n\n"
        "Eestis on nimepõhine liitmine eriti halb mõte. Mari Maasikaid on palju, Aivar Kivisid samuti. "
        "Kui te ühendate ilma stabiilse võtmeta, toodate valet inimest ja levitate seda aruandena. See on "
        "nii andmekvaliteet kui andmekaitse.\n\n"
        "Näited: vale võlg krediidimudelis, vale hinne õppearuanne, kaks klienti üheks kokku liidetud, "
        "surnud aadress, kuhu läheb kiri — see võib olla rikkumine.\n\n"
        "Insener: SCD ja värskenduse loogika. Kui inimene parandab e-posti, kui kiiresti teie dim muutub? "
        "Kui teie ait on nädal aega maas, elab vale kontakt aruandes.\n\n"
        "Analüütik: ärge siluge auke nii, et teete inimesest vale järelduse. Puuduv väärtus ei ole „0 ostu“ "
        "kui see on tegelikult „ei tea“.\n\n"
        "Kui ühendus on fuzzy, ärge esitage tulemust kui fakti juhtkonnale. See on õiglus ja õigsus koos."
    ),
},
{
    "type": "content",
    "title": "5. Säilitamine — väljavõttel peab olema surmakuupäev",
    "bullets": [
        "ametlikus baasis on tihti tähtaeg; teie CSV-l ei ole, kuni te selle panete",
        "värskendus, mis kirjutab otsa, vs ajalugu, mis kasvab igavesti",
        "versiooniajalugu, prügikast, snapshot, Time Travel, OneDrive — samuti säilitamine",
        "failinimesse kuupäev; kalendrisse kustutus; omanik kaustale",
        "„äkki läheb mudeli jaoks vaja“ ei ole tähtaeg",
    ],
    "notes": (
        "Ükski isikuandmete hulk ei tohi olla igavene. Andmetöös on tegelik probleem vari, mitte register.\n\n"
        "Allikas võib kustutada 7 aasta pärast. Teie 2019. aasta dump elab notebookis. Power BI andmestik, "
        "mida keegi ei julge kustutada. Delta Time Travel. Git LFS-is on CSV. See kõik on säilitamine.\n\n"
        "Insener: snapshot-poliitika on andmekaitseotsus. Kui te hoiate iga päeva täiskoopiat isikuandmetest "
        "kolm aastat, olete teadlikult valinud pika säilituse. Põhjendage või lühendage. Varukoopia peab "
        "saama ka kustutada, mitte ainult taastada.\n\n"
        "Analüütik: iga eksport on laps, kes ei oska ise surra. Pange failinimesse kuupäev. Pange Teams-kausta "
        "reegel. Ärge hoidke isikuandmetega dump’e portfoolios ega kodukettas.\n\n"
        "BI: vanad rakendused teenuses. Kord kvartalis: mis andmestikud on ilma omanikuta? See on säilitamise "
        "põhimõtte hügieen.\n\n"
        "Apotheka õppetund: vana ei ole ohutu. Vana on unustatud, unustatud on kaitsmata."
    ),
},
{
    "type": "content",
    "title": "6. Konfidentsiaalsus — kes näeb rida, kes laeb alla",
    "bullets": [
        "tööala, kaust, RLS, objektitaseme õigused — vaikimisi kitsas",
        "visuaal võib olla koond; allalaadimine on rida — kontrolli mõlemat",
        "ekraanipilt, jagatud ekraan, koolituse demo = samuti kättesaadavus",
        "testtoodang, jagatud parool, lai service principal = inseneri lekketee",
        "riskipõhine: palk ja tervis ei ela samas avatud kuubikus kui müügikoond",
    ],
    "notes": (
        "See on põhimõte, mille rikkumise eest Allium UPI muu hulgas trahvi sai: usaldusväärsus ja "
        "konfidentsiaalsus. Meetmed peavad vastama ohule.\n\n"
        "BI-analüütiku argipäev: Power BI tööala. „Kogu asutus“ on vaikimisi halb. Row-level security on "
        "lõimitud kaitse tööriist: piirkonnajuht näeb oma ridu, mitte kogu riiki. Aga RLS, mis ei kehti "
        "Exceli allalaadimisele või build-õigusele, on vale turvatunne. Testige allalaadimist.\n\n"
        "Analüütik: ärge pange palgafaili chatti. Ärge kasutage „kõik, kellel on link“. Enne jagamist "
        "vaadake, kes kaustas juba on — praktikant, väline, terve osakond.\n\n"
        "Insener: least privilege. Service principal ei pea lugema HR-tsooni. Logid ei pea sisaldama "
        "täispäringut isikukoodiga laiale admin-ringile. Testis maskeeritud andmed. Krüpteering, MFA, "
        "eraldi admin-kontod — Apotheka loo vastand.\n\n"
        "Koolitus ja demo: sünteetilised andmed. Kadreerige. See on konfidentsiaalsus, mitte ilu.\n\n"
        "Proportsioon: kohaloleku nimekiri ei nõua sama mis 750 000 terviserea. Aga ka väike nimekiri lekib."
    ),
},
{
    "type": "content",
    "title": "7. Vastutus — kui ei ole kirjas, ei ole olemas",
    "bullets": [
        "andmestiku omanik, eesmärk, alus, säilitus, kes näeb — üks leht",
        "töötlemistoimingute register ei ole juristi hobi; teie read peavad seal olema",
        "otsus „koond piisab“ / „isikukoodi ei võta“ kuulub PR-i või wiki, mitte pea sisse",
        "rikkumise hinnang kirjas ka siis, kui te ei teavita AKI-t",
        "„me oleme tublid“ ei ole tõendus",
    ],
    "callout": "Dokumenteerimata järv on andmekaitse mõttes pime järv.",
    "notes": (
        "Artikkel 5 lõige 2: vastutav töötleja peab suutma vastavust tõendada. Teie olete selle tõenduse "
        "tootjad.\n\n"
        "Kui AKI või DPO küsib: milliseid isikuandmeid see aruanne töötleb, peab olema vastus. Kui vastus "
        "on „vaatame koodist“, olete juba hiljaks jäänud.\n\n"
        "Praktiline miinimum igale andmestikule: omanik, allikad, eesmärk, õiguslik alus ühe lausega, "
        "kas on eriliik, säilitus, kes pääseb, kas allalaadimine on lubatud. See mahub README-sse või "
        "kataloogi. See on andmehaldus, mis on samal ajal andmekaitse.\n\n"
        "Insener: andmekataloog ja lineage ei ole luksus. Need on artikli 5 ja andmesubjekti õiguste eeldus.\n\n"
        "Analüütik: kui te otsustate veeru välja jätta, kirjutage see otsus. Muidu tuleb järgmine inimene "
        "ja lisab isikukoodi tagasi, sest „kuidas muidu ühendada“.\n\n"
        "Lause seinale: kui seda ei ole kirjas, ei ole seda andmekaitse mõttes olemas."
    ),
},
{
    "type": "content",
    "title": "Kontrollnimekiri enne „Run“ / „Publish“ / „Share“",
    "bullets": [
        "miks neid ridu vaja on?  (eesmärk + alus)",
        "kas saan vähemate veergude või koondiga?  (minimeerimine)",
        "kas liitmine tabab õiget inimest?  (õigsus)",
        "millal see koopia sureb?  (säilitamine)",
        "kes näeb visuaali ja kes saab Exceli?  (konfidentsiaalsus)",
        "kas inimene teaks, kui küsiks?  (läbipaistvus)",
        "kas omanik ja kirjeldus on kirjas?  (vastutus)",
    ],
    "notes": (
        "See on slaid, mille te pildistate. Seitse põhimõtet nupule vajutamise keeles.\n\n"
        "Run — analüütiku päring ja notebook. Publish — BI andmestik ja rakendus. Share — link, kaust, "
        "tööala, plus inseneri ACL järves. Kolm nuppu, sama nimekiri. Kolmkümmend sekundit enne klikki. "
        "See säästab nädalaid menetlust.\n\n"
        "Pange see pull requesti mallile, Power BI avaldamise juhisesse, analüütikatiimi wiki. Kui teie "
        "tiimis on juba andmekvaliteedi checklist, lisage need read sinna — ärge tehke eraldi „andmekaitse "
        "dokumenti, mida keegi ei ava“.\n\n"
        "Andmekaitse ebaõnnestub harva teadmise, sagedamini kiirustamise tõttu: sprinti lõpp, juht ootab, "
        "„panen lingi korra laiali“. Nimekiri on selle hetke jaoks.\n\n"
        "Järgmine: vead, mida just teie kolm rolli teevad — et ära tunda, mitte häbeneda."
    ),
},
{
    "type": "content",
    "title": "Levinud vead just analüütikas, BI-s ja torudes",
    "bullets": [
        "isikuandmetega fail „korraks“ koju, isiklikku e-posti, USB-le, avalikku GPT-sse",
        "filter aruandes peal, allalaadimises täisread",
        "ekraanipilt dashboardist nimedega — slakk, Confluence, koolitus",
        "väike n + haruldane tunnus = „anonüümne aruanne“",
        "test ja CI täistoote isikuandmetega, lai ligipääs",
        "omanikuta andmestikud, vanad pipeline’id, varjukaustad",
    ],
    "notes": (
        "Noogutage, kui olete näinud. Ilma häbita — et ära tunda.\n\n"
        "Esimene: kanal. Tööandmed kuuluvad lepinguga kaetud keskkonda. Avalik suurem keelemudel isikuandmetega "
        "on edastamine kuhugi, kuhu te ei tea.\n\n"
        "Teine: vale turvatunne visuaalist. Alati kontrollige, mida Export ja Analyze in Excel tegelikult annavad.\n\n"
        "Kolmas: ekraanipilt. Juhid ja koolitajad teevad seda. Kadreerige või kasutage demot.\n\n"
        "Neljas: n=1. Eestis tihti. Peitke või ühendage rühmad. Statistikaamet oskab; teie aruanne peab ka.\n\n"
        "Viies: test. „Sünteetika ei käitu õigesti“ — siis maskeerige, ärge avage haigla toodangut kogu IT-le.\n\n"
        "Kuues: peremeheta vara. Pipeline, mida keegi ei julge kinni panna. See on säilitamine ja vastutus.\n\n"
        "Esmaspäeva tegu: leidke üks CSV või üks liiga avatud andmestik."
    ),
},
{
    "type": "exercise",
    "time": "8 minutit  ·  4 gruppi",
    "title": "Milline põhimõte on hädas?",
    "bullets": [
        "A  Turundus võtab HR haiguslehtede väljavõtte, et sihtida „tervisepakette“.",
        "B  Analüütik hoiab 2018 klienddump’i sülearvutis, „sest mudel õpib paremini“.",
        "C  Palgaaruanne nimega; link „kõik kellel on link“, sh praktikant.",
        "D  Andmevoog teeb SELECT * allikast järve; mudelis on 4 KPI-d.",
    ],
    "notes": (
        "[HARJUTUS 8 min]\n\n"
        "Neli gruppi, üks lugu. Millised põhimõtted? Mis oleks õige tegu? 3 min arutelu, 60 s tagasiside.\n\n"
        "A: eesmärgi piirang + eriliik + seaduslikkus. Õige: ära tee. Vabatahtlik registreerumine, mitte "
        "haiguslehtede nimekiri.\n\n"
        "B: säilitamine + minimeerimine + konfidentsiaalsus. Õige: sünteetika või kitsas minimeeritud komplekt "
        "asutuse keskkonnas, krüptitud masin, tähtaeg.\n\n"
        "C: konfidentsiaalsus + minimeerimine. Õige: koond, rollipõhine ligipääs, mitte avalik link. "
        "Praktikant ei ole „kõik töötajad“.\n\n"
        "D: minimeerimine + lõimitud kaitse (järgmine plokk). Õige: võta järve need väljad, mida eesmärk "
        "vajab; ärge peegelda kogu allikat sest „toru on lihtsam“.\n\n"
        "Tihti on rikutud mitu põhimõtet. Nad on seotud."
    ),
},
{
    "type": "content",
    "kicker": "HARJUTUSE LÜHIKE KINNITUS",
    "title": "Neli pidurit teie tööriistades",
    "bullets": [
        "A  ära vii ridu ühest domeenist teise, eriti tervist",
        "B  vana dump sülearvutis ei ole treeningandmestik, see on risk",
        "C  palk + avatud link on õiguste viga, mitte visualiseerimise viga",
        "D  SELECT * torusse on minimeerimise vastand, isegi kui KPI-sid on neli",
    ],
    "notes": (
        "Kõik kuulsid sama järeldust, ka kui arutasite teist lugu. See on taotluslik: päriselus on rikkumine "
        "harva „üks paragrahv“. Haigusleht turundusse on korraga vale eesmärk, eriliik ja aluse puudumine. "
        "Avatud palgalink on konfidentsiaalsus ja minimeerimine. SELECT * on minimeerimine ja lõimitud kaitse.\n\n"
        "[KÜSI] Kas keegi nägi oma töös sarnast, üldistatult, ilma asutuse ja inimeste nimedeta? Üks-kaks "
        "lauset. Kui mitte, liikuge edasi.\n\n"
        "Järgmine täpsustus, mida algajad otsivad: kas piisab õiguslikust alusest või piisab „meil on RLS“. "
        "Vastus: kumbki üksi ei piisa."
    ),
},
{
    "type": "content",
    "title": "Alus avab ukse; põhimõtted ütlevad, kuidas toas käituda",
    "bullets": [
        "leping / seadus / huvi üksi ei luba SELECT * ega igavest ajalugu",
        "ilma aluseta on ka „ilus ja turvaline“ mudel ebaseaduslik",
        "näide: tarneandmed on leping — ei ole luba müüa profiili edasi",
        "näide: õigustatud huvi on kirjas — aga n=1 ruut ja avatud link rikuvad ikkagi",
    ],
    "notes": (
        "Algajad otsivad üht linnukest. Andmekaitse on ja: alus ja põhimõtted.\n\n"
        "Teil võib olla seaduslik alus palga maksmiseks. See ei luba palgaedetabelit kogu majale. Teil "
        "võib olla õigustatud huvi müügianalüüsiks. See ei luba hoida 2014. aasta täisdump’i sülearvutis.\n\n"
        "Vastupidi: te võite teha ilusa RLS-i ja ikkagi puudub alus uueks profiilianalüüsiks.\n\n"
        "Üks lause: alus avab ukse, põhimõtted ütlevad, kuidas toas käituda. Andmetöös: alus ütleb kas "
        "üldse joosta; põhimõtted ütlevad millised veerud, kellele, kui kaua, kui täpselt, kui tõendatult."
    ),
},
{
    "type": "cards",
    "title": "Analüütika kolm astet: ärge nimetage valet",
    "cards": [
        ("Koond",
         "Rühmad, keskmised, vahemikud.\n\nKontrolli n=1 ja haruldast tunnust.\n\nEestis: amet + vald on oht.\n\nTihti piisab juhtimisest."),
        ("Pseudonüüm",
         "Võti eraldi, analüüs koodidega.\n\nIKÜM kehtib edasi.\n\nHea vaikimisi analüütikakihis.\n\nÄrge jätke tõlketabelit samasse notebooki."),
        ("Täisidentiteet",
         "Nimi, isikukood, kontakt.\n\nAinult kui eesmärk ja roll seda nõuavad.\n\nLogi, kes vaatas.\n\nÄrge tehke sellest järve vaikevormingut."),
    ],
    "notes": (
        "Kolm astet, mida aetakse sassi sõnaga „anonüümne“.\n\n"
        "Koond on juhtimise sõber. Aga filter tapab. Peitke väiksed ruudud.\n\n"
        "Pseudonüüm on analüütika vaikehea. Insener hoiab võtit eraldi tsoonis. Analüütik ei pea nime "
        "nägema, et mudeldada ostukäitumist. Aga te ei tohi öelda, et IKÜM ei kehti.\n\n"
        "Täisidentiteet on operatiivne: võlg, tarne, palga maksmine, andmesubjekti päring. See ei ole "
        "BI vaikevaade.\n\n"
        "Pöördumatu anonümiseerimine on raske, eriti Eestis. Ärge lubage seda kergelt. Kui saate inimese "
        "tagasi, ei ole anonüümne.\n\n"
        "Masinõpe: treeningandmed on tavaliselt isikuandmed. Kehtib kõik täna õpitu.\n\n"
        "Teise osa kokkuvõte ja paus."
    ),
},
{
    "type": "content",
    "kicker": "OSA II  ·  KOKKUVÕTE",
    "title": "Kompass, mis jääb kätte",
    "bullets": [
        "seitse küsimust enne Run / Publish / Share",
        "JOIN, SELECT *, vana CSV, avatud link, n=1 on teie tegelikud riskid",
        "alus ja põhimõtted koos; koond → pseudonüüm → identiteet ainult vajadusel",
        "kirjutage otsus üles — muidu tuleb järgmine analüütik ja lisab veeru tagasi",
    ],
    "callout": "Pärast pausi: kuidas ehitada see kaitse mudelisse ja vaikimisi õigustesse.",
    "notes": (
        "Teine plokk kinni. Kui unustate paragrahvid, jätke seitse küsimust nupu peale.\n\n"
        "[KÜSI] Üks küsimus. Muidu paus 10 min, tagasi [KELLAAEG].\n\n"
        "Järgmine: seadus ei taha, et te lõpus küsiksite, kas valmis aruanne on okei. Ta tahab, et te "
        "kavandaksite koondi, RLS-i, maskeerimise ja kustutamise juba siis, kui te mudelit ja toru joonistate."
    ),
},
{
    "type": "break",
    "title": "Paus  ·  10 minutit",
    "subtitle": "Järgmine: lõimitud ja vaikimisi andmekaitse andmeplatvormis.",
    "notes": (
        "[PAUSE 10 min]\n\n"
        "Viimane paus. Pärast seda kaks plokki järjest: platvormi disain (32 min) ja DPO koostöö (28 min), "
        "siis kokkuvõte.\n\n"
        "Kui keegi küsib pausil „kas meil on DPO-d vaja“, öelge: see tuleb neljandas plokis; enne selleks "
        "õpime, mida teie saate disainis ise ära teha.\n\n"
        "Alustage, kui enamus on ruumis."
    ),
},
]
