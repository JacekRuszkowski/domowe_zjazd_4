"""
Zapytania do bazy danych z zawodnikami
"""

"""
--------------------1-----------------------------
-- Obok imion i nazwisk skoczków wypisz ich daty urodzenia w formacie typowym dla języka polskiego, czyli np. “07.02.2006 r.”

-- SELECT zawodnicy.imie, zawodnicy.nazwisko, to_char(zawodnicy.data_ur, 'DD-MM-YYYY') as data_ur_nowa from zawodnicy


--------------------2-------------------------------
-- Wypisz listę zawodników w formacie imię nazwisko (kraj), np. “Adam Małysz (POL)”.

-- select zawodnicy.imie ||' '|| initcap(zawodnicy.nazwisko) ||' '||'('|| zawodnicy.kraj ||')' as lista_skoczkow from zawodnicy


--------------------3-------------------------------
-- - FIS dba, aby skoczkowie narciarscy nie byli zbyt szczupli i wymaga, aby ich BMI wynosiło co
-- najmniej 20. Wypisz listę zawodników wraz z informacją czy mają odpowiednią wagę w stosunku do 
-- swojego wzrostu (informacja powinna być osobnym polem o wartości typu boolean).

-- select imie ||' '|| initcap(nazwisko) as zawodnik, waga/(wzrost/100.0)^2 > 20 as bmi_ok from zawodnicy 


--------------------4-------------------------------
--Obok imion i nazwisko skoczków wypisz ich BMI z dokładnością do 2 i 3 miejsc po przecinku.

-- select imie, nazwisko, round(waga/(wzrost/100.0)^2 , 2) as bmi from zawodnicy


--------------------5-------------------------------
--Wypisując imiona i nazwiska zamień wielkość liter w nazwiskach, tak by tylko pierwsza litera była wielka.

-- select imie, initcap(nazwisko) from zawodnicy


--------------------6-------------------------------
-- Wypisz listę wszystkich polskich zawodników.

-- select * from zawodnicy where kraj = 'POL'


--------------------7-------------------------------
-- Wypisz listę wszystkich trenerów bez podanej daty urodzenia.

--select * from trenerzy where data_ur_t is null


--------------------8-------------------------------
-- Wypisz listę zawodników w formacie imię nazwisko (kraj), np. “Adam Małysz (POL)”.
--Posortuj tę listę po nazwisku zawodnika, w kolejności alfabetycznej.

-- select imie ||' '|| nazwisko ||' '||'('|| kraj ||')' as zawodnicy_kraj from zawodnicy order by nazwisko asc


--------------------9-------------------------------
-- Wypisz listę trenerów posortowanych według daty urodzenia.

-- select * from trenerzy order by data_ur_t asc


--------------------10-------------------------------
-- Wypisz zawodników posortowanych według BMI

-- select *, round(waga/(wzrost/100.0)^2, 2) as bmi from zawodnicy order by bmi


--------------------11-------------------------------
-- - Wypisz listę zawodników urodzonych w sezonie od listopada do marca.

-- select * from zawodnicy where extract(month from data_ur) >= 11 or extract(month from data_ur) <= 3

 
--------------------12-------------------------------
-- - Znajdź trenerów, którzy nie trenują żadnych zawodników.

-- select * from trenerzy left join zawodnicy on trenerzy.kraj = zawodnicy.kraj where zawodnicy.kraj is null


--------------------13-------------------------------
-- - Znajdź trenerów, którzy trenują jakichś zawodników.

-- select imie_t ||' '|| nazwisko_t as trenerzy_trenujacy from trenerzy join zawodnicy on trenerzy.kraj = zawodnicy.kraj
-- group by trenerzy_trenujacy



--------------------13-------------------------------
-- - Znajdź zawodników, którzy nie mają trenera.

-- select imie ||' '|| nazwisko as zawodnicy_bez_trenera from zawodnicy 
-- left join trenerzy on zawodnicy.kraj = trenerzy.kraj where trenerzy.kraj is null


--------------------14-------------------------------
-- Znajdź takich zawodników, którzy są starsi od swoich trenerów. Znajdź takich zawodników, którzy są młodsi od swoich trenerów.

--zawodnicy starsi od trenerów
-- select imie, nazwisko from zawodnicy join trenerzy on zawodnicy.kraj = trenerzy.kraj
-- where data_ur < data_ur_t

--zawodnicy młodsi od trenerów
-- select imie, nazwisko from zawodnicy join trenerzy on zawodnicy.kraj = trenerzy.kraj
-- where data_ur > data_ur_t


--------------------14-------------------------------
-- - Podaj wielkości drużyn narodowych.

-- select kraj, count(kraj) as ilosc_zawodnikow from zawodnicy group by kraj


--------------------15-------------------------------
-- - Policz, ilu jest wszystkich zawodników.

-- select count(imie) as ilosc_zawdonikow from zawodnicy


--------------------16-------------------------------
-- - Podaj listę ekip uporządkowaną według średniego wzrostu zawodników.

-- select kraj, round(avg(wzrost)) as sr_wzrost from zawodnicy group by kraj


--------------------17-------------------------------
-- - Sprawdź, jaki jest największy wzrost w poszczególnych krajach.

-- select kraj, max(wzrost) as maks_wzrost from zawodnicy group by kraj


--------------------18-------------------------------
-- Sprawdź, jaki jest największy wzrost wśród wszystkich.
-- Wypisz zawodnika z największym, wzrostem

-- select * from zawodnicy
-- where wzrost = (select max(wzrost) from zawodnicy)


--------------------19-------------------------------
-- - Policz, ilu zawodników urodziło się w poszczególnych kwartałach.

-- select extract(quarter from data_ur) as kwartał, count(*) as ilosc_zawodnikow from zawodnicy
-- group by extract(quarter from data_ur)


--------------------20-------------------------------
-- - Policz, ilu zawodników urodziło się w poszczególnych latach w poszczególnych kwartałach.

-- select extract(year from data_ur) as rok, extract(quarter from data_ur) as kwartał, count(*) as ilosc_zawodnikow
-- from zawodnicy
-- group by extract(year from data_ur), extract(quarter from data_ur)


--------------------21-------------------------------
-- - Policz, jaka jest średnia wielkość ekipy narodowej.

select round(avg(ilosc_zespolow.count), 2) as srednia_wielkosc
from (select count(kraj) from zawodnicy group by kraj) as ilosc_zespolow


--------------------22-------------------------------
-- - Znajdź zawodników wyższych od Małysza.

-- select * from zawodnicy where wzrost > (select wzrost from zawodnicy where nazwisko = 'MAŁYSZ')
-- order by wzrost


--------------------23-------------------------------
-- - Znajdź zawodników starszych niż Heinz Kuttin.

-- select * from zawodnicy where data_ur > (select data_ur_t from trenerzy where imie_t = 'Heinz')
-- order by data_ur


--------------------24-------------------------------
-- - Wypisz zawodników cięższych niż średnia wśród wszystkich.

-- select * from zawodnicy where waga > (select round(avg(waga)) from zawodnicy as srednia_waga)
-- order by waga


"""