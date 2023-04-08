num = input("Введите номер билета: ")
sum1 = int(num[0]) + int(num[1]) + int(num[2])  # сумма первых трех цифр
sum2 = int(num[3]) + int(num[4]) + int(num[5])  # сумма последних трех цифр
if sum1 == sum2:
    print("yes")
else:
    print("no")
