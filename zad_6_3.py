"""
Podstawowa funkcjonalność:
Napisz program, który czyta plik tekstowy i wylicza oraz wypisuje bez powtórzeń wszystkie słowa występujące w pliku
wraz z informacją ile razy dane słowo występuje. Na przykład w ten sposób:

```
Zosia -> 34
Asesor -> 35
dwóch -> 35
Tadeusz -> 107
```

Ewentualne uproszczenie (w razie problemów z wypisywaniem): wypisz tylko jedno najczęściej występujące słowo.

Dalsze rozszerzenia (opcjonalnie):
- posortuj wypisywane słowa
- oprócz liczby poszczególnych słów policz i wypisz także liczbę wszystkich słów, łączną liczbę wszystkich znaków.

"""


def count_words_occur(file: input) -> dict:
    """
    Program liczy ilość wystąpień wszystkich wyrazów w pliku tekstowym.
    :param file: nazwia pliku wprowadzana przez użytkownika
    :return: Słownik z wyrazami i ilością wystąpień ułożony alfabetycznie
    """
    with open(file, encoding="utf8") as file:
        text = file.read()  # czytanie pliku

        # usuwanie znaków interpunkcyjnytch
        signs = [",", " ", ".", ";", ":", "-", "!", "?", "(", ")", "—", "…", "»", "«", "*", "/"]
        for char in signs:
            text = text.replace(char, " ")

        # tworzenie słownika z wyrazami i ilością wystąpień
        words_count = dict()

        # liczenie słów w sformatowanym tekście
        for word in text.split():
            if word.lower() in words_count:
                words_count[word.lower()] += 1
            else:
                words_count[word.lower()] = 1

        # sortowanie wyniku al;fabetycznie
        sort_words_count = dict(sorted(words_count.items(), key=lambda x: x[0]))
        file.close()

        return sort_words_count


def count_all_words(file: input) -> int:
    """
    Program liczy ilość wszystkich wyrazów w pliku tekstowym.
    :param file: nazwia pliku wprowadzana przez użytkownika
    :return: Liczba wyrazów
    """
    with open(file, encoding="utf8") as file:
        text = file.read()
        signs = [",", " ", ".", ";", ":", "-", "!", "?", "(", ")", "—", "…", "»", "«", "*", "/"]
        for char in signs:
            text = text.replace(char, " ")

        count = 0
        for word in text.split():
            count += 1
        return count


def count_signs(file: input) -> int:
    """
    Program liczy ilość wszystkich znaków (ze spacjami) w pliku tekstowym.
    :param file: nazwia pliku wprowadzana przez użytkownika
    :return: Liczba znakó
    """
    with open(file, encoding="utf8") as file:
        text = file.read()
        text_in_line = text.replace("\n", "")

        count = 0
        for char in text_in_line:
            count += 1
        file.close()
        return count


# wpradzaenie interakcji z użytkownikiem

while True:
    print(
        "Co mam zrobić? Wybierz nr działania i naciśnij enter\n1 -> policzyć ilość wystąpień każdego wyrazu w pliku;\n2 -> "
        "Policzyć ilość wszystkich wyrazów w pliku;\n3 -> Policzyć ilość znaków w pliku. ")
    choose = int(input())

    if choose == 1:
        file = input("Podaj nazwę pliku: ")
        try:
            print("\nWyrazy i ilość wystąpień:")
            for key, value in count_words_occur(file).items():
                print(f"{key} -> {value}")
            break
        except FileNotFoundError:
            print("Nie ma takiego pliku. Spróbuj jeszcze raz\n")
            continue
    elif choose == 2:
        file = input("Podaj nazwę pliku: ")
        try:
            print(f"Ilość wyrazów w pliku: {count_all_words(file)}")
            break
        except FileNotFoundError:
            print("Nie ma takiego pliku. Spróbuj jeszcze raz\n")
            continue

    elif choose == 3:
        file = input("Podaj nazwę pliku: ")
        try:
            print(f"Ilość znaków w pliku: {count_signs(file)}")
            break
        except FileNotFoundError:
            print("Nie ma takiego pliku. Spróbuj jeszcze raz\n")
            continue
    else:
        print("Nie podałeś prawidłowego numeru. Spróbuj jeszcze raz.\n")
        continue
