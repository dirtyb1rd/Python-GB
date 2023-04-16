mainArr = []
sizeArr = int(input('Укажите длину массива: '))

# Заполяем массив
for i in range(sizeArr):
    addItem = int(input('Заполните массив: '))
    mainArr.append(addItem)

userItem = int(input('Введите элемент, который хотите посчитать: '))

count = 0
for i in range(len(mainArr)):
    if (mainArr[i] == userItem):
        count += 1
print(count)