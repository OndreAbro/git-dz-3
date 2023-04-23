# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def rec_sum(a, b):
    if b > 0:
        a = rec_sum(a + 1, b - 1)
    return a


try:
    a, b = map(int, input('Введите значения A и B: ').split())
    if a >= 0 and b >= 0:
        print(f'Сумма {a} и {b}:', rec_sum(a, b))
    else:
        raise ValueError
except ValueError:
    print('Некорректный ввод данных!')
