# Задание №4
print("Задание №4")
heightChocolate = int(input("Введите высоту шоколадки: "))
widthChocolate = int(input("Введите длину шоколадки: "))
customPart = int(input("Введите, сколько долек вы хотите отломить от шоколадки: "))

if customPart%heightChocolate == 0 or customPart%widthChocolate == 0:
    print("Да!")
else:
    print("Нет")