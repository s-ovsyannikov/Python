def calculate_bmi(weight, height):
    return weight / height**2


def get_bmi_category(bmi):
    if bmi < 25:
        return "Норма, жить можно"
    elif bmi > 30:
        return "Ожирение"
    else:
        return "Избыточный вес, стоит задуматься"


weight = float(input("Введите вес (кг):"))
if weight <= 0:
    print("Вес не может быть нулевым или отрицательным")
height = float(input("Введите рост (м):"))
if height <= 0:
    print("Рост не может быть нулевым или отрицательным")

bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

print("Ваш ИМТ: ", round(bmi, 2))
print("Категория: ", category)
