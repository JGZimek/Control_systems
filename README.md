# Sterowanie adaptacyjne
## Analiza błędu średnio-kwadratowego - Projekt I
W projekcie przeprowadzono eksperyment, polegający na próbie odtworzenia sygnału z wygenerowanego wcześniej szumu o rozkładzie jednostkowym.
Celem eksperymentu było zbadanie wpływu różnych czynników na jakość odtwarzanego sygnału, mierzoną za pomocą błędu średnio-kwadratowego (MSE). W szczególności, analizowano:
1. Zależność MSE od horyzontu czasowego (H)
2. Zależność MSE od wariancji szumu (VAR)
3. Optymalizacje wartości H (Hopt) w zależności od wariancji szumu (VAR).

### Generowanie zaszumionego sygnału
Aby wygenerować odpowiednio zaszumiony sygnał, skorzystano z rozkładu jednostajnego. Ten rozkład charakteryzuje się tym, że każda wartość z przedziału [0,1] ma takie samo prawdopodobieństwo wystąpienia. Ponieważ potrzebny był szum o określonej wariancji, postąpiono następująco:
1. Funkcja `np.random.rand(samples number)` generuje losowe próbki z rozkładu jednostajnego na przedziale od 0 do 1. Odejmując 0,5 od każdej próbki, przesunięto średnią do 0
2. Rozkład jednostajny na przedziale od -0,5 do 0,5 ma wariancję równą 1/12. Mnożąc przez np.sqrt(12 * variance), przeskalowano wygenerowany szum tak, aby miał żądaną wariancję
$$var(u) = \frac{(b − a)^2}{12}$$
3. W rezultacie, zwracana jest tablica o długości samples number, która zawiera próbki zaszumionego sygnału o średniej 0 i określonej wariancji.
```python
x = np.linspace(0, 6 * np.pi, samples_number)
sin = np.sin(x)

def sin_noise_generator(sin, samples_number, variance):
    noise = (np.random.rand(samples_number) - 0.5) * np.sqrt(12 * variance)
    return sin + noise
```
### Filtracja zaszumionego sygnału
W celu odtworzenia sygnał oryginalnego użyto estymatora uśredniającego, który wykorzystywał określoną liczbę próbek sygnału zaszumionego do wyznaczenia jednej próbki sygnału odfiltrowanego:
$\hat{\theta}_{k} = \frac{1}{H}\sum_{i=1}^{H}\theta_{k-i}$
Parametr H oznacza horyzont czasowy estymatora. Im większy jest H, tym więcej informacji jest branych pod uwagę przy filtracji (co pozwala lepiej usunąć szum), ale też powoduje silne uśrednienie przebiegu sygnału.
```python
def sin_denoise_filter(sin_noise, h):
    sin_denoised = []
    for i in range (1, len(sin_noise) + 1):
        sin_denoised.append(np.mean(sin_noise[time_horizon_setter(i,h):i]))
    return sin_denoised
```
### Analiza błędu średnio-kwadratowego w zależności od wybranych parametrów
Poniżej przedstawiono wyniki przeprowadzonych badań wpływu parametrów na błąd średnio-kwadratowy (MSE) oraz optymalny horyzont czasowy (Hopt) przy zadanej liczbie próbek N. Błąd ten obliczano zgodnie z poniższym wzorem:
$MSE(\hat{\theta}_{k}) = \frac{1}{N}\sum_{k=0}^{N}(\hat{\theta}_{k}-\theta_{k}^{*})^2$
 
Jak zależy $MSE(\hat{\theta}_{k})$ od $H$?  
Z wykresu wynika, że MSE spada wraz ze wzrostem H. To sugeruje, że większa liczba próbek sygnału zaszumionego pozwala na lepszą rekonstrukcję sygnału oryginalnego. Jednak MSE nie spada do zera, lecz osiąga minimum dla pewnej wartości Hopt (H optymalne), po której wzrasta znacznie. Hopt to horyzont czasowy, dla którego MSE jest najniższe.

Jak zależy $$MSE(\hat{\theta}_{k})$ od $var z_{k}$$?  
Zwiększenie wariancji szumu wpływa negatywnie na MSE, co widać na wykresie. Jest to spowodowane tym, że sygnał oryginalny jest bardziej zniekształcony przez szum i traci na jakości.

Jak zależy $H_{opt}$ od $var z_{k}$?  
Zgodnie z wykresami, horyzont optymalny jest funkcją rosnącą VAR. To znaczy, że większa wariancja szumu wymaga większej liczby próbek sygnału zaszumionego do minimalizacji MSE.
