"""Rozbuduj poprzednie zadanie. Plik z logami posiada informację o czasie logowania do systemu i o czasie wylogowania
z systemu. Oblicz czas spędzony w systemie na podstawie informacji o tym kiedy użytkownik się logował do systemu i
kiedy się z niego wylogowywał. """


def log_time_counter(file: str) -> dict:
    with open(file) as file:
        read = file.read()

        # tworzę listę - zmieniam każda linijkę tekstu z pliku na listę
        all_data = []
        for element in read.split():
            user_data = element.split(';')
            all_data.append(user_data)

        # liczę sumy czasów loginów i logoutów dla konkretnych użytkowników i wrzucam dane do dwówch słowników
        login = dict()
        logout = dict()

        for data in all_data:
            user = data[0]
            time = int(data[2])
            if data[1] == 'LOGIN':
                if data[0] not in login:
                    login[user] = time
                else:
                    login[user] += time
            elif data[1] == "LOGOUT":
                if data[0] not in logout:
                    logout[user] = time
                else:
                    logout[user] += time

        # obliczam sumę czasu spędzonego w systemie dla każdego użytkownika i tworzę słownik z wynikiem
        result = dict()
        for k, v in login.items():
            for k2, v2 in logout.items():
                if k == k2:
                    total_time = v2 - v
            result[k] = total_time

        return result


for user, time in log_time_counter('logs.txt').items():
    print(f"{user.title()} was logged for {time / 60:.1f} min in total.")
