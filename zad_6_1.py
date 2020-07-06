'''
### Zadanie 6.1 | Dane skoczków narciarskich (3 godz.)

Plik CSV z danymi: http://pgradzinski.students.alx.pl/kpython/zawodnicy.csv

Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:

1. wypisuje najwyższego, najniższego, najcięższego i najlżejszego skoczka;
gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.
2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)). Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).
3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać, być może w innej kolejności:

```
AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1
```

'''

# tworzę sbie listę list zawodników i ich danych, żeby mieć dostęp do każdej pozycji po indeksie
file = 'zawodnicy.csv'

with open(file, encoding="utf8") as csv_file:
    data = csv_file.read()

    for sign in data:
        data = data.replace(";", " ")

    list_all = data.splitlines()

    # twórzę listę jaką potrzebuję czyli lista z listami linii z csv
    final_list = []
    for line in list_all:
        final_list.append(line.split())

    # tworzę słowniki z wagą i wzrostem
    wzrost = dict()
    waga = dict()

    # wzrost
    for line in final_list:
        wzrost[str(f"{line[0]} {line[1].title()}")] = int(line[-2])

    # # waga
    for line in final_list:
        waga[str(f"{line[0]} {line[1].title()}")] = int(line[-1])

    csv_file.close()


# \\\\\\\ 1 \\\\\\\ #

# liczenie min i max wzrostu i wagi

def max_min(extreme: str, what: str):
    """
    Program liczy najniższego, najwyższego, najcięższego lub najlżejszego zawodnika z listy.
    Informacjwe co policzyć podaje użytkownik
    :param extreme: 'min' albo 'max'
    :param what: 'waga' albo 'wzrost'
    :return: Tupla ze skoczkiem i jego wagą lub wzrostem.
    """
    sort_height = sorted(wzrost.items(), key=lambda x: x[1])
    sort_weight = sorted(waga.items(), key=lambda x: x[1])
    # try:
    if extreme == 'min' and what == 'waga':
        return sort_weight[0]
    elif extreme == 'max' and what == 'waga':
        return sort_weight[-1]
    elif extreme == 'min' and what == 'wzrost':
        return sort_height[0]
    elif extreme == 'max' and what == 'wzrost':
        return sort_height[-1]
    else:
        raise ValueError


print("\nZnajdywanie najniższego, najwyższego, najcięższego lub najlżejszego zawodnika z listy.")
while True:
    what = input("Co policzyć? Wpisz 'waga' lub 'wzrost': ")
    extreme = input("Jakią wartość obliczyć? Wpisz min lub max: ")
    try:
        result = max_min(extreme, what)
        print(f"Szukany zawodnik: {' - '.join(str(x) for x in result)}")
        break
    except ValueError:
        print("Podane dane są nieprawidłowe. Spróbuj jeszcze raz.")
        continue


# \\\\\\\ 2 \\\\\\\ #

# liczenie sumy wagi skoczków z poszczególnych krajów
def weight_sum(country):
    weight = 0
    if country == "POL":
        for line in final_list:
            if line[2] == "POL":
                weight += int(line[-1])
        # print(f"{country} - suma wagi skoczków to {weight_sum} kg.")
        # break
    elif country == "GER":
        for line in final_list:
            if line[2] == "GER":
                weight += int(line[-1])
    elif country == "FIN":
        for line in final_list:
            if line[2] == "FIN":
                weight += int(line[-1])
    elif country == "AUT":
        for line in final_list:
            if line[2] == "AUT":
                weight += int(line[-1])
    elif country == "NOR":
        for line in final_list:
            if line[2] == "NOR":
                weight += int(line[-1])
    elif country == "USA":
        for line in final_list:
            if line[2] == "USA":
                weight += int(line[-1])
    else:
        raise ValueError

    return weight


countries = []
[countries.append(line[2]) for line in final_list if not line[2] in countries]

print("\nZliczanie sumy wagi skoczków z poszczególnych krajów.")
while True:
    print("Dostępne kraje:", (", ".join(countries)))
    country = input("Wybierz z listy kraj, a policze ile ważą skoczkowie: ")

    try:
        print(f"{country} - Skoczkowie ważą w sumie {weight_sum(country)} kg.")
        break
    except ValueError:
        print("Nie ma takiego kraju na liście.")
        continue


# # \\\\\\\ 3 \\\\\\\ #
#
def count_jumpers() -> dict:
    """
    Program wylicza ile jest skoczków z poszczególnych krajów i zwraca słownik z wynikiem
    :return: Słownik key = kraj, a value = iloeść skoczkó
    """
    countries = dict()
    countries_all = []
    for line in final_list:
        countries_all.append(line[2])

    for country in countries_all:
        if country == country:
            count = countries_all.count(country)
            countries[country] = count
    return countries


print("\nZliczanie ilości skoczków z poszczególnych krajów.")
count = input("Naciśnij ENTER, żeby wypisać ile w każdym kraju jest skoczków.")
for country, amount in count_jumpers().items():
    print(f"{country} -> ilość skoczków: {amount} ")
