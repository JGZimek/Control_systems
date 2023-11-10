# Sterowanie adaptacyjne
## Analiza błędu średnio-kwadratowego w zależności od wybranych zmiennych - Projekt I
### Wstęp
W projekcie przeprowadzono eksperyment, polegający na próbie odtworzenia sygnału z wygenerowanego wcześniej szumu o rozkładzie jednostkowym.
Celem eksperymentu było zbadanie wpływu różnych czynników na jakość odtwarzanego sygnału, mierzoną za pomocą błędu średnio-kwadratowego (MSE). W szczególności, analizowano:
1. Zależność MSE od horyzontu czasowego (H)
2. Zależność MSE od wariancji szumu (VAR)
3. Optymalizacje wartości H (Hopt) w zależności od wariancji szumu (VAR).

### Generowanie zaszumionego sygnału
Aby wygenerować odpowiednio zaszumiony sygnał, skorzystano z rozkładu jednostajnego. Ten rozkład charakteryzuje się tym, że każda wartość z przedziału [0,1] ma takie samo prawdopodobieństwo wystąpienia. Ponieważ potrzebny był szum o określonej wariancji, postąpiono następująco:
1. Funkcja `np.random.rand(samples number)` generuje losowe próbki z rozkładu jednostajnego na przedziale od 0 do 1. Odejmując 0,5 od każdej próbki, przesunięto średnią do 0
2. Rozkład jednostajny na przedziale od -0,5 do 0,5 ma wariancję równą 1/12. Mnożąc przez np.sqrt(12 * variance), przeskalowano wygenerowany szum tak, aby miał żądaną wariancję
$$var(u) = (b − a)^2/12$$
3. W rezultacie, zwracana jest tablica o długości samples number, która zawiera próbki zaszumionego sygnału o średniej 0 i określonej wariancji.
```python
x = np.linspace(0, 6 * np.pi, samples_number)
sin = np.sin(x)

def sin_noise_generator(sin, samples_number, variance):
    noise = (np.random.rand(samples_number) - 0.5) * np.sqrt(12 * variance)
    return sin + noise
```
