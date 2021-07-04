while True:
    k = int(input())

    if k == 0:
        break

    n, m = list(map(int, input().split()))

    for _ in range(k):
        x, y = list(map(int, input().split()))

        if x == n or y == m:
            print('divisa')
        else:
            print('N' if y > m else 'S', 'O' if x < n else 'E', sep='')
