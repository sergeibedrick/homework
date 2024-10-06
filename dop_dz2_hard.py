def find_valid_pairs(n):
    pairs = []
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0 and (i, j) != (1, 1):
                pairs.append((i, j))
    return pairs

results = {n: find_valid_pairs(n) for n in range(3, 21)}
for n, pairs in results.items():
    print(f"Число {n}: {pairs}")

print()

# или так
def find_valid_pairs(n):
    return [(i, j) for i in range(1, n) for j in range(i, n) if n % (i + j)
            == 0 and (i, j) != (1, 1)]

results = {n: find_valid_pairs(n) for n in range(3, 21)}
for n, pairs in results.items():
    print(f"Число {n}: {pairs}")