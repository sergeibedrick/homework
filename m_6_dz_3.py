import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0  # Базовая степень опасности

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Координаты в пространстве
        self.speed = speed

    def move(self, dx, dy, dz):
        # Изменение координат с учетом скорости
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed

        # Проверка на глубину для координаты z
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z

    def get_cords(self):
        return f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True  # У птиц есть клюв

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)  # Случайное количество яиц от 1 до 4
        print(f"Here are(is) {eggs_count} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3  # Степень опасности для водных животных

    def dive_in(self, dz):
        # Изменяем координату z с учетом скорости и модуля dz
        new_z = self._cords[2] - abs(dz) * (self.speed / 2)
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8  # Высокая степень опасности для ядовитых животных


class Duckbill(PoisonousAnimal, AquaticAnimal,
               Bird):  # Изменяем порядок наследования
    sound = "Click-click-click"  # Звук утконоса

    def __init__(self, speed):
        super().__init__(speed)  # Инициализация родительского класса

    def speak(self):
        print(self.sound)  # Утконос издает звук


# Пример работы программы
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
print(db.get_cords())

db.dive_in(6)
print(db.get_cords())

db.lay_eggs()

print(Duckbill.mro()) # MRO проверка наследования (для себя)