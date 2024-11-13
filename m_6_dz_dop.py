import math

class Figure:
    """Базовый класс для геометрических фигур."""
    sides_count = 0

    def __init__(self, color, *sides):
        """Инициализирует фигуру."""
        self.__sides = [1] * self.sides_count
        self.__color = list(color)
        self.filled = False
        if len(sides) == self.sides_count:
            self.set_sides(*sides)


    def get_color(self):
        """Возвращает цвет фигуры."""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """Проверяет корректность RGB цвета."""
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        """Устанавливает цвет фигуры."""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        """Проверяет корректность сторон."""
        return (len(new_sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in new_sides))

    def get_sides(self):
        """Возвращает стороны фигуры."""
        return self.__sides

    def __len__(self):
        """Возвращает периметр фигуры."""
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    """Класс, представляющий круг."""
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        """Возвращает площадь круга."""
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    """Класс, представляющий треугольник."""
    sides_count = 3

    def get_square(self):
        """Возвращает площадь треугольника."""
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    """Класс, представляющий куб."""
    sides_count = 12

    def __init__(self, color, *sides):
        """Инициализирует куб."""
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.set_sides(*([sides[0]] * self.sides_count))

    def get_volume(self):
        """Возвращает объем куба."""
        return self.get_sides()[0] ** 3

# Код для проверки
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга)
print(len(circle1))

# Проверка объёма (куба)
print(cube1.get_volume())





