def count_elements(*args):
    number_sum = 0
    string_length_sum = 0

    def recursive_count(item):
        nonlocal number_sum, string_length_sum

        if isinstance(item, (int, float)):
            number_sum += item
        elif isinstance(item, complex):
            number_sum += item.real  # Учитываем только действительную часть комплексного числа
        elif isinstance(item, str):
            string_length_sum += len(item)
        elif isinstance(item, (list, tuple, set, dict)):
            if isinstance(item, dict):
                for key, value in item.items():
                    recursive_count(key)
                    recursive_count(value)
            else:
                for element in item:
                    recursive_count(element)

    for arg in args:
        recursive_count(arg)

    return number_sum, string_length_sum


# Входные данные (применение функции):
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_of_numbers, sum_of_string_lengths = count_elements(data_structure)
total = sum_of_numbers + sum_of_string_lengths

print(f"Сумма всех чисел: {sum_of_numbers}")
print(f"Сумма длин всех строк: {sum_of_string_lengths}")
print(f"Обшая сумма: {total} ")