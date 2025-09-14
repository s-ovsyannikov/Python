def to_fahrenheit(celsius):
    return round(celsius * (9 / 5) + 32)


def to_kelvin(celsius):
    return round(celsius + 273.15)


celsius = float(input("Введите температуру в Цельсиях: "))
print("Фаренгейт:", to_fahrenheit(celsius))
print("Кельвин:", to_kelvin(celsius))
