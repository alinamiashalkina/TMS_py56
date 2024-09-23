"""
Реализовать программу для вывода
последовательности чисел Фибоначчи до определённого
числа в последовательности. Номер числа, до которого нужно
выводить, задаётся пользователем с клавиатуры. Для
реализации последовательности использовать генераторную
функцию
"""

def fibonacci(i):
    a = 0
    b = 1
    for n in range(i):
        yield a
        a, b = b, a + b


try:
    i = int(input("Введите количество чисел, которое вы хотите увидеть "
                  "в последовательности Фибоначчи: "
                  ))
    if i < 0:
        print("Введите положительное целое число")
    else:
        print(f"Последовательность Фибоначчи из {i} чисел:")
        print(list(fibonacci(i)))

except ValueError:
    print("Ошибка ввода. Введенное значение должно быть целым числом")
