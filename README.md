# Sterowanie adaptacyjne
## Analiza błędu średnio-kwadratowego - Projekt I
W projekcie przeprowadzono eksperyment, polegający na próbie odtworzenia sygnału z wygenerowanego wcześniej szumu o rozkładzie jednostkowym.
Celem eksperymentu było zbadanie wpływu różnych czynników na jakość odtwarzanego sygnału, mierzoną za pomocą błędu średnio-kwadratowego (MSE). W szczególności, analizowano:
### Zależność MSE od horyzontu czasowego (H)
![Zależność MSE od horyzontu czasowego (H)](Charts_first_project/MSE(H).png)  
Z wykresu wynika, że MSE spada wraz ze wzrostem H. To sugeruje, że większa liczba próbek sygnału zaszumionego pozwala na lepszą rekonstrukcję sygnału oryginalnego. Jednak MSE nie spada do zera, lecz osiąga minimum dla pewnej wartości Hopt (H optymalne), po której wzrasta znacznie. Hopt to horyzont czasowy, dla którego MSE jest najniższe.
### Zależność MSE od wariancji szumu (VAR)
![Zależność MSE od wariancji szumu (VAR)](Charts_first_project/MSE(var).png)  
Zwiększenie wariancji szumu wpływa negatywnie na MSE, co widać na wykresie. Jest to spowodowane tym, że sygnał oryginalny jest bardziej zniekształcony przez szum i traci na jakości.
### Optymalizacje wartości H (Hopt) w zależności od wariancji szumu (VAR)
![Optymalizacje wartości H (Hopt) w zależności od wariancji szumu (VAR)](Charts_first_project/Hopt(var).png)  
Zgodnie z wykresami, horyzont optymalny jest funkcją rosnącą VAR. To znaczy, że większa wariancja szumu wymaga większej liczby próbek sygnału zaszumionego do minimalizacji MSE.
