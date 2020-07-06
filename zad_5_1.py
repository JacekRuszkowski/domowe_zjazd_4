""""### Zadanie 5.1

Zaimplementuj iterator zwracający jedynie samogłoski z zadanego ciągu znaków:

Przykładowe użycie:
for char in Vowels('ala ma kota a kot ma ale'):
"""


class OnlyVowels:
    def __init__(self, sentence, Vowels):
        self.sentence = sentence
        self.Vowels = Vowels
        self.found = []

    def __iter__(self):
        self.how_many_found = 0
        return self

    def __next__(self):
        # print("uruchomiono next")
        if self.how_many_found >= len(self.sentence):
            raise StopIteration
        self.how_many_found += 1

        for letter in self.sentence:
            if letter in self.Vowels:
                self.found.append(letter)
        return self.found


find_vowels = OnlyVowels("Zaimplementuj iterator zwracający jedynie samogłoski.", ("a", "e", "i", "o", "u", "y"))
iterator = iter(find_vowels)

print(next(iterator))
