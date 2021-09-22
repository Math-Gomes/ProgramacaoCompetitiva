if __name__ == '__main__':
    s = input()
    pos, sz = 0, 0
    for i, c in enumerate(s):
        if c == 'hello'[pos]:
            pos += 1
            sz += 1

        if sz == 5:
            print('YES')
            exit()
        else:
            continue

    print('NO')
