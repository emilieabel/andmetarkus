@echo off
cd /d "%~dp0"

if not exist parool.txt (
    echo Puudub parool.txt
    pause
    exit /b 1
)

echo 1/3  Bronze: organizations + activities API
python lae_bronze.py
if errorlevel 1 goto :viga

echo 2/3  SQL protseduur: dim_organizations + fact_activities
python kaivita_sql.py
if errorlevel 1 goto :viga

echo 3/3  Aruanne
python loo_aruanne.py
if errorlevel 1 goto :viga

echo.
echo Valmis. Ava aruanne.html  voi  Liikumisaktiivsus.pbip
echo.
pause
exit /b 0

:viga
echo Katkes.
pause
exit /b 1
