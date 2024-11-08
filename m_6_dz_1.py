class Animal:
    """Родительский класс для животных."""
    alive: bool = True
    fed: bool = False

    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self, food: 'Plant') -> None:
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    """Родительский класс для растений."""
    edible: bool = False
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


class Mammal(Animal):
    """Класс млекопитающих."""
    pass


class Predator(Animal):
    """Класс хищников."""
    pass


class Flower(Plant):
    """Класс цветов."""
    pass


class Fruit(Plant):
    """Класс фруктов."""
    edible = True


# Пример использования
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

