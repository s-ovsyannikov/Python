def decimal_to_binary(num):
    binary = ""
    while num // 2 != 0:
        last = num % 2
        last = str(last)
        binary += last

        rest = num // 2

        next = rest % 2
        next = str(next)
        binary += next

        next = rest // 2

        num = next
    result = binary[::-1]
    return result


num = int(input("Введите десятичное число: "))

# вызов ошибок ввода
if num < 0:
    raise ValueError("Only non-negative integers are allowed.")
elif not isinstance(num, int):
    raise TypeError("Input must be an integer.")

binary = decimal_to_binary(num)
print(f"Двоичное представление: {binary}")
