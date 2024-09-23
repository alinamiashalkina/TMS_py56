"""
Паттерн «Фабричный метод»
● Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
● Создайте классы Dog и Cat, которые наследуют от Animal
и реализуют метод speak.
● Создайте класс AnimalFactory, который использует
паттерн «Фабричный метод» для создания экземпляра
Animal. Этот класс должен иметь метод create_animal,
который принимает строку («dog» или «cat») и возвращает
соответствующий объект (Dog или Cat).
"""

from abc import ABC, abstractmethod

# интерфейс животного
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# конкретное животное
class Dog(Animal):
    def speak(self):
        print("Гав-гав")


# конкретное животное
class Cat(Animal):
    def speak(self):
        print("Мяу-мяу")


# фабричный метод по созданию животного
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self, animal_type: str) -> Animal:
        pass


# конкретный создатель - собачья фабрика
class DogFactory(AnimalFactory):
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        else:
            print(f"Эта фабрика не создает животных типа {animal_type}")


# конкретный создатель - кошачья фабрика
class CatFactory(AnimalFactory):
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "cat":
            return Cat()
        else:
            print(f"Эта фабрика не создает животных типа {animal_type}")


dog_factory = DogFactory()
my_dog = dog_factory.create_animal("dog")
my_dog.speak()

cat_factory = CatFactory()
my_cat = cat_factory.create_animal("cat")
my_cat.speak()


dog_factory = DogFactory()
my_dog = dog_factory.create_animal("cow")
