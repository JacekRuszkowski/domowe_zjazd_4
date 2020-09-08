"""
Napisz program odczytujący dane z Twojej nowo utworzonej bazy.

Następnie spróbuj napisać program, który wczytuje dane z bazy i zapisuje je w pliku CSV.

Wykorzystaj napisane już wcześniej klasy/metody do obsługi CSV dla Twoich klas z ogłoszeniami.

"""

import psycopg2
import csv

# połączanie z bazą danych
conn = psycopg2.connect(
    host="localhost",
    database="ogloszenia",
    user="postgres",
    password="dejmos_1"
)
cur = conn.cursor()


# wczytywanie dancyh z tabelek z bazy danych
def read_DB(query):
    cur.execute(f"{query}")
    result = cur.fetchall()
    for line in result:
        print(line)

# edytowanie tabel
def edit_DB(query: str):
    cur.execute(f"{query}")
    conn.commit()


# zapisywanie do csv
def write_to_csv(file, table):
    outpuquery = f"COPY {table} to STDOUT CSV HEADER"
    with open(file, 'w', encoding="utf-8") as csv_file:
        cur.copy_expert(outpuquery, csv_file)


# wczytywanie pliku csv
def read_file(file):
    with open(file, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            adverts_list = row
            print(' '.join([format(word, '<15') for word in adverts_list]))



read_DB("select * from samochody join sprzedawcy on samochody.id_sprzedawcy = sprzedawcy.id")
# write_to_csv('sprzedawcy.csv', 'sprzedawcy')
# read_file('samochody.csv')
# edit_DB("")


cur.close()
conn.close()
