startElement = int(input('Введите первый элемент арифмитической прогресии (a1): '))
difference = int(input('Укажите разность арифмитической прогресии (d): '))
countElements = int(input('Введите количество элементов в арифмитической прогрессии: '))
elements = []

for i in range(countElements):
    elements.append(startElement + i * difference)

print(elements)