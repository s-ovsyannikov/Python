def tribonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    a, b, c = 0, 1, 1
    for i in range(3, n + 1):
        next_value = a + b + c
        a, b, c = b, c, next_value
    return c


n = int(input("Введите номер числа Трибоначчи: "))

if not isinstance(n, int):
    raise TypeError("Input must be an integer.")

if n < 0:
    raise ValueError("Input must be a non-negative integer.")

result = tribonacci(n)
print(f"T({n}) = {result}")
