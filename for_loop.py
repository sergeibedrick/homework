numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
special = []  # список особых чисел (в данном случае, для 1)

for num in numbers:
    if num == 1:
        special.append(num)
        continue

    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print("Простые числа:", primes)
print("Непростые числа:", not_primes)
print("Особые числа:", special)