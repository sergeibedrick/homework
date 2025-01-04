import unittest
from unittest.suite import TestSuite

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
            for participant in list(self.participants): # итерируемся по копии списка
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant) # удаляем из оригинального списка

        return finishers


def freeze_tests(cls):
    """Декоратор для пропуска тестов в замороженном TestCase."""
    is_frozen = getattr(cls, 'is_frozen', False)  # Берем атрибут is_frozen, если он есть, иначе False

    for name, method in list(cls.__dict__.items()):
        if name.startswith('test_') and callable(method):
            if is_frozen:

                def skipped_test(self, *args, **kwargs):
                    raise unittest.SkipTest('Тесты в этом кейсе заморожены')
                setattr(cls, name, skipped_test)

    return cls

@freeze_tests
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для управления заморозкой

    def test_walk(self):
        """Проверяет метод walk."""
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """Проверяет метод run."""
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        """Проверяет методы run и walk с разными объектами."""
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


@freeze_tests
class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self) -> None:
        """Настройка перед каждым тестом."""
        self.tournament: Tournament = Tournament('distance')
        self.first_participant_name: str = 'John'
        self.second_participant_name: str = 'Mike'

    def test_first_tournament(self):
        """Проверка первого участника."""
        result: str = self.tournament.start_tournament(
            [self.first_participant_name, self.second_participant_name])
        self.assertEqual(self.first_participant_name, result)


    def test_second_tournament(self):
        """Проверка второго участника."""
        result: str = self.tournament.start_tournament(
            [self.second_participant_name, self.first_participant_name])
        self.assertEqual(self.second_participant_name, result)

    def test_third_tournament(self):
        """Проверка третьего участника."""
        result: str = self.tournament.start_tournament(
            [self.second_participant_name, self.second_participant_name])
        self.assertEqual(self.second_participant_name, result)


if __name__ == '__main__':
    # Динамический импорт в зависимости от текущего файла
    if __file__.endswith('suite_12_3.py'):  # Если это suite_12_3.py
        suite = TestSuite() # в файле suite_12_3.py добавляем TestSuite()
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest)
        suite.addTests(tests)

        tests = unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest)
        suite.addTests(tests)

        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)