# 1
countCoins = int(input("Введите количество монет (n): "))
eagleCoins = int(input("Введите количество монет, лежащие вверх гербом: "))
numberCoins = int(input("Введите количество монет, лежащие вверх решкой: "))
while (eagleCoins + numberCoins > countCoins):
    print("Число монет не должно превышать", countCoins)
    eagleCoins = int(input("Введите количество монет, лежащие вверх гербом: "))
    numberCoins = int(input("Введите количество монет, лежащие вверх решкой: "))

if (eagleCoins == numberCoins):
    print("Нужно перевернуть", eagleCoins, "монет")
elif (eagleCoins > numberCoins):
    print("Необходимо перевернуть", numberCoins, "монет")
else:
    print("Необходимо перевернуть", eagleCoins, "монет")