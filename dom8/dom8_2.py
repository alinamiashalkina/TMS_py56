def calculator():
    try:
        a, b = map(float, input("Введите два числа через пробел: ").split())
        operation = input("Введите операцию, которую следует выполнить "
                          "(+, -, *, /): "
                          )
        if operation not in ["+", "-", "*", "/"]:
            raise ValueError("Введен неверный оператор")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return
    if operation == "+":
        result = a+b
        return f"{a} + {b} = {result:.2f}"
    elif operation == "-":
        result = a-b
        return f"{a} - {b} = {result:.2f}"
    elif operation == "*":
        result = a*b
        return f"{a} * {b} = {result:.2f}"
    elif operation == "/":
        try:
            if b == 0:
                raise ZeroDivisionError("На ноль делить нельзя!")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")
            return
        result = a/b
        return f"{a}/{b} = {result:.2f}"


print(calculator())
