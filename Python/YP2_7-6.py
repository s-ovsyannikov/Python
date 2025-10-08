def armstr(num):
    if num == 0:
        return None
    elif num < 0:
        raise ValueError("Input must be non-negative.")
    elif type(num) is not int:
        raise TypeError("Input must be an integer")

    first = True

    for number in range(1, num + 1):
        original = number
        symbol_qty = 0
        temp = number

        while temp > 0:
            temp = temp // 10
            symbol_qty += 1

        sum = 0
        temp = number
        while temp > 0:
            digit = temp % 10
            sum += digit**symbol_qty
            temp = temp // 10

        if sum == original:
            if first:
                print(number, end="")
                first = False
            else:
                print(",", end="")
                print(number, end="")


num = int(input("Введите верхнюю границу диапазона: "))
armstr(num)
