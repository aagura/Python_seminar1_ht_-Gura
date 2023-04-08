# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


sum = int(input("Введите количество журавликов: "))

if sum % 6 != 0:
    print("Нет решения")
else:
    x = sum // 6
    y = x * 4
    print("Петя сделал", x, "журавликов")
    print("Катя сделала", y, "журавликов")
    print("Сережа сделал", x, "журавликов")
