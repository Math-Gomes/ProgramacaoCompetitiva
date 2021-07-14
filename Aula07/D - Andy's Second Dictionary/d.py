from re import findall

text = ''

while True:
    try:
        text += input().lower() + '\n'
    except:
        break

print(*sorted(set(findall('[a-z\-]+', text.replace('-\n', '')))), sep='\n')
