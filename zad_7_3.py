"""
Napisz program wczytujący plik z logami aktywności użytkowników w systemie.
Na podstawie wczytanych danych wyświetl informację o sumarycznym czasie
przebywania każdego użytkownika w systemie.

$ python read_logs.py logs_simple.txt
Czas przebywania w systemie:
- user-1: 92 s
- user-2: 51 s
- user-3: 20 s
"""

file = 'logs_simple.txt'
log_dictionary = dict()
with open(file, encoding="utf-8") as file:
    read = file.read()
    logs_list = read.split()
    for element in logs_list:
        separate = element.split(";")
        user = separate[0]
        time = int(separate[1])
        if user not in log_dictionary:
            log_dictionary[user] = time
        else:
            log_dictionary[user] += time
    file.close()

    for user, time in log_dictionary.items():
        print(f"{user}: {time}")
