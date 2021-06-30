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

v.sort()
for i in range(len(v) - 1):
  if v[i] == v[i+1]:
    print(v[i])
    break