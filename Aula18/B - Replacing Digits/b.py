if __name__ == '__main__':
    a = list(map(int, list(input())))
    s = list(map(int, list(input())))
    
    while True:
        max_s = max(s)
        min_a = min(a)

        if max_s < min_a:
            break

        s.remove(max_s)
        a[a.index(min_a)] = max_s

    print(*a, sep = '')

