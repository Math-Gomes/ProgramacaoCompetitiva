if __name__ == '__main__':
    a, k = input().split()
    a = list(map(int, list(a)))
    k = int(k)

    i = 0

    while k > 0 and i < len(a):
        limit = len(a) if (i + k) >= len(a) else i + k + 1
        max_i = i

        # Procura a posição do maior elemento de um intervalo do array, 
        # considerando a limitação de movimentos restantes
        for j in range(i + 1, limit):
            if a[j] > a[max_i]:
                max_i = j
        
        k -= (max_i - i) # Subtrai de k a distância de a[i] até a[max_i]
        
        if k >= 0:
            # Troca a[max_i] com os elementos anteriores até que a[max_i] esteja na posição i
            for j in range(max_i, i, -1):
                tmp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = tmp

        i += 1

    print(*a, sep='')