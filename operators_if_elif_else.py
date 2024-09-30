# Ввод трех целых чисел
numbers = list(map(int, input('Введите три целых числа через пробел: ').split()))

# Преобразование списка в множество
unique_numbers = set(numbers)

# Проверка количества уникальных значений
if len(unique_numbers) == 1:
    result = 3  # Все числа равны
elif len(unique_numbers) == 2:
    result = 2  # Два числа равны
else:
    result = 0  # Все числа разные

# Вывод результата
print(result)

# мне так больше нравится
result = 3 if len(unique_numbers) == 1 else 2 if len(unique_numbers) == 2 \
    else 0
print(result)