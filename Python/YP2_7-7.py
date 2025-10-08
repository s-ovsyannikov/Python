def triangle_type(trian1, trian2, trian3):
    # обрабатываем исключения
    if a <= 0 or b <= 0 or c <= 0:
        return "Невозможно"

    if (a + b) > c and (a + c) > b and (b + c) > a:
        if a == b == c:
            return "Равносторонний"
        elif a == b or a == c or b == c:
            return "Равнобедренный"
        else:
            return "Разносторонний"
    else:
        return "Невозможно"


a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

result = triangle_type(a, b, c)
print(f"Тип треугольника: {result}")
