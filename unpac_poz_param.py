# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()                              # Вызов без аргументов
print_params(a = 10)                        # Один аргумент
print_params(10, b = 'test')             # Два аргумента
print_params(10, 'test', c = False)     # Три аргумента
print_params(b = 25)                        # Именованный аргумент
print_params(c = [1, 2, 3])                 # Именованный аргумент
print()

# 2.Распаковка параметров:
values_list = [3.14, 'pi', (1, 2, 3)]
values_dict = {'a': "словарь", 'b': 200, 'c': [4, 5, 6]}

print_params(*values_list)
print_params(**values_dict)
print()

# 3.Распаковка + отдельные параметры:
values_list_2 = [777, True]
print_params(*values_list_2, 42)    # Распаковка списка и дополнительный аргумент
print_params(*values_list_2, c = 42)    # Распаковка списка и именованный
                                        # аргумент

#Дополнительный пример: распаковка частично
print_params(1, *values_list_2[1:], c = False) # первый элемент - 1,
                                                # b распаковывается из values_list_2 (начиная со второго элемента),
                                                # с задан явно