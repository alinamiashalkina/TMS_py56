"""
ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● eat(meal, value) – может принимать в meal только ”nectar”
или “grass”. Если съедает нектар, то value вычитается из
части слона, пчеле добавляется. Иначе – наоборот. Не
может увеличиваться больше 100 и уменьшаться меньше 0.
"""


class BeeElephant:
    def __init__(self, bee: int, eleph: int):
        self.bee = bee
        self.eleph = eleph

    def fly(self) -> bool:
        return self.bee >= self.eleph

    def trumpet(self):
        if self.bee <= self.eleph:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal: str, value: int):
        if meal == "nectar":
            if self.eleph >= value:
                self.eleph -= value
                self.bee += value
                if self.bee > 100:
                    self.bee = 100
                if self.eleph < 0:
                    self.eleph = 0
                print(f"ПчелоСлон съел {value} нектара. "
                      f"Теперь часть пчелы = {self.bee}, "
                      f"часть слона = {self.eleph}")
            else:
                print(f"Слишком мало слона, чтобы съесть {value} нектара")
        elif meal == "grass":
            if self.bee >= value:
                self.bee -= value
                self.eleph += value
                if self.eleph > 100:
                    self.eleph = 100
                if self.bee < 0:
                    self.bee = 0
                print(f"ПчелоСлон съел {value} травы. "
                      f"Теперь часть пчелы = {self.bee}, "
                      f"часть слона = {self.eleph}")
            else:
                print(f"Слишком мало пчелы, чтобы съесть {value} травы")
        else:
            print(f"ПчелоСлон {meal} не ест, "
                  f"предложите ему nectar или grass ")


my_bee_el = BeeElephant(20, 30)

print(my_bee_el.fly())
print(my_bee_el.trumpet())
my_bee_el.eat("nectar", 10)
my_bee_el.eat("grass", 100)
my_bee_el.eat("honey", 5)

