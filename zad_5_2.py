"""
Zaimplementuj generator zwracający jedynie samogłoski z zadanego ciągu znaków:

Przykładowe użycie:
for char in vowels('ala ma kota a kot ma ale'):
    ...
"""


def only_vowels(sentence):
    vowels = ["a", "e", "i", "o", "u", "y"]
    for letter in sentence:
        if letter in vowels:
            yield letter


vowels_list = []
for x in only_vowels('Zaimplementuj iterator zwracający jedynie samogłoski.'):
    vowels_list.append(x)

print(vowels_list)
