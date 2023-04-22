# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def rec_exponention(a, b):
    if b == 0:
        return 1
    else:
        if abs(b) > 1:
            a *= rec_exponention(a, abs(b) - 1)
        return a if b > 0 else 1 / a


try:
    a, b = map(int, input('Введите значения A и B: ').split())
    print(f'Результат возведения числа {a} в степень {b}:', rec_exponention(a, b))
except ValueError:
    print('Некорректный ввод данных!')