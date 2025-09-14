import math

number = int(input("Введите число:"))
if number < 0:
    print("Факториал отрицательного числа не существует")
else:
    print("Факториал числа равен:", math.factorial(number))
