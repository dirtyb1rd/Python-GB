def checkPhrase(song):
    volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    parts = song.split()
    summary = list()
    for item in parts:
        k = 0
        for letter in item:
            if letter in volwes:
                k += 1
        summary.append(k)
    if len(set(summary)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')
