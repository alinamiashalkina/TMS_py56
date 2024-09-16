"""
Класс «Автобус». Класс содержит свойства:
● скорость
● максимальное количество посадочных мест
● максимальная скорость
● список фамилий пассажиров
● флаг наличия свободных мест
● словарь мест в автобусе
Методы:
● посадка и высадка одного или нескольких пассажиров
● увеличение и уменьшение скорости на заданное значение
● операции in, += и -= (посадка и высадка пассажира по
фамилии)
"""
from dataclasses import dataclass, field


@dataclass
class Bus:
    max_seats: int
    max_speed: int
    passengers: list = field(default_factory=list)
    seats: dict = field(init=False)    # значение не задается при инициализации
    speed: int = 0

    def __post_init__(self):
        self.seats = {i: None for i in range(1, self.max_seats + 1)}
        for i, passenger in enumerate(self.passengers):
            self.seats[i + 1] = passenger

    @property
    def available_seats(self) -> int:
        """Количество свободных мест """
        return self.max_seats - len(self.passengers)

    @property
    def has_available_seats(self) -> bool:
        """Флаг наличия свободных мест """
        return self.available_seats > 0

    def add_passenger(self, *new_passengers: str) -> int:
        """
        Добавляет одного или нескольких пассажиров, если есть свободные места
        """
        count_added = 0
        for passenger in new_passengers:
            if self.has_available_seats:
                # Находим первое свободное место
                for seat_number, smb_on_seat in self.seats.items():
                    if smb_on_seat is None:
                        self.seats[seat_number] = passenger
                        self.passengers.append(passenger)
                        count_added += 1
                        print(f"Пассажир {passenger} "
                              f"сел на место {seat_number}"
                              )
                        break
            else:
                print("В автобусе нет свободных мест!")
                break  # Прерываем, если мест больше нет
        print(f"В автобус село {count_added} пассажиров")
        return count_added

    def remove_passenger(self, *passengers: str) -> int:
        """ Удаляет пассажиров по фамилии """
        count_remove = 0
        for passenger in passengers:
            for seat_number, smb_on_seat in self.seats.items():
                if smb_on_seat == passenger:
                    # Освобождаем место
                    self.seats[seat_number] = None
                    # Удаляем из списка пассажиров
                    self.passengers.remove(passenger)
                    count_remove += 1
                    print(f"Пассажир {passenger} "
                          f"вышел, место {seat_number} свободно"
                          )
                    break
            else:
                print(f"Пассажир {passenger} не найден")
        print(f"Из автобуса вышло {count_remove} пассажиров")
        return count_remove

    def increase_speed(self, value: int):
        """
        Увеличивает скорость на заданное значение,
        не превышая максимальную
        """
        if self.speed+value >= self.max_speed:
            self.speed = self.max_speed
            print("Достигнута максимальная скорость автобуса")
        else:
            self.speed += value

    def decrease_speed(self, value: int):
        """Уменьшает скорость на заданное значение, не меньше нуля."""
        if self.speed - value <= 0:
            self.speed = 0
            print("Автобус остановлен")
        else:
            self.speed -= value

    # переопределяем метод для корректного использования оператора in
    def __contains__(self, passenger: str) -> bool:
        """Проверяет, есть ли пассажир в списке"""
        return passenger in self.passengers

    def __iadd__(self, passenger: str) -> 'Bus':
        """Добавление пассажира с помощью оператора +="""
        self.add_passenger(passenger)
        return self

    def __isub__(self, passenger: str) -> 'Bus':
        """Высадка пассажира с помощью оператора -="""
        self.remove_passenger(passenger)
        return self

    def __str__(self) -> str:
        return (f"Bus(max_seats={self.max_seats}, max_speed={self.max_speed}, "
                f"current_speed={self.speed}, passengers={self.passengers}, "
                f"seats={self.seats})"
                )


bus = Bus(8, 100, passengers=["Ivanov", "Petrov", "Meshalkina"])
print(bus)

print(bus.has_available_seats)
bus.add_passenger("Pavlov", "Sergeev")
print(bus)

bus.increase_speed(30)
print(bus)

bus.decrease_speed(40)
print(bus)

bus -= "Pavlov"
bus += "Pupkin"
print(bus)

print("Pupkin" in bus)
