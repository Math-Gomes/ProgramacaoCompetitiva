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

# Parte 1 do algoritmo de Floyd!

T = v[0]        # T é tartaruga (primeiro elemento do vetor)
L = v[v[0]]     # L é a lebre (segundo da "lista" -- o elemento apontado pelo primeiro elemento do vetor)
while T != L:
  T = v[T]      # T anda uma posição na lista
  L = v[v[L]]   # L anda duas posições na lista

# Só podemos dizer que T e L estão dentro do ciclo

# Parte 2 do algoritmo de Floyd!

# L continua aonde estava
T = v[0]       # T volta para o início
while T != L:
  T = v[T]
  L = v[L]

# Quando o algoritmo termina, T e L apontam para o início da lista
# É o elemento repetido do vetor

print(T)