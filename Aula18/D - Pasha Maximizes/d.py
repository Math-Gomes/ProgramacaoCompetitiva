if __name__ == '__main__':
    a, k = input().split()
    a = list(map(int, list(a)))
    k = int(k)

    i, j = 0, 0

    while j < k and i < (len(a) - 1):
        swap = False
        
        if a[i + 1] > a[i]: # swap
            tmp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = tmp

            j += 1
            swap = True

        if swap and i != 0:
            i -= 1
        else:
            i += 1

    
    print(*a, sep='')