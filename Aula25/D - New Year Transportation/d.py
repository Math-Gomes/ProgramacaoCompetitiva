if __name__ == '__main__':
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = 1
    while s < t: 
        s += a[s - 1]
    print('YES') if s == t else print('NO')
        