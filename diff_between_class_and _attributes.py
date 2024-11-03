class House:
    houses_history = []         # создаём атрибут houses_history = []

    def __new__(cls, *args):
        instance = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])     # Название здания передается в первом аргументе
        return instance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __repr__(self):
        return f'{self.name} с {self.floors} этажами'

    def __del__(self):
        print(f'"{self.name}" снесён, но он останется в истории')


# print(House.houses_history)
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
