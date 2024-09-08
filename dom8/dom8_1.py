def calculator_imt():
    try:
        weight = float(input("Введите Ваш вес в кг: "))
        height = float(input("Введите Ваш рост в метрах: "))
        if weight <= 0 or height <= 0:
            raise ValueError("Вес и рост должны быть положительными числами!")
        if weight > 650 or height > 3:
            raise ValueError("Будьте внимательнее при вводе значений!\n"
                             "Возможно Вы ввели значения не в тех единицах\n"
                             "или не в том порядке.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return

    try:
        imt = float(weight / height**2)
        if imt > 110:    # Cамый высокий ИМТ оценивался в 105,2 (кг/м²)
            raise ValueError("Слишком большое значение ИМТ. "
                             "Рассчет произведен по некорректным данным")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    if imt < 16:
        return f"Значение ИМТ {imt:.2f}, выраженный дефицит массы тела"
    elif 16 <= imt < 18.5:
        return f"Значение ИМТ {imt:.2f}, недостаточная  масса тела"
    elif 18.5 <= imt < 25:
        return f"Значение ИМТ {imt:.2f}, вес в норме"
    elif 25 <= imt < 30:
        return f"Значение ИМТ {imt:.2f}, избыточная масса тела"
    elif 30 <= imt < 35:
        return f"Значение ИМТ {imt:.2f}, ожирение первой степени"
    elif 35 <= imt < 40:
        return f"Значение ИМТ {imt:.2f}, ожирение второй степени"
    else:
        return f"Значение ИМТ {imt:.2f}, ожирение третьей степени (морбидное)"


print(calculator_imt())
git