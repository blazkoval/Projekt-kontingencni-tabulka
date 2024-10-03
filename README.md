## Projekt-kontingencni-tabulka 

# Zadání - Analýza plánovaných hodin u studijní skupiny v časovém období (gql_ug + gql_events)

<<<<<<< HEAD
## Společné podmínky
-	Vytvořit GQL dotaz na základě existující federace, 
-	Definovat transformaci GQL response -> table rows (vstup pro kontingenční tabulku)
-	Vytvořit kontingenční tabulku
-	Vytvořit koláčový / sloupcový graf 
-	Vytvořit Sunburst / Chord graf
-	Výsledek realizujte jako ipynb notebook (autentizace jménem a heslem, realizace aiohttp, transformace response, vytvoření tabulky, vytvoření grafu).


## Postup práce

Za prvé byla potřeba vytvořit vhodný dotaz pro export dat, se kterýma by se pracovalo.

Bylo několik návrhů na dotaz, ale výsledný byl nejvhodnější po konzultaci s panem profesorem.

V projetku 'transformdata.py' je první verze transoframce a tvoření kontigenční tabulky.
V daném projektu chyběl dotaz na API a zároveň nějaký typ autentizace s API.


Dále v notebooks ve složce 'hrbolek' se nachází projekt prezentovaným na projektovém dnu 17.06.2024.
Nachází se tam autentizace, mapování, flattening a dotaz. Tyto funkce jsou upravené kódy od pana profesora.

Upravil se dotaz na API. 
Přidala se agregace dat, kdy z 'enddate' a 'startdate' byla vytvořena proměnná 'duration'.

Výsledky, které se uložili do json formátu jsou v 'aggregatedData.json'
Jelikož data jsou neúplná (není jich dostatek pro testování), tak byl vytvořen vlastní json soubor pod názvem 'aggregated.json'.

Výsledek projektu je tedy kontigenční tabulka, sloupcový graf a sunburst graf.


alt + shift + f = pr formátování jsonu
=======

alt + shift + f = pro formátování jsonu
>>>>>>> 8e3e6275faf006817c4377e9f9e8ccf649e6026f
