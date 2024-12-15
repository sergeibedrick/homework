import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return len(all_data)  # Возвращаем длину списка вместо самого списка


def linear_execution(filenames):
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейное выполнение: {end_time - start_time:.6f} секунд")


def multiprocess_execution(filenames):
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное выполнение: {end_time - start_time:.6f} секунд")


if __name__ == '__main__':
    filenames = [f'./Files/file {i}.txt' for i in range(1, 5)]

    # Линейное выполнение
    linear_execution(filenames)

    # Многопроцессное выполнение
    multiprocess_execution(filenames)