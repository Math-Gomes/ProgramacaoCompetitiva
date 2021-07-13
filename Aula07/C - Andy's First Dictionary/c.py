from re import findall

words = set()

while True:
    try:
        [words.add(w) for w in findall('[a-z]+', input().lower())] 
    except:
        break

print(*sorted(words), sep='\n')
