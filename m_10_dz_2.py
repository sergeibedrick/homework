import threading
import time



class Knight(threading.Thread):
    """Класс рыцаря, сражающегося с врагами."""

    enemies: int = 100  # Общее количество врагов для всех рыцарей

    def __init__(self, name: str, power: int) -> None:
        """Инициализирует рыцаря."""
        super().__init__()
        self.name: str = name
        self.power: int = power
        self.days: int = 0

    def run(self):
        """Запускает поток сражения рыцаря."""

        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.days += 1
            time.sleep(1)
            Knight.enemies -= self.power  # уменьшаем общее количество врагов

            remaining_enemies = max(0, Knight.enemies)
            print(
                f"{self.name} сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание и запуск рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")