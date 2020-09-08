"""
Wykorzystaj napisane już wcześniej klasy/metody do obsługi CSV dla Twoich klas z ogłoszeniami.
"""
import csv


class Advert:
    def __init__(self, title: str, price: float, contact: str):
        self.title = title
        self.price = price
        self.contact = contact

    def get_info(self):
        return f"{self.title}, {self.price}, {self.contact}"

    def __str__(self):
        return self.get_info()


class AdvertsList:
    def __init__(self):
        self.elements = ["Title, Price, Contact"]


    def add_advert(self, advert: Advert):
        self.elements.append(advert)

    def list_lenght(self):
        return len(self.elements)

    # obsługa pliku csv
    def write_to_csv(self, file):
        with open(file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter="\t")
            for row in self.elements:
                writer.writerow([row])

    def read_csv(self, file):
        with open(file, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                adverts_list = row
                print(' '.join([format(word, '<15') for word in adverts_list]))

    # wypisanie wszystkich ogłoszeń
    def wypisz(self):
        print("Aktualne ogłeszenia:")
        for element in self.elements:
            print(element)


adv1 = Advert("Opel Vectra", 11000, "508 145 525")
adv2 = Advert("Subaru forester", 35000, "503 206 400")
adv3 = Advert("Honda Civic", 15000, "500 658 898")
adv4 = Advert("Mitsubishi ASX", 45300, "605 654 123")
adv5 = Advert("Ford Mondeo", 33000, "603 562 980")
adv6 = Advert("Renault Megane", 23000, "603 562 980")

ogloszenia = AdvertsList()
ogloszenia.add_advert(adv1)
ogloszenia.add_advert(adv2)
ogloszenia.add_advert(adv3)
ogloszenia.add_advert(adv4)
ogloszenia.add_advert(adv5)
ogloszenia.add_advert(adv6)

# ogloszenia.write_to_csv('samochody_ogloszenia.csv')
ogloszenia.read_csv('samochody_ogloszenia.csv')


