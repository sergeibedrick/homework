def is_prime(func):
    def wrapper(*args):
        # Вызываем оригинальную функцию
        result = func(*args)

        # Проверяем, является ли результат простым числом
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")

        # Возвращаем результат оригинальной функции
        return result

    return wrapper


@is_prime
def sum_three(a : int, b : int, c : int):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)

print()

result = sum_three(3, 3, 6)
print(result)