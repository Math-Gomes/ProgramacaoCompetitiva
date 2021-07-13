from re import findall

text = ''
words = set()

while True:
    try:
        text += input().lower().replace('-\n', '')
    except:
        [words.add(w) for w in findall('[a-z\-]+', text)]
        break

print(*sorted(words), sep='\n', end='')
