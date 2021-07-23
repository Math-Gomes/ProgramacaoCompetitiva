from collections import Counter

class SegTree:
    # Método Recursivo
    # Constrói uma SegTree 'T' a partir de um array 'A'
    # O primeiro elemento de 'A' está em 'start'
    # O último elemenot de 'A' está em 'end'
    # O nó atual da árvore sendo analisado é 'node'
    def buildRec(T, A, node, start, end):
        if start == end:
            # Folha representa um elemento único 
            T[node] = A[start]
        else:
            mid = (start + end) / 2
            # Chamada recursiva para filho à esquerda 
            buildRec(T, A, 2 * node, start, mid)
            # Chamada recursiva para filho à direita
            buildRec(T, A, 2 * node + 1, mid+1, end)
            # Nó interno tem a SOMA dos dois filhos 
            T[node] = T[2 * node] + T[2 * node + 1];        # <======= IMPORTANTE

    # Interface para a construção da árvore
    # 'T' é o vetor que armazenará a árvore
    # 'A' é o vetor com os dados originais
    # 'n' é o número de elemento em 'A'. 'T' deve ter tamanho '2n'
    # Complexidade de tempo: O(n)
    # Complexidade de espaço: O(n)
    def build(T, A, n):
        buildRec(T, A, 1, 0, n-1) # A raíz tem nó 1 e representa o segmento A[0, ..., n-1]

    # Função recursiva pela busca da soma de A[l, ..., r]
    # 'T' é a SegTree
    # 'node' é o nó atual da SegTree sendo inspecionado
    # 'start' é o início do intervalo representado em 'node'
    # 'end' é o fim do intervalo representado em 'node'
    # 'l' é o limite inferior da busca
    # 'r' é o limite superior da busca
    def queryRec(T, node, start, end, l, r):
        if r < start or end < l:
            # [start, end] está fora de [l, r] -- não há interseção
            return 0;                                       # <======= IMPORTANTE
        
        if l <= start and end <= r:
            # [start, end] está contido em [l, r] 
            return T[node]
        
        # [start, end] e [l, r] têm interseção 
        mid = (start + end) / 2
        p1 = queryRec(T, 2 * node, start, mid, l, r)
        p2 = queryRec(T, 2 * node + 1, mid + 1, end, l, r)
        return (p1 + p2);                                   # <======= IMPORTANTE

    # Interface para a busca: Soma dos elementos A[l, ..., r]
    # 'T' é a SegTree
    # 'n' é o número de elementos no vetor 'A'
    # 'l' limite inferior da busca
    # 'r' limite superior da busca
    def query(T, n, l, r): #Soma(A[l, ..., r])
        return queryRec(T, 1, 0, n-1, l, r)

    # Função Recursiva para atualizar A[idx], fazendo A[idx] += val
    # 'T' é a SegTree
    # 'A' é o vetor original com os elementos
    # 'node' é o nó atual da SegTree sendo inspecionado
    # 'start' é o início do intervalo representado por 'node' 
    # 'end' é o fim do intervalo representado por 'node' 
    # 'idx' é o índice do elemento a ser atualizado
    # 'val' é o valor a ser somado a A[idx]
    def updateRec(T, A, node, start, end, idx, val):
        if start == end:
            # Nó folha, atualiza A e T
            A[idx] += val
            T[node] += val
        else:
            mid = (start + end) / 2
            if start <= idx and idx <= mid:
                # idx está no filho à esquerda 
                updateRec(T, A, 2 * node, start, mid, idx, val)
            else:
                # idx está no filho à direita 
                updateRec(T, A, 2 * node + 1, mid + 1, end, idx, val)
            
            # Faz atualização do nó pai 
            T[node] = T[2 * node] + T[2 * node + 1];        # <======= IMPORTANTE

    # Interface para atualizar A[idx], fazendo A[idx] += val
    # 'T' é a SegTree
    # 'A' é o vetor original com os elementos
    # 'n' é o tamanho de 'A'
    # 'idx' é o índice do elemento a ser atualizado
    # 'val' é o valor a ser somado a A[idx]
    def update(T, A, n, idx, val): # A[idx] = A[idx] + val
        updateRec(T, A, 1, 0, n - 1, idx, val)

if __name__ == '__main__':
    n, q = map(int, input().split())

    A = list(map(int, input().split()))

    for _ in range(q):
        i, j = map(int, input().split())
        print(max(Counter(A[i:j]).items(), key = lambda x: x[1])[1])

