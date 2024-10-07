# Сначала создадим глобальную переменную
calls = 0

# создадим функцию, которая будет увеличивать значение переменной calls при
# каждом вызове
def count_calls():
    global calls
    calls += 1

# создадим функцию, которая принимает строку и возвращает кортеж
def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

# создадим функцию, которая принимает строку и список, проверяя,
# содержится ли строка в списке
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (s.lower() for s in list_to_search)

# Вызовы функций
result1 = string_info('Hello Python Developers')
result2 = string_info('Python Programming')
contains_check1 = is_contains('hello', ['Hello', 'world'])
contains_check2 = is_contains('java', ['Python', 'Ruby'])

# Вывод результата вызовов и значения calls
print(result1)
print(result2)
print(contains_check1)
print(contains_check2)
print(calls)

