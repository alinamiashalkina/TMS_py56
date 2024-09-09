class Car:

    def __init__(self, color, type_, year):
        self.color = color
        self.type_ = type_
        self.year = year


    def start_car(self):
        print("Автомобиль заведён")

    def stop_car(self):
        print("Автомобиль заглушен")

    def color_car(self, color):
        self.color = color
        print(f"Цвет автомобиля: {color}")

    def type_car(self, type_):
        self.type_ = type_
        print(f"Тип автомобиля: {type_}")

    def year_car(self, year):
        self.year = year
        print(f"Год выпуска автомобиля: {year}")


my_car = Car("красный", "седан", "2000")
my_car.start_car()
my_car.color_car("фиолетовый")
my_car.type_car("внедорожник")
my_car.year_car("2023")
my_car.stop_car()
