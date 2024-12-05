def all_variants(text):
    length = len(text)
    # Внешний цикл для начального индекса
    for start in range(length):
        # Внутренний цикл для конечного индекса
        for end in range(start + 1, length + 1):
            yield text[start:end]  # Возвращаем подстроку от start до end

# Пример вызова функции и итерации
a = all_variants("abc")
for i in a:
    print(i)