mainArr = []
sizeArr = int(input('Укажите длину массива: '))

# Заполяем массив
for i in range(sizeArr):
    addItem = int(input('Заполните массив: '))
    mainArr.append(addItem)

userNum = int(input('Введите число: '))

# Создаем массив с расстояниями до указанного числа
distArr = []
distBtwNum = 0
for i in range(len(mainArr)):
    distBtwNum = abs(userNum - mainArr[i])
    distArr.append(distBtwNum)
print(mainArr)
print(distArr)
# Ищем в массиве с расстояниями наименьшее значение

maxDist = 0
for i in range(len(distArr)):
    if (distArr[i] > maxDist):
        maxDist = distArr[i]

lowDist = 0
for i in range(len(distArr)):
    if (distArr[i] < maxDist):
        maxDist = distArr[i]
        lowDist = i

print('Ближайшее число к числу', userNum, '- это', mainArr[lowDist])