"""
Паттерн «Строитель»
● Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
● Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
● Создайте класс PizzaDirector, который принимает
экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza.
"""
from abc import ABC, abstractmethod


class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("Сыр")
        if self.pepperoni:
            ingredients.append("Пепперони")
        if self.mushrooms:
            ingredients.append("Грибы")
        if self.onions:
            ingredients.append("Лук")
        if self.bacon:
            ingredients.append("Бекон")
        return (f"Ваша пицца: размер {self.size} см, ингредиенты: "
                f"{', '.join(ingredients)}"
                )


class PizzaBuilder(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_pepperoni(self):
        pass

    @abstractmethod
    def add_mushrooms(self):
        pass

    @abstractmethod
    def add_onions(self):
        pass

    @abstractmethod
    def add_bacon(self):
        pass


class MargaritaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def get_size(self):
        while True:
            try:
                self.pizza.size = int(input("Введите размер пиццы в см: "))
                # ограничим размер пиццы 95 см
                if self.pizza.size <= 0 or self.pizza.size > 95:
                    print("Вы указали неверный размер")
                else:
                    break
            except ValueError:
                print("Введите положительное целое число")

    def add_cheese(self):
        self.pizza.cheese = True

    def add_pepperoni(self):
        pass

    def add_mushrooms(self):
        pass

    def add_onions(self):
        pass

    def add_bacon(self):
        pass

    def get_pizza(self):
        return self.pizza


class PepperoniBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def get_size(self):
        while True:
            try:
                self.pizza.size = int(input("Введите размер пиццы в см: "))
                # ограничим размер пиццы 95 см
                if self.pizza.size <= 0 or self.pizza.size > 95:
                    print("Вы указали неверный размер")
                else:
                    break
            except ValueError:
                print("Введите положительное целое число")

    def add_cheese(self):
        self.pizza.cheese = True

    def add_pepperoni(self):
        self.pizza.pepperoni = True

    def add_mushrooms(self):
        pass

    def add_onions(self):
        pass

    def add_bacon(self):
        pass

    def get_pizza(self):
        return self.pizza


class ChefPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def get_size(self):
        while True:
            try:
                self.pizza.size = int(input("Введите размер пиццы в см: "))
                # ограничим размер пиццы 95 см
                if self.pizza.size <= 0 or self.pizza.size > 95:
                    print("Вы указали неверный размер")
                else:
                    break
            except ValueError:
                print("Введите положительное целое число")

    def add_cheese(self):
        self.pizza.cheese = True

    def add_pepperoni(self):
        self.pizza.pepperoni = True

    def add_mushrooms(self):
        self.pizza.mushrooms = True

    def add_onions(self):
        self.pizza.onions = True

    def add_bacon(self):
        self.pizza.bacon = True

    def get_pizza(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder

    def make_pizza(self):
        self._builder.get_size()
        self._builder.add_cheese()
        self._builder.add_pepperoni()
        self._builder.add_mushrooms()
        self._builder.add_onions()
        self._builder.add_bacon()

    def pizza_for_you(self):
        return self._builder.get_pizza()


margarita_builder = MargaritaBuilder()
director = PizzaDirector(margarita_builder)
director.make_pizza()
pizza_margarita = director.pizza_for_you()
print(pizza_margarita)

pepperoni_builder = PepperoniBuilder()
director = PizzaDirector(pepperoni_builder)
director.make_pizza()
pizza_pepperoni = director.pizza_for_you()
print(pizza_pepperoni)

chef_pizza_builder = ChefPizzaBuilder()
director = PizzaDirector(chef_pizza_builder)
director.make_pizza()
chef_pizza = director.pizza_for_you()
print(chef_pizza)
