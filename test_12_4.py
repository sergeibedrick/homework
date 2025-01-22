import unittest
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для управления заморозкой

    def test_walk(self):
        """Проверяет метод walk с обработкой исключения."""
        try:
            runner = Runner("Walker", -1)  # Передаем отрицательное значение
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        """Проверяет метод run с обработкой исключения."""
        try:
            runner = Runner(123, 5)  # Передаем что-то кроме строки
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')

    def test_challenge(self):
        """Проверяет методы run и walk с разными объектами."""
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()


first = Runner('Вося', 10)
second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())