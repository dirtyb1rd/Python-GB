# Задание №3
print("Задание №3")
ticket = int(input("Введите номер вашего билета: "))
ticketRight = ticket%1000
# Получаем четвртый разряд. Если он больше или равен 5, то число окргулятся, т. е ticketL + 1. Нам это не надо, поэтому отнимаем единицу
ticketMid = ticket%1000
ticketMid = round(ticketMid/100)
ticketLeft = round(ticket/1000)
if ticketMid >= 5:
    ticketLeft = ticketLeft - 1

ticketLeftDigitOne = ticketLeft//100
ticketLeftDigitTwo = ticketLeft//10
ticketLeftDigitTwo = ticketLeftDigitTwo%10
ticketLeftDigitThree = ticketLeft%10


ticketRightDigitOne = round(ticketRight/100)
ticketRightDigitTwo = ticketRight//10
ticketRightDigitTwo = ticketRightDigitTwo%10
ticketRightDigitThree = ticketRight%10

if ticketLeftDigitOne + ticketLeftDigitTwo + ticketLeftDigitThree == ticketRightDigitOne + ticketRightDigitTwo + ticketRightDigitThree:
    print("У вас счастливый билет! Ура!\nНомер билета:", ticket)
else:
    print("Вам не повезло...\nВаш билет:", ticket)