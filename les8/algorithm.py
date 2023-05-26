from functions import create
from interface import *
path = 'directory.txt'
create(path)

userChoice = 0
while userChoice != 5:
    userChoice = interface()
    if userChoice == 1:
        from functions import addContact
        userInput = str(input('Введите ФИО и номер телефона через пробел: '))
        addContact('directory.txt', userInput)
    elif userChoice == 2:
        from functions import showAll
        print(showAll(path))
    elif userChoice == 3:
        from functions import searchByLastName
        userInput = str(input('Введите фамилию: '))
        searchByLastName(path, userInput)
    elif userChoice == 4:
        from functions import edit
        userInput = str(input('Введите фамилию, которую хотите изменить: '))
        userInputToEdit = str(input('Введите новую фамилию: '))
        edit(path, userInput, userInputToEdit)
print('Спасибо за работу. Выход...')