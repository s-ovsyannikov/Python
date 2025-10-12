def print_max(a, b):
    """
    Prints the maximum of two numbers.

    Parameters:
    a -- first number
    b -- second number

    Note:
    If a and b are equal, it prints that they are equal.
    """
    if a > b:
        print(a, "is max")
    elif a == b:
        print(a, "equals to", b)
    else:
        print(b, "is max")


# Пример вызова:
print_max(3, 5)

# Получение справки:
help(print_max)
