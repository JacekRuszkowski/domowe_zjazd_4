### Zadanie 7.1 | Pobieranie informacji z API metaweather
"""
Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
Skorzystaj z modułu urllib.request, json oraz API MetaWeather.
"""

import json
import urllib.request
from urllib.request import Request
from urllib.error import URLError, HTTPError

location = input("Enter location: ")
if " " in location:
    location = location.replace(" ", "+")

# w pierwszym zapytaniu wyciągam nr woeid
url = f'https://www.metaweather.com/api/location/search/?query={location}'

query = Request(url)
with urllib.request.urlopen(query) as req:
    result = json.loads(req.read())
    if not result:
        print(f"Sorry. We don't have weather data for {location.replace('+', ' ').title()}.")
    else:
        for data in result:
            for k, v in data.items():
                if k == "woeid":
                    woeid = v

        # w drugim zapytaniu sprawdzam pogodę po numerze woid
        url2 = f'https://www.metaweather.com/api/location/{woeid}/'

        query2 = Request(url2)
        with urllib.request.urlopen(query2) as req2:
            result2 = json.loads(req2.read())
            data2 = next(iter(result2.values()))
            print(f"\nTodays weather for {location.replace('+', ' ').title()}: \n")
            for k2, v2 in data2[0].items():
                print(f"{k2.title()} -> {v2}")




