def fillArr():
    condition = 1
    mainArr = []
    print('Заполняйте массив, записывая новые значения с новой строки. Для выходна введите 0')
    distElement = int(input('Введите первый элемент массива: '))
    mainArr.append(distElement)
    while (condition == 1):
        distElement = int(input('Введите следующий элемент массива: '))
        if (distElement == 0):
            break
        mainArr.append(distElement)
    return mainArr

finalArr = fillArr()

def defineIndexes():
    distArr = []
    minValue = int(input('Ввдеите минимальное зачение: '))
    maxValue = int(input('Ввдеите максимальное зачение: '))

    for i in range(len(finalArr)):
        if minValue <= finalArr[i] <= maxValue:
            distArr.append(i)
    print('Определёны индексы массива:')
    return distArr

print(defineIndexes())