# -*- coding: utf-8 -*-
"""Slaidid: lõimitud/vaikimisi platvormis, DPO koostöö, kokkuvõte."""

S3 = [
{
    "type": "section",
    "kicker": "OSA III  ·  umbes 32 minutit",
    "title": "Lõimitud ja vaikimisi kaitse andmeplatvormis",
    "subtitle": "IKÜM artikkel 25  ·  mudel, toru, tööala ja vaikevaade — mitte kleebis lõpus",
    "notes": (
        "Kolmas teema. See on koht, kus seadus kohtub teie backlogiga.\n\n"
        "Lõimitud andmekaitse tähendab: kaitse on arhitektuur. Te mõtlete sellele, kui valite allikaid, "
        "kujundate skeemi, otsustate, mis läheb järve, mis jääb koondiks, kuidas testida.\n\n"
        "Vaikimisi andmekaitse tähendab: kui keegi ei klõpsa ekstra, on ohutum valik peal. Koond, suletud "
        "tööala, tühjad linnukesed, lühike säilitus, privaatne profiil.\n\n"
        "Artikkel 25 oli ka Apotheka menetluses laual koos turbe artikliga 32. See ei ole iluidee. "
        "Inseneri ja BI-arhitekti kohustus, mida analüütik iga aruandega kas toetab või lõhub.\n\n"
        "Lihtne seletus, siis teie töönäited, mõjuhinnang, ja harjutus: parandage halb platvorm."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 25",
    "title": "Artikkel 25 kahe lausega teie keeles",
    "bullets": [
        "lõimitud: juba toru ja mudelit kavandades pane kaitsemeetmed sisse",
        "vaikimisi: töötle ainult eesmärgiks vajalikku — hulk, ulatus, aeg, kättesaadavus",
        "vaikimisi ei ole „kogu maja näeb ridu“ ega „kõik kellel on link“",
        "seadus arvestab tehnika taset, kulu ja ohtu — „oleme väikesed“ ei ole vabastus",
        "kui oht on suur (eriliik, maht), peab meede olema tugevam, mitte olematu",
    ],
    "notes": (
        "Kaks lauset.\n\n"
        "Esimene: kui te otsustate, kas ehitada ühtne „kõik inimese andmed“ järv või domeenide kaupa "
        "tsoonid, on see juba artikkel 25. Kui te otsustate, kas testis on toodang või mask, on see artikkel "
        "25. Kui te lisate automaatse kustutuse või ei lisa, on see artikkel 25. Jurist, kes tuleb pärast "
        "go-live’i, on liiga hilja ja liiga kallis.\n\n"
        "Teine: vaikimisi ainult vajalik. Neli telge. Hulk — veerud ja inimesed. Ulatus — millised kasutused. "
        "Aeg — kui kaua snapshot elab. Kättesaadavus — kes näeb. Viimane on BI süda: uus aruanne ei tohi "
        "olla vaikimisi avalik kogu internetile ega kogu asutusele. Inimene või roll avab teadlikult.\n\n"
        "Proportsioon: väike seltsing ja haigla ei tee sama. Mõlemad teevad midagi, mis vastab ohule. "
        "Kulu ei ole automaatne vabastus, kui mängus on 750 000 terviserida.\n\n"
        "Tõlge: kaitse on disainivalik teie sprintides."
    ),
},
{
    "type": "cards",
    "title": "Kaks kaksikut teie tööriistades",
    "cards": [
        ("Lõimitud  ·  by design",
         "Arhitektuur alguses.\n\n• kas isikukoodi on järves vaja?\n• kas võti ja analüüs on eraldi?\n• kas test on maskeeritud?\n• kas kustutus on toru osa?\n• kas lineage ja logid on olemas?"),
        ("Vaikimisi  ·  by default",
         "Tehaseseadistus.\n\n• uus tööala suletud, mitte kogu maja\n• vaikevaade koond, mitte rida\n• allalaadimine kinni, kuni roll lubab\n• uued veerud peidus, kuni eesmärk on kirjas\n• säilitus lühike, kuni keegi põhjendab"),
    ],
    "notes": (
        "Lõimitud on skeem, tsoonid, maskeerimine, automaatne unustamine, auditilogi. Seda teeb peamiselt "
        "andmeinsener koos BI-arhitektiga. Analüütik nõuab seda, mitte ei palu „anna kõik veerud, ma filterdan“.\n\n"
        "Vaikimisi on see, mis juhtub, kui kiirustate. Kui uue aruande vaikeõigus on kogu firma, olete "
        "artikli 25 lõike 2 vastu. Kui Export Excel on vaikimisi kõigil, samuti. Kui linnuke „jaga "
        "lingiga“ on lihtsaim tee, valitakse see alati.\n\n"
        "Mäletage üht: ohutu valik peab olema mugavam kui ohtlik. Kui turvaline tee on raske, läheb inimene "
        "CSV-ga koju. See on ka disain — protsessi disain."
    ),
},
{
    "type": "content",
    "title": "Andmeinsener: tsoonid, mask, unustamine, jälg",
    "bullets": [
        "eraldage domeenid: HR / tervis / klient / logid ei ole üks avatud järv",
        "toodang ≠ test ≠ õpe; maskeerige või sünteesige enne, kui ligipääs laieneb",
        "võtmetsoon eraldi; analüütikakiht pseudonüümiga",
        "säilitus- ja kustutusreegel on pipeline’i osa, mitte käsitsitöö lubadus",
        "logige, kes luges tundlikku tsooni; lineage andmesubjekti päringuks",
    ],
    "notes": (
        "Kui te ehitate platvormi, olete artikli 25 peamine tegija.\n\n"
        "Üks avatud järv „sest analüütikud tahavad paindlikkust“ on eesmärgi piirangu ja minimeerimise "
        "vastand. Tehke tsoonid ja lepingud tsoonide vahel. Terviseandmed ei voola turunduskuubikusse "
        "sest JOIN oli lihtne.\n\n"
        "Test ja CI on lekketee number üks inseneri maailmas. Täiskoopia laiale ringile on toodangu "
        "õiguste bypass. Maskeerimine, sünteetika, kitsas salvestatud protseduur — valige, aga ärge "
        "jätke toodangut „ajutiselt“.\n\n"
        "Pseudonümiseerimine on teie kingitus analüütikule: nad saavad mudeldada ilma nime nägemata. "
        "Võti jääb kitsasse teenusesse.\n\n"
        "Unustamine: kui allikas kustutab, kas ait oskab järgneda? Kui ei, on teil illegaalne muuseum.\n\n"
        "Lineage: kui tuleb „andke mu andmed“, peate oskama öelda, millistes tabelites ta elab. See on "
        "inseneri vastus artiklitele 15 ja 17, mitte juristi Excel."
    ),
},
{
    "type": "content",
    "title": "BI-analüütik: mudel, RLS, allalaadimine, tööala",
    "bullets": [
        "ärge tooge mudelisse veerge, mida visuaal ei kasuta",
        "vaikimisi koond; rida-realt ainult rollile, RLS testitud allalaadimisel",
        "uus avaldamine: kitsas tööala, nimelised inimesed, mitte kogu asutus",
        "koolitus ja ekraanipilt: sünteetika või tugevalt kadreeritud",
        "andmestiku omanik + kustutamiskuupäev + „kes tohib Export“",
    ],
    "notes": (
        "BI on koht, kus kättesaadavus otsustatakse ühe klikiga.\n\n"
        "Mudel on minimeerimise koht. Iga kasutu veerg on lekke pind. Peidetud veerg, mis tuleb Excelisse, "
        "on vale turvatunne.\n\n"
        "RLS on vaikimisi andmekaitse, kui see päriselt töötab. Testige: teine kasutaja, teine roll, "
        "Export, Analyze in Excel, build-õigus. Kui RLS kaob allalaadimisel, ärge lubage allalaadimist "
        "või tehke eraldi koond-andmestik.\n\n"
        "Tööala: uus raport ei ole demoks kogu firmale. Andke nimelised õigused. Vaadake üle, kes on "
        "viewer vs contributor — contributor võtab andmed kaasa.\n\n"
        "Omanik: igal andmestikul peremees. Kvartali hügieen: mis on surnud, mis on liiga avatud.\n\n"
        "[KÜSI] Kes on saatnud Power BI lingi „vaata kui ilus“ ilma õigusi kontrollimata? See on inimlik. "
        "Täna on sellel nimi: vaikimisi kättesaadavus oli vale."
    ),
},
{
    "type": "content",
    "title": "Andmeanalüütik: päring, notebook, ühendamine, jagamine",
    "bullets": [
        "kirjutage eesmärk päringu kohale või ticketisse enne JOIN-i",
        "ärge tõmmake täispilti koju; töötage asutuse keskkonnas",
        "valim, koond, pseudonüüm enne, kui „vaatan korra kõiki ridu“",
        "ärge kleepige isikuandmeid avalikku keelemudelisse ega juhuslikku SaaS-i",
        "väljavõttel kuupäev ja kustutus; ärge jätke varjukausta",
    ],
    "notes": (
        "Analüütik on see, kes küsib uue küsimuse. Teie oht on uudishimu plus oskus.\n\n"
        "Hea tava: ticketis või notebooki päises kolm rida — eesmärk, allikad, kas on isikuandmed. See on "
        "läbipaistvus ja vastutus 30 sekundiga.\n\n"
        "Töötage seal, kus leping katab. Isiklik Colab isikukoodidega on volitamata töötleja. Avalik GPT "
        "samuti. Asutuse kinnine keskkond, kui on.\n\n"
        "Enne täispilti küsige, kas 10% valim või koond vastab küsimusele. Tihti vastab.\n\n"
        "Jagamine: saatke link õigesse kausta, mitte manus kümnele inimesele. Iga manus on uus koopia, "
        "mis ei sure.\n\n"
        "Kui teie küsimus nõuab uut liitmist üle domeenide — klient plus HR plus logi — see on DPO-kutse, "
        "mitte reede õhtune eksperiment."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 35",
    "title": "Millal analüütikaprojekt vajab mõjuhinnangut?",
    "bullets": [
        "kõrge oht inimeste õigustele — enne alustamist, mitte pärast kaebust",
        "tüüpiliselt: ulatuslik jälgimine, ulatuslik eriliik, skoor/profiil, mis mõjutab otsust",
        "teie roll: kirjeldada andmevoog, mahud, liitmised, kes näeb, kus elab",
        "kui jääkrisk jääb kõrgeks — AKI-ga konsulteerida enne go-live’i (art 36)",
        "uus näotuvastus, massiline asukohalogi, automaatne keeld = ärge „teeme korra“",
    ],
    "notes": (
        "DPIA on artikli 25 raskem vend. Kui oht on kõrge, ei piisa seitsmest küsimusest peas. Peab olema "
        "kirjalik hinnang: mida teeme, mis oht, mis meetmed, mis jääb.\n\n"
        "Andmetöös sattute siia, kui teete: ulatuslikku jälgimist (asukoht, kaamerad, pidev profiil); "
        "tervise- või muu eriliigi kuubikut suurele hulgale; skoori, millest sõltub laen, töö, teenus; "
        "uue tehnoloogia massilist kasutust.\n\n"
        "Teie olete DPIA-s asendamatud, sest jurist ei tea, millisest API-st read tulevad. Joonistage "
        "allikas → toru → mudel → tarbija. Ärge öelge „see on juriidika“.\n\n"
        "Kui pärast meetmeid on oht ikka kõrge, tuleb enne alustamist AKI-ga rääkida. Harva, aga olemas.\n\n"
        "Praktiline: kui teie sprint hakkab ehitama „inimese 360“ või automaatset keeldumist, kutsuge DPO "
        "sprinti planeerimisse, mitte retrospektiivi."
    ),
},
{
    "type": "exercise",
    "time": "7 minutit  ·  paarides",
    "title": "Parandage see andmeplatvorm",
    "bullets": [
        "üks järv: CRM + palgad + haiguslehed + veebilogid, ligipääs „kõik analüütikud“",
        "test = toodangu täiskoopia; CI logib päringud isikukoodiga",
        "Power BI vaikevaade: rida-realt, Export kõigile, tööala kogu asutus",
        "snapshot iga päev, keegi ei kustuta; 2019 dump elab notebookis",
        "ülesanne: 5 muudatust, mis teeksid selle lõimituks ja vaikimisi turvaliseks",
    ],
    "notes": (
        "[HARJUTUS 7 min]\n\n"
        "Taotluslikult halb. Viis muudatust. Koguge tahvlile.\n\n"
        "Oodatav:\n"
        "1. Tsoonid: HR/tervis eraldi, kitsas roll; turundus ei näe haiguslehti.\n"
        "2. Analüütikakiht pseudonüüm; identiteet ainult operatiivsele rollile.\n"
        "3. Test maskeeritud; CI ei logi isikukoode laiale ringile.\n"
        "4. BI vaikevaade koond; RLS; Export kinni või eraldi koond-andmestik; tööala nimeline.\n"
        "5. Snapshot-poliitika + kustutus; notebookide dump keelatud / tähtajaline.\n"
        "6. Omanik ja kataloog; logid tundlikule tsoonile.\n"
        "7. Haigusleht on eriliik — võib-olla ei kuulu üldse sellesse järve.\n\n"
        "Rõhutage: keegi ei keela HR-il palka näha. Keelatud on vaikimisi kõigile analüütikutele. See on "
        "artikli 25 teine lõige päriselus."
    ),
},
{
    "type": "content",
    "kicker": "OSA III  ·  KOKKUVÕTE",
    "title": "Kaitse on backlogi osa, mitte juristi kleebis",
    "bullets": [
        "lõimitud = tsoonid, mask, võti eraldi, unustamine, lineage",
        "vaikimisi = koond, suletud tööala, kitsas Export, lühike säilitus",
        "analüütik, BI ja insener lõhuvad või ehitavad seda iga päev",
        "kõrge ohu projekt: mõjuhinnang enne, DPO sprinti, mitte pärast lansseerimist",
    ],
    "callout": "Viimane plokk: kuidas teie rollis DPO-ga töötada — ja millal teda üldse vaja on.",
    "notes": (
        "Kolmas kinni, pausi ei ole.\n\n"
        "Teie kolm rolli kohtuvad artiklis 25 iga päev. Insener otsustab, kas tervis ja müük elavad samas "
        "järves. BI otsustab, kas vaikevaade on koond või rida. Analüütik otsustab, kas teha uus JOIN pühapäeval "
        "või kirjutada ticket. Kui üks kolmest lõhub, ei aita teiste hea disain.\n\n"
        "Esmaspäeva kaks tegu: esiteks vaadake üks andmestik — millised veerud on mudelis ilma visuaalita. "
        "Teiseks vaadake, kes vaikimisi näeb ja kas Export on lahti. Need kaks klikki on artikkel 25.\n\n"
        "Nüüd inimene, kellele te näitate andmevoo joonist — kui ta asutuses on — ja millal seadus ütleb, "
        "et ta peab olema. Oluline: teie ei saa DPO-ks saamisega andmekaitset „ära delegeerida“."
    ),
},
{
    "type": "section",
    "kicker": "OSA IV  ·  umbes 28 minutit",
    "title": "Andmekaitsespetsialist ja andmetöötaja",
    "subtitle": "IKÜM artiklid 37–39  ·  teie ei ole DPO  ·  teie olete esimene filter ja varajane signaal",
    "notes": (
        "Viimane suurteema. DPO, eesti keeles andmekaitsespetsialist.\n\n"
        "Kaks viga andmetiimides. Esimene: „meil on DPO, tema vastutab, meie teeme JOIN-e“. Vale. "
        "Teine: „meil ei ole DPO-d, järelikult võime analüüsida mida iganes“. Ka vale.\n\n"
        "Me vaatame, millal asutus peab määrama, mida spetsialist teeb, mis on huvide konflikt — eriti "
        "kui tahetakse panna analüütik või andmejuht DPO-ks — ja kuidas teie teda kutsute enne, mitte pärast."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artiklid 37–39",
    "title": "Kes ta on teie tiimi jaoks",
    "bullets": [
        "nõustaja ja kontaktpunkt inimestele ning AKI-le — mitte teie päringute autor",
        "jälgib, et asutus täidaks IKÜM-i; ei ole automaatselt süüdlane lekke korral",
        "vastutus jääb vastutavale töötlejale ehk asutusele, kelle nimel te Run vajutate",
        "võib olla oma või väline; peab olema pädev, mitte „linnuke kodulehel“",
        "teie tabelid on tema töö tooraine: ilma andmekaardita ei saa ta aidata",
    ],
    "notes": (
        "DPO on selleks, et organisatsioonis oleks keegi, kes oskab andmekaitset, kellel on aeg, ja kellel "
        "on tee juhtkonnani.\n\n"
        "Ta ei kirjuta teie SQL-i. Ta küsib: miks see liitmine, kes näeb, kas on eriliik, kas on DPIA. "
        "Teie tõlgite tehnika inimkeelde. See on koostöö, mitte allumine ega peitmine.\n\n"
        "Leke jääb asutuse vastutuseks. Kui te ignoreerite soovitust ja avaldate palgaaruande avatud "
        "lingiga, on see asutuse rike ja teie tööjälg.\n\n"
        "Kontakt peab olema avalik. Inimene (klient, töötaja) peab saama DPO-le kirjutada. Kui tuleb "
        "päring „minu andmed“, küsitakse teilt, millistes andmestikes ta on. Kui teie järv on nimetu, "
        "läheb kuu tähtaeg.\n\n"
        "Ärge pange DPO-ks „seda, kes teab andmeid“, kui sama inimene otsustab, mida koguda. Tuleme "
        "huvide konflikti juurde."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 37",
    "title": "Millal asutus peab DPO määrama — teie kontekst",
    "bullets": [
        "avalik sektor: kool, ministeerium, omavalitsus, paljud haiglad — jah",
        "põhitegevus = ulatuslik, korrapärane, süstemaatiline jälgimine (nt asukohaäpp, massiline profiil)",
        "põhitegevus = ulatuslik eriliik või süüteoandmed (haigla, suur tervisekuubik)",
        "väike e-pood / kolme inimese stuudio: tihti ei ole DPO kohustuslik — IKÜM kehtib ikkagi",
        "andmetiim ise ei asenda DPO-d; vabatahtlik DPO = samad sõltumatuse reeglid",
    ],
    "notes": (
        "Kolm künnist, et teaksite, kas teie tööandja peab rolli omama — ja et te ei arvaks, et analüütik "
        "on automaatselt DPO.\n\n"
        "Avalik sektor on selge jah. Kui teete haridus- või riigiaruandeid, on spetsialist olemas või peab "
        "olema. Leidke ta.\n\n"
        "Jälgimine põhitegevusena: mitte üks kaamera laos, vaid äri, mis on inimeste jälgimine — asukoht, "
        "massiline käitumisprofiil, ulatuslik videovalve teenusena.\n\n"
        "Eriliik põhitegevusena: haigla, suur hooldekodu, ulatuslik terviseanalüütika. Üks haiguslehe "
        "veerg väikeses firmas ei ole veel see künnis, aga on ikkagi eriliik ja pidur.\n\n"
        "Pagarikoda töötleb töötajate andmeid, see ei ole pagari põhitegevus. Teie kui analüütik pagarikojas "
        "peate ikkagi põhimõtteid järgima.\n\n"
        "Kui DPO-d ei ole, olete teie esimene filter. Kohustused ei kao."
    ),
},
{
    "type": "cards",
    "title": "Kas nemad vajavad DPO-d? Suund, mitte kohtuotsus",
    "subtitle": "Täpne vastus sõltub faktidest. Andmetiim ei ole iseenesest künnis.",
    "cards": [
        ("Kool / ministeerium + hariduskuubik",
         "Jah, avalik sektor.\n\nLaste andmed. Analüütik teeb koostööd, ei asenda DPO-d."),
        ("Haigla / suur apteegianalüütika",
         "Tõenäoliselt jah: eriliik + ulatus.\n\nTeie faktitabel võib olla tervis."),
        ("Väike e-pood, 200 klienti, üks Power BI",
         "Tõenäoliselt DPO ei ole kohustuslik.\n\nAlus, koond, 72 h, õigused kehtivad ikkagi."),
        ("Asutuse andmeplatvormi tiim",
         "Tiim ≠ DPO.\n\nKui asutus peab määrama, määrab. Andmejuht DPO-ks = huvide konflikti oht."),
    ],
    "notes": (
        "Neli pilti.\n\n"
        "Kool ja ministeerium: jah. Teie koondaruanne on hea, kui on tõesti koond. DPO on asutuse oma.\n\n"
        "Haigla, suur apteek: peaaegu kindlasti jah. Apotheka näitab, miks ostuajalugu ei ole „lihtsalt müük“.\n\n"
        "Väike e-pood: DPO tihti pole kohustuslik. Teie Power BI peab ikkagi olema kitsas, minimaalne, "
        "tähtajaline. „Ei ole DPO-d“ ≠ „võin SELECT * koju“.\n\n"
        "Andmetiim: teid tahetakse vahel panna DPO-ks, sest „teate andmeid“. Kui teie otsustate, milliseid "
        "isikuandmeid platvormi tuua, ja siis kontrollite iseennast, on konflikt. Parem väline või eraldi "
        "inimene.\n\n"
        "Kodutöö: vaadake asutuse veebi jalust. Kes on DPO? Kui ei tea, leidke järgmisel nädalal."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 39",
    "title": "Mida DPO teilt ootab — ja mida teie temalt",
    "bullets": [
        "tema: nõustab, jälgib poliitikaid, aitab mõjuhinnangul, räägib AKI-ga",
        "teie: andmevoog inimkeeles, mahud, veerud, kes näeb, kus koopiad elavad",
        "kutsu varakult: uus allikas, uus liitmine, uus avalik/lai aruanne, uus skoor",
        "ära oota, et ta teie SQL-i loeb — tõlgi: mis otsus, mis rida, mis oht",
        "varjuprojektid („teeme ära, muidu keelab“) on punane lipp",
    ],
    "notes": (
        "Hea koostöö: te mõtlete ühendada kliendid ja veebilogi. Viis rida DPO-le: eesmärk, andmed, kes "
        "näeb, kus, millal kustutame. Ta küsib kaks asja. Te teete vaikevaate koondiks. Odav.\n\n"
        "Halb: kolm kuud tööd, lansseerimine, kiitus, kaebus, siis DPO, kes peab ütlema juhile, et oleks "
        "pidanud olema teisiti. Kallis.\n\n"
        "Teie oskus on näha nooli. Joonistage. Iga nool on töötlemine.\n\n"
        "Kui kardate, et DPO keelab, on oht tõenäoliselt olemas. Parem keeld enne kui leke pärast.\n\n"
        "Leke või kahtlus: DPO ja juht kohe, mitte pärast „ära parandamist“. 72 tundi tiksub."
    ),
},
{
    "type": "content",
    "kicker": "IKÜM artikkel 38",
    "title": "Sõltumatus: miks andmejuht ei ole automaatselt hea DPO",
    "bullets": [
        "DPO-le ei anta juhiseid, kuidas ta oma ülesandeid täidab; allub juhtkonnale",
        "teda ei karistata ebamugava „ärge liitke seda“ eest",
        "ressurss: aeg, koolitus, ligipääs andmestikele — 0,05 kohta ei ole roll",
        "huvide konflikt: ärge pange DPO-ks seda, kes otsustab töötlemise eesmärke ja vahendeid",
        "tegevjuht, IT-juht, andmejuht, HR-juht, turundus, pearaamatupidaja — tavaliselt halb kombinatsioon",
    ],
    "notes": (
        "Sõltumatus teeb rolli päriseks.\n\n"
        "Ta peab saama öelda: see 360-profiil on ohtlik. Kui ta selle eest kaotab preemia, on artikkel 38 "
        "rikkumine.\n\n"
        "Andmetöös on konflikt klassikaline. Inimene, kes juhib andmeplatvormi, tahab, et andmed voolaksid. "
        "DPO peab vahel ütlema ei. Sama pea ei saa mõlemat ausalt teha.\n\n"
        "Analüütik, kes on tiimi ainus „andmeinimene“ ja kellele pannakse DPO müts, on samas ohus: ta "
        "kontrollib omaenda päringuid.\n\n"
        "Väikeses asutuses on ausam väline spetsialist kui näiline sisemine. Kui määrate vabatahtlikult, "
        "kehtivad ikkagi 38 ja 39 — ärge pange nime jalusesse ilma ajata."
    ),
},
{
    "type": "content",
    "title": "Millal teie ticketist peab saama DPO-ticket",
    "bullets": [
        "uus isikuandmete allikas torusse või mudelisse",
        "liitmine üle domeenide (klient + HR + logi + tervis)",
        "rida-realt või nimega vaade uuele, laiemale publikule",
        "skoor, automatiseeritud soovitus või keeld",
        "eriliik, lapsed, asukohajälg, näotuvastus, massiline profiil",
        "plaan kasutada uut pilve, keelemudelit või välist tööriista isikuandmetega",
    ],
    "callout": "Kui ticketis on sõna „360“, „kõik andmed kokku“ või „profiil“, kutsuge enne koodi.",
    "notes": (
        "See on praktiline eskalatsiooninimekiri analüütikule, BI-le ja insenerile. Pange see tiimi juhisesse.\n\n"
        "Kõik ei pea DPO-d. Uus koondmüük maakonna kaupa olemasolevast müügikuubikust — seitse küsimust "
        "piisavad. Uus „kogu kliendi elu ühes vaates kogu müügile“ — DPO.\n\n"
        "Uus tööriist on sageli unustatud: küsitluskeskkond, kaardirakendus, AutoML, tõlketeenus, avalik "
        "GPT. See on volitatud töötleja küsimus. Ärge ühendage enne lepingut.\n\n"
        "Lapsed ja tervis: alati kõrgem. Haridus- ja terviseanalüütikud — madalam künnis kutsuda.\n\n"
        "Kui kahtlete, üks lühike kiri on odavam kui kolm kuud valet suunda."
    ),
},
{
    "type": "exercise",
    "time": "6 minutit  ·  paarides",
    "title": "Kas kutsud DPO?  jah / ei / oleneb",
    "bullets": [
        "1) uus KPI: keskmine ost maakonna ja kuu kaupa, olemasolev müügimudel",
        "2) JOIN: kliendid + veebiklikid + tugipiletid „üheks profiiliks“ müügile",
        "3) testkeskkond täiskoopiaga toodangust, ligipääs kogu andmetiimile",
        "4) Power BI palgakoond osakonnale, n=4, RLS puudub",
        "5) avalik ChatGPT: kleepite 50 kliendirea „et kirjutaks kokkuvõtte“",
        "6) vallavalitsuse haridusanalüütik teeb ministeeriumile koondit",
    ],
    "notes": (
        "[HARJUTUS 6 min]\n\n"
        "1) Tavaliselt ei, DPO-d pole vaja igaks KPI-ks. Seitse küsimust + n=1 kontroll. Kui filter võimaldab "
        "ühe poe ühe kliendi, oleneb — kitsenda.\n\n"
        "2) Jah. Uus eesmärk, uus profiil, lai publik. DPO / DPIA küsimus.\n\n"
        "3) Jah, vähemalt DPO või infoturve. Toodangu bypass. See on platvormiotsus, mitte „ajutine“.\n\n"
        "4) Jah või vähemalt peatuge. Palk, väike n, identiteet kergesti tuletatav. Pole vaja oodata kaebust.\n\n"
        "5) Jah, peatuge kohe. Tõenäoline volitamata edastamine. See ei ole „ainult tekst“. DPO ja juhis "
        "keelemudelite kohta.\n\n"
        "6) Asutusel peab DPO olema (avalik sektor). Analüütik kutsub, kui koond võib muutuda tuvastatavaks "
        "või kui andmeid liigub asutuste vahel ilma kokkuleppeta. Koond ise on hea suund.\n\n"
        "Kui aeg otsas, jätke 6 suuliseks."
    ),
},
{
    "type": "content",
    "kicker": "OSA IV  ·  KOKKUVÕTE",
    "title": "DPO on kompass, mitte vihmavari teie dump’idele",
    "bullets": [
        "asutus vastutab; teie olete käsi; DPO nõustab ja valvab",
        "künnis: avalik sektor, ulatuslik jälgimine, ulatuslik eriliik",
        "andmejuht/analüütik DPO-ks = tihti konflikt; tiim ei asenda rolli",
        "kutsuge enne uue allika, profiili, laia ridade vaate, skoori või uue pilve",
    ],
    "notes": (
        "Viimane plokk kinni.\n\n"
        "DPO ei ole luksus ega karistus. Ta on luba öelda ebamugav lause enne, kui selle ütleb AKI. "
        "Kasutage teda. Kui teda ei ole, kehtivad seitse küsimust ikkagi — siis olete teie esimene filter "
        "ja teie ticketi eskalatsiooninimekiri on veel tähtsam.\n\n"
        "Andmetiimides on kiusatus öelda „see on compliance, meie teeme andmeid“. Täna nägite, et SELECT, "
        "Publish ja ACL ongi see koht, kus seadus rakendub. DPO aitab halli ala; ta ei istu teie kõrval "
        "iga värskenduse juures.\n\n"
        "Kokkuvõte: neli lauset, kümme käsku, esmaspäeva 30 minutit, allikad, küsimused. Umbes kümme minutit. "
        "Hoidke tempo, et küsimustele jääks aega."
    ),
},
{
    "type": "content",
    "kicker": "KOKKUVÕTE",
    "title": "Neli teemat, neli lauset teie rollis",
    "bullets": [
        "seadus: IKÜM kehtib ka analüüsile, mudelile ja torule; IKS täiendab; AKI valvab",
        "põhimõtted: seitse küsimust enne Run, Publish ja Share",
        "lõimitud/vaikimisi: tsoonid ja koond sisse ehitatud; ohutu valik on peal",
        "DPO: kutsuge vara; ta ei kirjuta SQL-i ega võta teie vastutust ära",
    ],
    "notes": (
        "Korrake aeglaselt.\n\n"
        "Te ei ela „kuskil Euroopas üldiselt“. Te elate Eestis, teete päringuid, ja IKÜM+IKS+AKI kehtivad "
        "teie artefaktidele.\n\n"
        "Teie igapäev on põhimõtted nupu peal, mitte lühendid.\n\n"
        "Ärge liimige kaitset otsa. Pange see skeemi, RLS-i, tööala vaikeõigusesse, snapshoti poliitikasse.\n\n"
        "DPO on liitlane. Ta ei ole vihmavari varjufailidele ega vaenlane, kelle eest sprinti peita.\n\n"
        "Kui need neli lauset on olemas, on kolm tundi õnnestunud."
    ),
},
{
    "type": "content",
    "title": "Andmetöötaja kümme käsku",
    "bullets": [
        "1  küsi enne „miks see päring“, mitte ainult „kuidas JOIN“",
        "2  kui võtme, logi või n=1-ga saab inimese kätte, on tegu isikuandmetega",
        "3  ära too isikukoodi mudelisse igaks juhuks; ära tee SELECT * torusse",
        "4  uus liitmine või uus publik = uus eesmärk, kuni tõestatakse vastupidi",
        "5  koond enne rida; väike n on Eestis oht",
        "6  igal väljavõttel, snapshotil ja notebooki dump’il on surmakuupäev",
        "7  tööala kitsas; testi Export; ära jaga „kõik kellel on link“",
        "8  test, demo ja koolitus ainult maskeeritud või sünteetiliste andmetega",
        "9  vale link või lekkinud aruanne: ütle kohe, 72 tundi tiksub",
        "10  omanik ja kirjeldus kirjas — muidu ei ole andmekaitse mõttes olemas",
    ],
    "size": 16,
    "spacing": 4,
    "notes": (
        "See on slaid, mille te pildistate. Tänane pärand teie rollile.\n\n"
        "Loen korra. Te ei pea numbreid. Te peate ära tundma hetke, kui käsi läheb Run, Publish või Share peale.\n\n"
        "Esimene on tähtsaim: miks. Kuidas te õpite sellel kursusel. Miks on andmekaitse.\n\n"
        "Kui te esmaspäeval ühe asja teete, tehke 6 või 7: leidke vana CSV või liiga avatud andmestik. "
        "See on rohkem kui slaiditeooria."
    ),
},
{
    "type": "content",
    "title": "Esmaspäeva 30 minutit",
    "bullets": [
        "joonistage üks andmevoog: allikas → toru → mudel → aruanne → allalaadimine",
        "märkige, kus on isikuandmed, eriliik, n=1 oht",
        "vaadake tööala või kausta õigused ja Export",
        "pange ühele andmestikule omanik, eesmärk, tähtaeg",
        "leidke DPO kontakt — või kes vastutab, kui teda ei ole",
    ],
    "notes": (
        "Konkreetne, mitte „ole teadlikum“.\n\n"
        "Kolmkümmend minutit esmaspäeval. Üks voog, mitte kogu platvorm — muidu ei alusta keegi. Joonistage "
        "paberile või Confluence’i: kust read tulevad, kus need mudelis on, kes aruannet näeb, kas Excel "
        "tuleb kaasa. Märkige punasega isikuandmed ja eriliik.\n\n"
        "Siis üks andmestik korda: omanik, eesmärk ühe lausega, tähtaeg. Siis DPO nimi — või aus märge, "
        "et rolli ei ole ja juhtkond vastutab otse.\n\n"
        "Kui teete seda tiimina, pange seitse küsimust PR-malli. Insenerid: tsoon ja mask backlogi. "
        "BI: RLS ja Export test. Analüütikud: keelatud on isikuandmed avalikus GPT-s ja kodukettas.\n\n"
        "See 30 minutit on tänase loengu tegelik eksam, mitte mälutest paragrahvide kohta."
    ),
},
{
    "type": "content",
    "title": "Kuhu edasi, kui päriselt tarvis",
    "bullets": [
        "Andmekaitse Inspektsioon  ·  aki.ee  — juhendid, mõisted, rikkumisteade",
        "Riigi Teataja  ·  isikuandmete kaitse seadus (IKS)",
        "EUR-Lex  ·  määrus (EL) 2016/679  (IKÜM)",
        "EDPB suunised: DPO, rikkumine, anonümiseerimine",
        "teie asutuse privaatsusteade, DPO, andmekataloog, platvormi juhis",
    ],
    "callout": "See koolitus ei asenda juriidilist nõu, AKI juhendit ega teie DPO-d.",
    "notes": (
        "Ärge alustage juhuslikust blogist. Alustage AKI-st. Seadus on Riigi Teatajas, määrus EUR-Lexis. "
        "EDPB on tihe, kui lähete sügavamale.\n\n"
        "Kõige lähem: teie DPO, teie kataloog, teie platvormi reeglid. Kui neid ei ole, on see ise leid.\n\n"
        "Kordan: ma ei andnud juriidilist nõu teie konkreetse kuubiku kohta. Päris kahtlus — DPO, jurist, AKI."
    ),
},
{
    "type": "content",
    "title": "Kolm küsimust teile — enne kui teie minult",
    "bullets": [
        "mis on üks päring, andmestik või kaust, mille te esmaspäeval üle vaatate?",
        "kes on teie DPO — või kes vastutab, kui teda ei ole?",
        "milline seitsmest küsimusest on teie tiimis kõige nõrgem?",
    ],
    "notes": (
        "[2–3 min]\n\n"
        "Mõelge. Võite öelda ühe valjusti.\n\n"
        "Esimene: konkreetne artefakt. Ilma selleta ei muutu midagi.\n\n"
        "Teine: nägu. Andmekaitse on inimeste teema.\n\n"
        "Kolmas: ausalt. Paljud ütlevad säilitamine, minimeerimine või Export. Siis teate, millega alustada.\n\n"
        "Nüüd teie küsimused."
    ),
},
{
    "type": "quote",
    "title": "Andmetarkus on oskus ridu kasutada.\nAndmekaitse on oskus inimesi nendes ridades austada.",
    "subtitle": "Aitäh. Küsimused on oodatud — ka need, mis tunduvad „liiga tehnilised“.",
    "notes": (
        "Lõpusõna.\n\n"
        "Eesmärk ei olnud teid kartlikuks teha. Eesmärk oli teha teid tähelepanelikuks just seal, kus te "
        "olete tugevad: päring, mudel, toru, aruanne. Eestis on andmed lähedal. See eelis püsib usalduse peal. "
        "Usaldus katkeb teie avatud lingi, teie SELECT *, teie testkoopia või teie unustatud dump’iga.\n\n"
        "Kasutage seitset küsimust. Pange kaitse tsoonidesse ja vaikeõigustesse. Rääkige DPO-ga enne profiili. "
        "Kui midagi katki läheb, ärge vaadake kõrvale.\n\n"
        "Aitäh. Küsimused — ka „kas RLS piisab“ ja „kas koond on alati okei“. Need on õiged küsimused.\n\n"
        "[Tüüpilised vastusealgused:]\n"
        "— RLS: hea, kui testitud allalaadimisel; ei asenda minimeerimist.\n"
        "— Koond: jah, kuni filter viib n=1 või haruldase tunnuseni.\n"
        "— ChatGPT: ärge kleepige isikuandmeid avalikku mudelisse.\n"
        "— Isikukood ühendamiseks: eelistage sisemist võtit; isikukood kitsasse tsooni.\n"
        "— Avaandmed: avalik ei tähenda iga uut eesmärki ja iga liitmist.\n"
        "— Kaamera / logid töökohal: eesmärk, teavitus, proportsioon; mitte salajane distsipliinikuubik.\n\n"
        "Lõpetage õigel ajal. Tänage."
    ),
},
]
