# path = 'directory.txt'
def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        print('Файл: "справочник -> directory.txt"')
        file = open(path, 'w')
    finally:
        file.close()


def addContact(fileName, content):
    data = open(fileName, 'a')
    data.write(content + '\n')
    data.close()

def showAll(fileName):
    data = open(fileName, 'r')
    for content in data:
        print(content)
    data.close()

def searchByLastName(fileName, lastName):
    a = 0
    data = open(fileName, 'r')
    for content in data:
        if(lastName in content):
            print(content + '\n Найдено!')
            a = 123
            break
    if a != 123:
        print('No way')
    data.close()

def edit(fileName, pastContent, newContent):
    data = open(fileName, 'r+')
    for line in data:
        if(pastContent in line):
            pastContent = data.writelines(newContent)
        else:
            print('Нет информации для изменения...')
    data.close()