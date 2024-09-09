class Soda:
    def __init__(self, taste=""):
        self.taste = taste

    def descript_soda(self):
        if self.taste:
            print(f"у тебя газировка со вкусом {self.taste}")
        else:
            print("у тебя обычная газировка")

apple_soda = Soda("яблоко")
apple_soda.descript_soda()

rasp_soda = Soda("малина")
rasp_soda.descript_soda()

simple_soda = Soda()
simple_soda.descript_soda()
