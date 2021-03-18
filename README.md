# Sudoku-1

Opis zadania: \
Zagadnienie znane jako sudoku (jap. od „sūji wa dokushin ni kagiru”, czyli „cyfry muszą być pojedyncze”) to szeroko znana i popularna łamigłówka, której celem jest wypełnienie diagramu o wymiarach 9×9 w taki sposób, aby w każdym wierszu, w każdej kolumnie i w każdym z dziewięciu pogrubionych kwadratów 3×3 (zwanych „blokami” lub „podkwadratami”) znalazło się po jednej cyfrze od 1 do 9. W przeciwieństwie do innych łamigłówek, sudoku nie wymaga od gracza wykonywania żadnych rachunków matematycznych, przez co wydaje się prosta. W rzeczywistości bez cierpliwości oraz umiejętności logicznego myślenia rozwiązanie diagramu nie jest możliwe. 
W 2005 roku udowodniono, że istnieje 6 670 903 752 021 072 936 960 różnych poprawnych plansz sudoku. Wiadomo także, że aby rozwiązanie planszy było jednoznaczne, potrzeba mieć podanych minimum 17 cyfr w diagramie. Nie każdy układ 17 cyfr daje jednak rozwiązanie jednoznaczne. Liczba znanych 17-cyfrowych plansz sudoku dających jednoznaczne rozwiązanie to 49 151.

Przegląd literatury z zakresu stosowanych metod: \
Do dziś powstało wiele technik rozwiązywania sudoku. Poniżej znajdują się krótkie opisy kilku z nich.
1.	Backtracking (z ang. wycofywanie)
Backtracking jest przeszukiwaniem w głąb - przed przejściem do następnej gałęzi całkowicie eksploruje wybraną gałąź, aż do znalezienia dopuszczalnego rozwiązania. Algorytm odwiedza puste komórki w określonej kolejności, wpisując cyfry po kolei lub cofając się, gdy okaże się, że żadna cyfra nie jest prawidłowa. Zaletami tej metody są gwarantowane rozwiązanie (o ile zagadka jest ważna) oraz prostota algorytmu. Wadą tej metody natomiast jest to, że czas rozwiązywania może być długi w porównaniu z algorytmami wzorowanymi na metodach dedukcyjnych.

2.	Constraint programming (z ang. programowanie z ograniczeniami)
Helmut Simonis w artykule „Sudoku as a Constraint Problem” opisuje wiele algorytmów rozumowania opartych na ograniczeniach. Niektóre solvery obejmują metodę modelowania i rozwiązywania sudoku. Według Simonisa program taki może wymagać mniej niż 100 wierszy kodu, aby rozwiązać prostą odmianę sudoku. Jeśli kod wykorzystuje silny algorytm rozumowania, włączenie algorytmu backtrackingu jest potrzebne tylko w przypadku najtrudniejszych diagramów sudoku. Metoda łącząca algorytm oparty na modelu ograniczeń z algorytmem backtrackingu posiada zalety w postaci krótkiego czasu rozwiązywania problemów i możliwości rozwiązania wszystkich diagramów sudoku.

3.	Exact cover (z ang. dokładne pokrycie)
Opis zagadnienia sudoku jako problem exact cover pozwala na znalezienie skutecznego rozwiązania, jak i na elegancję samego opisu. Użycie algorytmu takiego jak Algorytm X Knutha zazwyczaj rozwiązuje sudoku w ciągu kilku milisekund. Alternatywnym podejściem jest użycie eliminacji Gaussa w połączeniu z tzw. column and row striking (z ang. uderzanie w kolumny i wiersze).

