a = 2
b = 500

nImparDivisores = 0
for i in range(a, b + 1):
  if int(i ** 0.5) ** 2 == i:
    nImparDivisores += 1
    
print(nImparDivisores)
