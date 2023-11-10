# Sterowanie adaptacyjne
## Analiza błędu średnio-kwadratowego - Projekt I
W projekcie przeprowadzono eksperyment, polegający na próbie odtworzenia sygnału z wygenerowanego wcześniej szumu o rozkładzie jednostkowym.
Celem eksperymentu było zbadanie wpływu różnych czynników na jakość odtwarzanego sygnału, mierzoną za pomocą błędu średnio-kwadratowego (MSE). W szczególności, analizowano:

### Zależność MSE od horyzontu czasowego (H)
Z wykresu wynika, że MSE spada wraz ze wzrostem H. To sugeruje, że większa liczba próbek sygnału zaszumionego pozwala na lepszą rekonstrukcję sygnału oryginalnego. Jednak MSE nie spada do zera, lecz osiąga minimum dla pewnej wartości Hopt (H optymalne), po której zaczyna ponownie wzrastać. Hopt to horyzont czasowy, dla którego MSE jest najniższe.  

![Zależność MSE od horyzontu czasowego (H)](Charts_first_project/MSE(H).png)
### Zależność MSE od wariancji szumu (VAR) 
Zwiększenie wariancji szumu wpływa negatywnie na MSE, co widać na wykresie. Jest to spowodowane tym, że sygnał oryginalny jest bardziej zniekształcony przez szum i traci na jakości.  

![Zależność MSE od wariancji szumu (VAR)](Charts_first_project/MSE(var).png)
### Optymalizacje wartości H (Hopt) w zależności od wariancji szumu (VAR)
Zgodnie z tym co da się zauważyć na wykresie, horyzont optymalny jest funkcją rosnącą VAR. To znaczy, że większa wariancja szumu wymaga większej liczby próbek sygnału zaszumionego do minimalizacji MSE.  

![Optymalizacje wartości H (Hopt) w zależności od wariancji szumu (VAR)](Charts_first_project/Hopt(var).png)

### Wnioski
Główne wyniki obserwacji z eksperymentu odtwarzania sygnału sinusoidalnego na podstawie szumu o rozkładzie jednostkowym są następujące:
1. MSE jest miarą jakości odtwarzania sygnału oryginalnego na podstawie sygnału zaszumionego.
2. MSE maleje wraz ze wzrostem liczby próbek sygnału zaszumionego (H), ale tylko do pewnej wartości optymalnej (Hopt), po której zaczyna rosnąć.
3. Hopt zależy od wariancji szumu (VAR) i rośnie wraz z nią.
4. Im większa VAR, tym większy MSE i tym trudniej odtworzyć sygnał oryginalny.
5. W celu uzyskania najlepszych wyników należy dobierać H tak, aby było równe Hopt dla danego poziomu VAR.
