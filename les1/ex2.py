# Петя = p
# Серёжа = c
# p = c = z
# Катя = 2(p + c) = k
# 3(p + c) = 6 (допустим, что они сделали 6 журавликов)
# p + c = 2
# p = c = 1
# k = 4 * z

print("Задание №2")
countPapers = int(input("Введите, сколько всего журавликов сделали дети: "))
PetyaAndSergey = countPapers/3
Petya = PetyaAndSergey//2
Sergey = PetyaAndSergey//2
Katya = PetyaAndSergey//2 * 4
print("Петя сделал:", Petya, "Сергей сделал:", Sergey, "Катя сделала:", Katya)