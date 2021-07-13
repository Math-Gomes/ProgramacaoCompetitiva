d = {}

while True:
    try:
        english, foreign = input().split()
        d[foreign] = english
    except:
        break

while True:
    try:
        word = input()
        try:
            print(d[word])
        except KeyError:
            print('eh')
    except:
        break
    