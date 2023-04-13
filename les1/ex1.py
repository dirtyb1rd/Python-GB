# # Задание 1
print("Задание №1")
userNum = int(input("Введите трёхзначное число: "))
digitOne = round(userNum/100) # 1.23 without round ()
digitTwo = (userNum//10) % 10
digitThree = userNum%10
result = digitOne + digitTwo + digitThree
print("Резльтат сложения всех разрядов числа", userNum, "равен", result)