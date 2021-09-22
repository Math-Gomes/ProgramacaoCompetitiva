if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())

        l = 1
        r = n * k
        while l < r:
            mid = l + (r - l) // 2
            count = mid - (mid // n) # Qtd de números não-divisíveis por n no intervalo [1, mid]

            if count < k:
                l = mid + 1
            else:
                r = mid

        print(l)
