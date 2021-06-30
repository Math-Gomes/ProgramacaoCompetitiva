import random

def createVector(N):
  v = [i for i in range(1, N)]
  j = v[random.randint(0, len(v)-1)]
  v.append(j)
  random.shuffle(v)
  return v

#v = [1, 3, 4, 2, 2]
#v = [1, 2, 3, 4, 4]
#v = [3, 1, 3, 2, 4]
#v = [1, 1, 2]
#v = [1, 1]

v = createVector(100)

tam = 0       # Tamanho de v
sum = 0       # Somatório dos elementos de v
max = v[0]    # Maior elemento de v

# Laço para calcular o tamanho de v, a soma dos elementos e o valor do maior elemento
for i in v:
  sum += i
  if i > max:
    max = i
  tam += 1

# Sabemos que os elementos de v vão de 1 a n e algum desses elementos se repete

# A soma dos elementos de uma p. a. é dada por n * (n + 1) / 2
sum_pa = (max) * (max + 1) / 2

repeticoes = tam - max

diff = sum - sum_pa

numeroRepetido = diff / repeticoes

print(int(numeroRepetido))