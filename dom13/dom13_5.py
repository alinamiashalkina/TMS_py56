"""
Паттерн «Стратегия»
● Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
● Создайте несколько классов, каждый реализует
определенную стратегию математической операции,
например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute, который
принимает два числа и выполняет соответствующую
операцию.
● Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate,
который выполняет операцию с помощью текущей стратегии.
"""

from abc import ABC, abstractmethod


# интерфейс стратегии
class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int):
        pass


# конкретная стратегия сложения
class AdditionStrategy(Strategy):
    def execute(self, a: int, b: int):
        return a + b


# конкретная стратегия вычитания
class SubtractionStrategy(Strategy):
    def execute(self, a: int, b: int):
        return a - b


# конкретная стратегия умножения
class MultiplicationStrategy(Strategy):
    def execute(self, a: int, b: int):
        return a * b


# конкретная стратегия деления
class DivisionStrategy(Strategy):
    def execute(self, a: int, b: int):
        try:
            return a / b
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
            return None


# контекст выполнения
class Calculator:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def calculate(self, a: int, b: int):
        return self.strategy.execute(a, b)


calculator = Calculator(AdditionStrategy())
print(calculator.calculate(4, 2))

calculator.set_strategy(SubtractionStrategy())
print(calculator.calculate(4, 2))

calculator.set_strategy(MultiplicationStrategy())
print(calculator.calculate(4, 2))

calculator.set_strategy(DivisionStrategy())
print(calculator.calculate(4, 2))

calculator.set_strategy(DivisionStrategy())
print(calculator.calculate(4, 0))
