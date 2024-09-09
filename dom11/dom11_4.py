from math import pi


class Sphere:
    def __init__(self, rad=1, x=0, y=0, z=0):
        self.rad = rad
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4 * pi * self.rad**3 / 3

    def get_square(self):
        return 4 * pi * self.rad**2

    def get_radius(self):
        return self.rad

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, rad):
        self.rad = rad

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, a, b, c):    # координаты искомой точки (a, b, c)
        # Вычисляем квадрат расстояния от точки до центра сферы
        distance_squared = (
                            (a - self.x) ** 2 + (b - self.y) ** 2 +
                            (c - self.z) ** 2
        )
        # Проверяем, меньше ли расстояние квадрата радиуса
        if distance_squared < self.rad ** 2:
            return True
        else:
            return False


obj = Sphere(5, 1, 2, 3)
print(obj.get_volume())
print(obj.get_square())
print(obj.get_radius())
print(obj.set_radius(8))
print(obj.set_center(4, 5, 6))
print(obj.is_point_inside(7, 3, 8))


