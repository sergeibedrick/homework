def apply_all_func(int_list, *functions):
    """Применяет переданные функции к списку чисел."""
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

