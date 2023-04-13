# 3
limit = int(input("Укажите число N: ")) # извлекаем корень из числа N
result = 1
i = 1
while (result < limit):
    result = 2 ** i
    if result > limit:
        break
    i+=1
    print(result)
# 2 4 8 16 32 64   100