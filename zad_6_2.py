'''
### Zadanie 6.2 | Policz wybrane słowo (1 godz.)

Plik z utworem "Pan Tadeusz" do pobrania: http://pgradzinski.students.alx.pl/kpython/pan-tadeusz.txt

Niech program dla podanej nazwy pliku tekstowego i dla podanego słowa policzy ile razy to słowo występuje w pliku
(np. Tadeusz w pliku `pan-tadeusz.txt`).
'''


def word_counter(word: str, file) -> int:
    """
    Program szuka danego wyrazu w pliku tekstowym i podaje ile razy wystepuje.
    :param file:
    :param word:
    :return:
    """
    plik = open(file, encoding="utf8")
    tekst = plik.read()
    words = tekst.split(' ')
    count = 0
    for x in words:
        if x.lower() == word.lower():
            count += 1

    plik.close()

    return count


file = input("Podaj nazwę pliku: ")
word = input("Podaj szukane słowo: ")
try:
    print(f"Ilosc wystąpień słowa '{word}': {word_counter(word, file)}")
except FileNotFoundError:
    print("Nie ma takiego pliku.")
