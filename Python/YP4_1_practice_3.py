def factorial(n):
    """Возвращает n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial.__doc__)  # 'Возвращает n!'
help(factorial)
print(type(factorial))  # <class 'function'>
