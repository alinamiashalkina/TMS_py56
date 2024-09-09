class Math:

    def addition(self, a, b):
        print(f"a + b = {a+b}")

    def subtraction(self, a, b):
        print(f"a - b = {a - b}")

    def multiplication(self, a, b):
        print(f"a * b = {a * b}")

    def division(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("На 0 делить нельзя!")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")
            return
        print(f"a / b = {a / b:.2f}")


math_obj = Math()
math_obj.addition(125, 5)
math_obj.subtraction(98, 17)
math_obj.multiplication(55, 82)
math_obj.division(100, 13)
math_obj.division(100, 0)

# ниже то же самое с применением @staticmethod

""" 
Предупреждение "Method 'addition' may be 'static'" означает, что метод, 
который вы определили в классе, не использует ни одно из свойств экземпляра 
и поэтому может быть определен как статический метод. Статические методы не 
требуют класса или экземпляра для вызова и могут быть вызваны непосредственно 
из класса.
"""
class Math:
    @staticmethod
    def addition(a, b):
        print(f"a + b = {a+b}")

    @staticmethod
    def subtraction(a, b):
        print(f"a - b = {a - b}")

    @staticmethod
    def multiplication(a, b):
        print(f"a * b = {a * b}")

    @staticmethod
    def division(a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("На 0 делить нельзя!")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")
            return
        print(f"a / b = {a / b:.2f}")



Math.addition(125, 5)
Math.subtraction(98, 17)
Math.multiplication(55, 82)
Math.division(100, 13)
Math.division(100, 0)
