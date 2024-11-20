import os
import time

# Указываем каталог для обхода
directory = "."

# Используем os.walk для обхода каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматируем время в удобочитаемый формат
        formatted_time = time.strftime("%d.%m.%Y %H:%M",
                                       time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: '
            f'{filesize} байт, Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')