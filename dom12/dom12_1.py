from dataclasses import dataclass

@dataclass
class Product:
    __prod_name: str
    __shop_name: str
    __prod_cost: float

    @property
    def prod_name(self):
        return self.__prod_name

    @property
    def shop_name(self):
        return self.__shop_name

    @property
    def prod_cost(self):
        return self.__prod_cost

    def __str__(self) -> str:
        """
        возвращает информацию о товаре в читабельном формате
        """
        return (f"Название товара: {self.prod_name}, "
                f"Название магазина: {self.shop_name}, "
                f"Стоимость: {self.prod_cost:.2f}"
                )
    # переопределим метод __repr__ для читабельности
    # при работе со списками товаров в дальнейшем
    def __repr__(self) -> str:
        """
        при выводе списка товаров возвращает информацию о товаре
        в читабельном формате
        """
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__prod_cost + other.__prod_cost
        else:
            raise TypeError("Невозможно выполнить сложение")


class Storehouse:
    def __init__(self):
        self.__products = []

    @property
    def products(self):
        """
        возвращает копию списка товаров, чтобы избежать изменений вне класса
        """
        return list(self.__products)

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
        else:
            raise TypeError("В список товаров можно добавить только товары")

    def get_product_by_index(self, index):
        if 0 <= index < len(self.__products):
            return self.__products[index]
        else:
            raise IndexError("Индекс не указывает ни на один товар")

    def __getitem__(self, index):
        """
        обеспечивает доступ к товарам по индексу
        """
        return self.get_product_by_index(index)

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.prod_name == name:
                return product
        else:
            print(f"Товар с именем {name} не найден")
            return None

    def sort_by_name(self):
        return sorted(self.__products, key=lambda product: product.prod_name)

    def sort_by_shop(self):
        return sorted(self.__products, key=lambda product: product.shop_name)

    def sort_by_cost(self):
        return sorted(self.__products, key=lambda product: product.prod_cost)


prod1 = Product("phone", "5element", 799.00)
prod2 = Product("notebook", "21vek", 1999.99)
prod3 = Product("tablet", "amd", 1200.20)
store = Storehouse()
store.add_product(prod1)
store.add_product(prod2)
store.add_product(prod3)

# посмотреть полученный список товаров на складе
print(store.products)


# вывод информации о товаре со склада по индексу
print(store[2])

# вывод информации о товаре со склада по имени товара
print(store.get_product_by_name("phone"))
# print(store.get_product_by_name("car"))

# сортировка товаров по названию, по магазину и по цене
print(store.sort_by_name())
print(store.sort_by_shop())
print(store.sort_by_cost())

# перегруженная операция сложения товаров по цене
print(f"Сумма к оплате при покупке телефона и ноутбука составит "
      f"{prod1 + prod2}"
      )


