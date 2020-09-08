### Zadanie 7.5 | Pracownicy
"""
Napisz program obsługujący pracowników.
Przechowuj imię, nazwisko, email, rok urodzenia, pensję.

Skorzystaj z modułu json.

Przykład użycia:
$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] d Imie: Jan
Nazwisko: Nowak
Rok urodzenia: 1980
Pensja: 5000.0

$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] w Pracownicy:
- [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN
"""

import json

# employees_string = '''
# {
#     "employees": [
#         {
#         "name": "Jacek Ruszkowski",
#         "email": "jac.ruszkowski@gmail.com",
#         "phone": "509-152-818",
#         "birth_year": "1980",
#         "salary": "7000"
#         }
#     ]
# }
# '''
# data = json.loads(employees_string)


with open('employees.json') as file:
    data = json.load(file)
    print(data)

    while True:
        print("\nWhat do you want to do?")
        action = input("1 - show all employees; 2 - add new employee: ")

        if action == '1':
            for employee in data['employees']:
                print("")
                for k, v in employee.items():
                    print(f"{k.title()}: {v}")
            break
        elif action == '2':
            # wprowdzanie nowego pracownika
            new_employee = dict()
            new_employee['name'] = input("Employee name and last name: ")
            new_employee['email'] = input("Employee e-mail: ")
            new_employee['phone'] = input("Employee phone number: ")
            new_employee['salary'] = input("Employee salary: ")

            data['employees'].append(new_employee)

            with open('employees.json', 'w') as file:
                json.dump(data, file, indent=2)
            break

        else:
            print("Choose 1 or 2. Try again.")
