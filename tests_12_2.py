import unittest
from typing import Dict

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

class TournamentTest(unittest.TestCase):
    all_results: Dict[int, str] = {} # атрибут класса для хранения результатов

    @classmethod
    def setUpClass(cls) -> None:
        """Создаем словарь для хранения результатов."""

        print("setUpClass") # для наглядности


    def setUp(self) -> None:
        """Создаем бегунов перед каждым тестом."""
        self.usain: Runner = Runner("Усэйн", speed=10)
        self.andrey: Runner = Runner("Андрей", speed=9)
        self.nick: Runner = Runner("Ник", speed=3)


    def test_usain_vs_nick(self) -> None:
        """Тест забега Усэйн против Ник."""
        tournament: Tournament = Tournament(90, self.usain, self.nick)
        result: Dict[int, Runner] = tournament.start()
        last_place: int = max(result.keys())

        TournamentTest.all_results[1] = result #  сохраняем результаты
        # теста
        self.assertEqual(result[last_place].name, "Ник")  # Ник должен быть последним




    def test_andrey_vs_nick(self) -> None:
        """Тест забега Андрей против Ник."""
        tournament: Tournament = Tournament(90, self.andrey, self.nick)
        result: Dict[int, Runner] = tournament.start()
        last_place: int = max(result.keys())

        TournamentTest.all_results[2] = result #  сохраняем результаты теста

        self.assertEqual(result[last_place].name, "Ник") # Ник должен быть последним



    def test_usain_andrey_nick(self):
        """Тест забега Усэйн, Андрей и Ник."""
        tournament: Tournament = Tournament(90, self.usain, self.andrey, self.nick)

        result: Dict[int, Runner] = tournament.start()
        last_place: int = max(result.keys())

        TournamentTest.all_results[3] = result #  сохраняем результаты теста

        self.assertEqual(result[last_place].name, "Ник")  # Ник должен быть последним


    @classmethod
    def tearDownClass(cls) -> None:
        """Выводим результаты всех тестов."""
        print("tearDownClass") # для наглядности

        for key, value in cls.all_results.items():
            print(value)




if __name__ == '__main__':
    unittest.main()