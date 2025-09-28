# калькулятор простых операций


def sum(number_1, number_2):
    sum_num = number_1 + number_2
    return sum_num


def diff(number_1, number_2):
    diff_num = number_1 - number_2
    return diff_num


def mul(number_1, number_2):
    mul_num = number_1 * number_2
    return mul_num


def div(number_1, number_2):
    div_num = number_1 / number_2
    return div_num


number_1, number_2 = int(input()), int(input())
print("Сумма:", sum(number_1, number_2))
print("Разность:", diff(number_1, number_2))
print("Произведение:", mul(number_1, number_2))
print("Деление:", div(number_1, number_2))
