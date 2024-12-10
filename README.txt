3 testy na stránku s registračním formulářem
Spouštění: 	pytest -n 3 .\tests --html=reports/report.html, pro spuštění všech testů najednou a vygenerování html reportu
		pytest .\tests\test_[jméno testu].py, spuštění samostatného testu
Potřebné pytest pluginy: html - generování reportů, xdist - spouštění testů paralelně
Hierarchie projektu: pages - POM, tests - jednotlivé test soubory, reports - vygenerované reporty