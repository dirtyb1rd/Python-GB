# 2
firstNum = int(input("Загадайте первое число: "))
secondNum = int(input("Загадайте второе число: "))

while (firstNum or secondNum) > 1000:
    print("Числа должны быть не больше 1000. Повторите ввод")
    firstNum = int(input("Загадайте первое число: "))
    secondNum = int(input("Загадайте второе число: "))

firstGuess = int(input("Угадайте первое число: "))
secondGuess = int(input("Угадайте второе число: "))

while (firstGuess != firstNum) or (secondGuess != secondNum):
    print("Подсказка:\nПроизведение этих чисел равно", firstNum * secondNum, "\nИх сумма равна", firstNum + secondNum)
    firstGuess = int(input("Загадайте первое число: "))
    secondGuess = int(input("Загадайте второе число: "))
print("Поздравляю. Вы угадали!")