# Pythoni koolituse materjalide teadme



## Sissejuhatus

Slaidid failis `01_python_slaidid.pdf` annavad üldise sissejuhatuse Pythoni keelele ning selle kasutamisele andmeanalüütikas.

Fail `02_hello.py` teeb läbi kõige lihtsama "tere, maailm" näite ning `03_hello.ipynb` õpetab kasutama Jupyteri märkmike keskkonda, annab baas teadmised Pythoni süntaksist ja andmetüüpidest, if/else loogikast ja funktsioonide defineerimisest. Märkmiku teises pooles laadime alla peamised andmeanalüütika teegid ning teeme tutvust `pandas` ja `duckdb` pakutavate peamiste funktsioonidega.

## Andmete eeltöötlus ja visualiseerimine

Andmete eeltöötluse ja visualiseerimise baastõed teeme selgeks `04_iris.ipynb` failis toodud näidetega kasutades lihtsat klassikalist Irise andmestikku.

Selle käigus arutame, mida tähendab tunnuse jaotus ning milliste graafiku tüüpidega (KDE graafik, karpdiagram, viiuli diagram) seda kujutada.

Vaatame ka kahte kiiret ja mugavat võtet andmetest esmase ülevaate saamiseks: duckdb `SUMMARIZE` päring ja Seaborni `pairplot`.

Seejärel on soovitatav anda osalejatele aega iseseisvalt samu meetodeid proovida pingviinide andmestikul, millest annab ülevaate `05_penguin.ipynb`. See andmestik on umbes kaks korda suurem, sisaldab puuduvaid väärtuseid ning on seega natuke sarnasem päris elule.

Pingviinide andmestiku peal saab näitlikustada ka ennustavate mudelite treenimise ja ennustuste genereerimise põhimõtteid, antud näites oleme kasutanud logistilist regressiooni `statsmodels` teegist.

## Andmete sisse lugemine eri allikatest

Märkmik `06_data_ingestion.ipynb` demonstreerib andmete sisse lugemist kolmest peamisest allikast:

- failidest kasutades `pd.read_*` funktsioone
- andmebaasidest Postgresi näitel
- REST APIdest kasutades `requests` teegi võimalusi

## Päris eluline näide EMTA andmetel

EMTA kodulehelt saadud andmetega teeme läbi praktilise ja päriselulise andmeanalüütika näite, mis on toodud märkmikus `07_emta.ipynb`. Andmete saamiseks on vaja all laadida kaks faili: `tasutud_maksud_kaesolev_aasta.csv` ja `tasutud_maksud_varasemad_aastad.csv`, nende leidmisel on abiks kuvatõmmis `andmed_saad_siit.png`, kus on näha nii URL kui asukoht lehel.

Teeme läbi järgmised sammud:

- andmetega tutvumine 
- kahe tabeli kokku ühendamine (duckdb `UNION`)
- tabeli pööramine pikalt kujult laiale kujule (duckdb `UNPIVOT`)
- Pythonis defineeritud funktsioonide kasutamine duckdb päringute sees, et teostada operatsioone, mida on puhtas SQLis ebamugav või suisa võimatu teha
- avastuslik andmeanalüüs (duckdb `SUMMARIZE` ja graafikud)
- logaritmilise skaala kasutamine, et visualiseerida andmeid, mis on sisuliselt eksponentsiaalse jaotusega
- statistiline testimine, antud näites `mannwhitneyu` test kontrollimaks, kas Tartumaa ja Pärnumaa ettevõtete käibed on statistiliselt olulisel määral erinevad

## Interaktiivsete töölaudade loomine Streamliti abil


Fail `08_streamlit_emta.py`  ja `pages/palgad.py` moodustavad Streamlit'i äpi, mis loob samadest EMTA andmetest interaktiivse töölaua. Töölaua avaleht annab ülevaate Eesti majandusest kohalike omavalitsuste lõikes, raporti teine leht aga palkadest majandusharude lõikes.

Töölaua vaatamiseks tuleb käivitada Streamlit'i server käsuga `python -m streamlit run streamlit_emta.py`, käsk tuleb käivitada `Python` kaustas. 
