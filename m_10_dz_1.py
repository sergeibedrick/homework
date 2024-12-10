from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Измерение времени выполнения функций
start_time = datetime.now()

# Вызовы функции write_words с заданными аргументами
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time = datetime.now()
print(f"Время выполнения функций: {end_time - start_time}")

# Измерение времени выполнения потоков
start_time_threads = datetime.now()

# Создание потоков для вызова функции write_words с заданными аргументами
threads = []
threads.append(Thread(target=write_words, args=(10, "example5.txt")))
threads.append(Thread(target=write_words, args=(30, "example6.txt")))
threads.append(Thread(target=write_words, args=(200, "example7.txt")))
threads.append(Thread(target=write_words, args=(100, "example8.txt")))

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = datetime.now()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads}")