4.	PSO (Particle Swarm Optimisation – z ang. optymalizacja rojem cząstek)
Alberto Moraglio i Julian Togelius w pracy „Geometric Particle Swarm Optimization for the Sudoku Puzzle” wykazali możliwość zastosowania GPSO do nietrywialnych przestrzeni kombinatorycznych na przykładzie sudoku. Pokazali, że określenie ogólnej postaci GPSO do formatu diagramów sudoku jest stosunkowo proste. Jednak wykazali także, że wyniki uzyskane z zastosowania algorytmu genetycznego znacznie przewyższyły wyniki uzyskane dzięki PSO.
James Hereford w artykule „Integer-valued Particle Swarm Optimization applied to Sudoku puzzles” na przykładzie sudoku opisał całkowitoliczbową odmianę PSO, która jest dostosowana do dyskretnych problemów optymalizacyjnych. Wykazał, że IPSO działa lepiej niż klasyczne PSO, ale nie tak dobrze jak algorytmy ewolucyjne, takie jak algorytmy genetyczne czy strategia ewolucyjna (μ + λ). Wysunął hipotezę, że sudoku jest trudnym problemem dla PSO, ponieważ dobre rozwiązania nie są koniecznie blisko siebie w przestrzeni poszukiwań. PSO nie ma mechanizmu „pożyczania” dobrych pod-rozwiązań od jednej z cząstek i łączenia ich z dobrymi pod-rozwiązaniami innej cząstki, jak w przypadku operatora krzyżowania występującego w algorytmach ewolucyjnych.

5.	GA (Genetic Algorithms – z ang. algorytmy genetyczne)
John M. Weiss w artykule pod nazwą „Genetic Algorithms and Sudoku” zauważył, że GA okazały się skuteczne w atakowaniu wielu NP-trudnych problemów, w szczególności problemów optymalizacyjnych, takich jak problem komiwojażera. Stwierdził natomiast, że GA okazują się „niezwykle nieskuteczne w rozwiązywaniu sudoku”, przynajmniej jeśli chodzi o czas uzyskania optymalnego rozwiązania. Jako przyczyny wskazał m. in. powolną zbieżność oraz niezdolność do ucieczki od lokalnych minimów. Z drugiej strony, wybierając wystarczająco duże wielkości populacji i rozsądne ustawienia pozostałych parametrów, algorytm był w stanie rozwiązać większość diagramów. 
Yuji Sato i Hazuki Inoue w pracy pt. „Solving Sudoku with Genetic Operations that Preserve Building Blocks” zaproponowali GA uwzględniające efektywne building blocks (z ang. bloki budujące), jak również silniejszą funkcję poszukiwania lokalnego. Stwierdzili, że algorytm z wysokim prawdopodobieństwem znajduje optymalne rozwiązania. Zauważyli również, że można się spodziewać jeszcze większej dokładności, dodając do zaproponowanego algorytmu korektę opartą na disparity hypothesis (z ang. hipoteza rozbieżności).

Algorytm:
- liczebność populacji: **a(100)**
- selekcja: wybor rodziców **µ(75)** (typ selekcji: proporcjonalna do przystosowania) -> losowo wybieramy pary do krzyżowania -> tworzymy **λ(75)** potomków -> ze zbioru **µ**+**λ** wybieramy **a** osobników do nowej populacji (typ selekcji: proporcjonalna do przystosowania)
- mutacja: nie zostanie zrealizowana na pierwszym etapie implementacji
- krzyżowanie: równomierne i jednopunktowe
- ocena (warunek stopu): maksymalna liczba iteracji **(200)**, brak poprawy najlepszego rozwiązania populacji od **(10)** iteracji, znalezienie rozwiązania (funkcja celu **= 0**)
- iteracja = stworzenie jednej populacji = generacja 

Źródła:
https://pl.wikipedia.org/wiki/Sudoku \
https://pl.qaz.wiki/wiki/Sudoku_solving_algorithms \
Helmut Simonis – „Sudoku as a Constraint Problem” \
Alberto Moraglio i Julian Togelius - „Geometric Particle Swarm Optimization for the Sudoku Puzzle” \
James Hereford – „Integer-valued Particle Swarm Optimization applied to Sudoku puzzles” \
John M. Weiss – „Genetic Algorithms and Sudoku” \
Yuji Sato i Hazuki Inoue – „Solving Sudoku with Genetic Operations that Preserve Building Blocks” \
