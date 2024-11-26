def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            if isinstance(item, (int, float)):
                result += item
            else:
                raise TypeError
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple, str)):
        print('В numbers записан некорректный тип данных')
        return None

    sum_result, incorrect_count = personal_sum(numbers)

    try:
        average = sum_result / (len(numbers) - incorrect_count)
    except ZeroDivisionError:
        return 0

    return average


# Примеры вызова функции
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')