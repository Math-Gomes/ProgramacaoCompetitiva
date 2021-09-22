import random

n = int(1e5)

lista = [random.randint(0, 10) for _ in range(n)]
print(n)
print(*lista, sep = ' ')