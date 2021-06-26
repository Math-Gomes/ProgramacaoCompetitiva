a = 2
b = 500

nImparDivisores = 0
for i in range(a, b + 1):
  nDivisores = 0
  for j in range(1, i + 1):
    if i % j == 0:
      nDivisores += 1
  if nDivisores % 2 == 1:
    nImparDivisores += 1

print(nImparDivisores)
