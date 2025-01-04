import unittest
from unittest.suite import TestSuite
from tests_12_3 import RunnerTest, TournamentTest # импортируем тесты из tests_12_3.py


if __name__ == '__main__':
    suite = TestSuite()
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest)
    suite.addTests(tests)

    tests = unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest)
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)