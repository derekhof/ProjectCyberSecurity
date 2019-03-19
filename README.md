# ProjectCyberSecurity

README

///////////////////////////////////////////
//////FILE: SinglePageScraper.py///////////
///////////////////////////////////////////

********************************************
***** SinglePageScraper(url, keywords) *****
********************************************
In de functie wordt het commentaar van een html pagina vergeleken met een lijst van keywords. 
Als positieve match is wordt dit als resultaat teruggegeven. De opbouw van het resultaat is aan te passen
in het config.json bestand. De opbouw is als volgt:

"DEFAULT_FINDING_STRING_PART_1" + url + "DEFAULT_FINDING_STRING_PART_1" + positive matched keywords

url = string
Keywords = list of strings
return value = string

********************************************
************** loadIniConfig() *************
********************************************
In de functie worden de configuratie settings ingelezen en opgeslagen in een globale variabele.
De functie geeft een boolean terug als het inlezen van het config bestand is geslaagd.

return = boolean

///////////////////////////////////////////
