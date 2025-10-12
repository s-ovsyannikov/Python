def is_palindrome(string):
    """Обычная проверка палиндрома."""
    string.lower()

    if string == string[::-1]:
        return True
    else:
        return False


def is_palindrome_recursive(string):
    """Рекурсивная проверка палиндрома."""
    string.lower()

    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome_recursive(string[1:-1])


# Получение ввода от пользователя
string_input = input("Введите строку: ")

# Вывод результатов
print("Обычный метод:", is_palindrome(string_input))
print("Рекурсивный метод:", is_palindrome_recursive(string_input))
