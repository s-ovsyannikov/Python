import math


def bin_kef(num, kef):
    n = math.factorial(num)
    k = math.factorial(kef)
    t = math.factorial(num - kef)
    result = int(n / (k * t))
    return result


num = int(input("Введите число n: "))
kef = int(input("Введите число k: "))

if not type(num) == int and not type(kef) == int:
    raise TypeError("Arguments must be integers.")
if num < 0 or kef < 0 or kef > num:
    raise ValueError("Invalid values: require 0 <= kef <= num")

result = bin_kef(num, kef)
print(f"C({num}, {kef}) = {result}")
