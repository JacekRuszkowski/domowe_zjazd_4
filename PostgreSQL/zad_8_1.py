"""
Załóż bazę danych, która będzie zawierać dane ogłoszeń, analogiczne do tych w utworzonych wcześniej klasach.

Wersja prostsza: stwórz jedną tabelę dla ogłoszeń samochodowych (zarówno dane ogólne, jak i dane samochodu). Zadbaj
o odpowiednie typy kolumn (szczególnie ważne dla „prawdziwych” baz danych).

Wersja bardziej złożona: trzymaj dane sprzedawców w oddzielnej tabeli, a w ogłoszeniach odwołuj się do sprzedawców za
pomocą `id` ("klucz obcy") tak, aby ten sam sprzedawca mógł mieć przypisanych wiele ogłoszeń.

Wersja jeszcze bardziej złożona (tylko dla tych, którzy już znają bazy danych): ogólne dane ogłoszeń trzymaj w jednej
tabeli, a rozszerzone dane dotyczące samochodów w oddzielnej. Wówczas można też dodać tabelę zawierającą rozszerzone
dane dla ogłoszeń mieszkaniowych.

Wypełnij tabelę (/tabele) przykładowymi danymi.


"""

# zapytania w pgadmin, których użyłem do stworzenia bazy danych:

"""
create table sprzedawcy(
	id serial primary key,
	imie text,
	nazwisko text,
	nr_tel text
);

create table samochody (
	id serial primary key,
	marka text,
	cena integer,
	data_1_rej date,
	przebieg integer,
	id_sprzedawcy int references sprzedawcy(id)
)

insert into samochody (marka, cena, data_1_rej, przebieg)
values
('Ford Mondeo', 20800, '2009-03-18', 176250),
('Audi A4', 75000, '2017-03-05', 60000),
('Citroen DS4', 32900, '2011-12-19', 64458),
('Volkswagen Sharan', 38900, '2012-12-17', 216934),
('Toyota Avensis', 42000, '2014-02-13', 149500),
('Kia Stinger', 208900, '2019-07-01', 5000),
('Subaru Forester', 22755, '2009-01-01', 202000),
('Ford Mondeo', 36900, '2011-03-22', 245000),
('Renault Espace', 59900, '2016-02-27', 129000),
('Skoda Octavia', 105100, '2020-01-12', 150),
('Opel Zafira', 60900, '2018-12-05', 21000),
('Chrysler Town & Country', 58900, '2015-03-15', 98800);

insert into sprzedawcy (imie, nazwisko, nr_tel)
values
('Jan', 'Dąbrowski', '500-800-400'),
('Kzysztof', 'Krawczyk', '500-450-878'),
('Anna', 'Kowalczyk', '605-200-123')

update samochody set id_sprzedawcy = 3 where id = 7 or id = 9 or id = 12 ---- i podobnie dla innch sprzedawców. 
"""
