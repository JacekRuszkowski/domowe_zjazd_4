# Nie potrzebujuę dawać separatrora " "


file = 'lorem.txt'

with open(file, encoding="utf8") as file:
    text = file.read()


    words_count = dict()

    for word in text.split():
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    for word, count in words_count.items():
        print(f"{word} -> {count}")
