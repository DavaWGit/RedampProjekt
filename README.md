4 testy na stránku s registračním formulářem <br>
<h1> Spouštění: </h1> V hlavní složce projektu: <br>
		pytest -n 4 .\tests --html=reports/report.html, pro spuštění všech testů najednou a vygenerování html reportu <br>
		pytest .\tests\test_[jméno testu].py, spuštění samostatného testu <br>
<h2>Potřebné pytest pluginy:</h2> html - generování reportů, xdist - spouštění testů paralelně <br> 
<h2>Hierarchie projektu:</h2> pages - POM, tests - jednotlivé test soubory, reports - vygenerované reporty <br>
<h2> Testy </h2> test_form -> testuje zda se vypíše error message při zadání špatných údajů při přihlašování <br>
		test_register -> testuje zda se dokáže uživatel dostat k finální stránce při vytváření nového účtu <br>
  		test_platform -> testuje náhodné proklikávání stránkou na více platformách s různými viewporty <br>
    		test_performance -> testuje zda se stránka načte do určitého času na různých internetových rychlostech <br>
