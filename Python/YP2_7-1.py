def calculate_months_to_threshold(start, rate, threshold):
    # ставим и обнуляем счетчики на кол-во месяцев и месячный прирост
    month_increase = 0
    month_qty = 0
    # проверяем, что стартовое значение не превышает пороговое, если превышает - возвращаем 0
    if start >= threshold:
        return 0

    # запускаем цикл, пока месячный прирост меньше порогового - идем по циклу, возвращаем кол-во месяцев до достижения порога
    while month_increase < threshold:
        month_increase = start + start * (rate / 100)
        month_qty += 1
        start = month_increase
        # выход из цикла при достижении кол-ва месяцев 1000
        if month_qty > 1000:
            break
    return month_qty


start = int(input("Введите начальное количество пользователей: "))
rate = float(input("Введите темп роста в процентах: "))
threshold = int(input("Введите пороговое значение: "))

if rate <= 0:
    raise ValueError("Growth rate must be greater than 0.")
elif start <= 0 or threshold <= 0:
    raise ValueError("Start and threshold must be positive numbers.")


months = calculate_months_to_threshold(start, rate, threshold)
print(f"Количество месяцев для достижения порога: {months}")
