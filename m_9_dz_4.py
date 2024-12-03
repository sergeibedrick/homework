first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

print(result)



def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')
    return write_everything


write = get_advanced_writer('result.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice

class MysticBall:
    def __init__(self, *words):
        # Инициализация атрибута words с переданными строками
        self.words = words

    def __call__(self):
        # Случайный выбор слова из коллекции words
        return choice(self.words)

# Пример использования класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Определенно', 'Не знаю',
                        'Возможно', 'Вряд ли', 'Вероятно', 'Вероятнее всего', 'Вероятно нет')
print(first_ball())
print(first_ball())
print(first_ball())