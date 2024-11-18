from typing import List, Dict, Tuple, Union

class WordsFinder:
    """Класс для поиска слов в файлах."""

    def __init__(self, *file_names: str) -> None:
        """Инициализирует объект WordsFinder."""
        self.file_names: Tuple[str, ...] = file_names


    def get_all_words(self) -> Dict[str, List[str]]:
        """Возвращает словарь со словами из каждого файла."""
        all_words: Dict[str, List[str]] = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - '] # для split

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    text = f.read().lower()
                    for char in punctuation: # удаление пунктуации
                        text = text.replace(char, '')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words


    def find(self, word: str) -> Dict[str, Union[int, None]]:
        """Находит первое вхождение слова в каждом файле."""
        result: Dict[str, Union[int, None]] = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            try:
                result[file_name] = words.index(word) + 1 # первое вхождение, +1 так как индексация начинается с 0
            except ValueError:
                result[file_name] = None # если слово не найдено
        return result

    def count(self, word: str) -> Dict[str, int]:
        """Подсчитывает количество вхождений слова в каждом файле."""

        result: Dict[str, int] = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result




# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
