# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трехзначное число: "))

# Разбиваем число на цифры
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

# Суммируем цифры
digit_sum = digit1 + digit2 + digit3

# Выводим результат
print("Сумма цифр трехзначного числа", number, "равна", digit_sum)