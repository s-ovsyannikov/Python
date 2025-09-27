def how_many_times(message):
    # разбиваем строку на символы, добавляем в список
    characters = []
    for char in message:
        characters.append(char)

    # ставим счетчик нажатий, в цикле перебираем элементы списка
    times = 0
    for x in characters:
        x = ord(x)

        # если значение в ASCII находится в требуемом диапазоне, увеличиваем счетчик нажатий
        if 97 <= x <= 122:
            times += x - 96

        # если в тексте есть пробел - ничего не добавляем к счетчику
        elif char == 32:
            pass

        # если значение в ASCII за пределами диапазона - вызываем ошибку значения
        else:
            raise ValueError("String must contain only lowercase a-z letters or spaces")

    return times


message = input("Введите сообщение (строчные буквы): ")
if not type(message) == str:
    raise TypeError("Input must be a string")

clicks = how_many_times(message)
print(f"Количество нажатий: {clicks}")
