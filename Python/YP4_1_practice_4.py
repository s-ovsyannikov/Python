def factorial(n):
    """Возвращает n!"""
    return 1 if n < 2 else n * factorial(n - 1)

# Присваиваем функцию переменной
fact = factorial

# Проверяем, что переменная fact ссылается на ту же функцию
print(fact)         # <function factorial at ...>
print(fact(5))      # 120

# Используем функцию factorial с map
result = map(factorial, range(11))
print(result)       # <map object at ...> — это ленивый итератор

# Преобразуем результат в список
print(list(result)) # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800] 