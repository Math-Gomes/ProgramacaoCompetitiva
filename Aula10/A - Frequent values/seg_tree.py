class SegTree:
    def __init__(self, A):
        self.A = A
        self.n = len(A)
        self.T = [0] * (4 * self.n)
        self.build()

    def __str__(self):
        return self.tree_repr()

    def tree_repr_rec(self, node, start, end, level):
        if node > len(self.T) - 1:
            return ""
        else:
            level += 1
            mid = (start + end) // 2

            # Chamada recursiva para filho à esquerda 
            left = self.tree_repr_rec(2 * node, start, mid, level)

            # Chamada recursiva para filho à direita
            right = self.tree_repr_rec(2 * node + 1, mid + 1, end, level)
            
            # current = '- {:5d}'.format(self.T[node]) + '\n' if self.T[node] else "\n"
            return '   ' * level + '{:5d}'.format(self.T[node]) + '\n' + left + right

    def tree_repr(self):
        return self.tree_repr_rec(1, 0, self.n - 1, 0)

    """
        Método Recursivo
        Constrói uma SegTree 'T' a partir de um array 'A'
        O primeiro elemento de 'A' está em 'start'
        O último elemento de 'A' está em 'end'
        O nó atual da árvore sendo analisado é 'node'
    """
    def buildRec(self, node, start, end):
        if start == end:
            # Folha representa um elemento único 
            self.T[node] = self.A[start]
        else:
            mid = (start + end) // 2
            
            # Chamada recursiva para filho à esquerda 
            self.buildRec(2 * node, start, mid)

            # Chamada recursiva para filho à direita
            self.buildRec(2 * node + 1, mid + 1, end)

            # Nó interno tem a SOMA dos dois filhos 
            self.T[node] = self.T[2 * node] + self.T[2 * node + 1]; # <======= IMPORTANTE
        
    """
        Interface para a construção da árvore
        'T' é o vetor que armazenará a árvore
        'A' é o vetor com os dados originais
        'n' é o número de elemento em 'A'. 'T' deve ter tamanho '2n'
        Complexidade de tempo: O(n)
        Complexidade de espaço: O(n)
    """
    def build(self):
        self.buildRec(1, 0, self.n - 1) # A raíz tem nó 1 e representa o segmento A[0, ..., n-1]

    """
        Função recursiva pela busca da soma de A[l, ..., r]
        'T' é a SegTree
        'node' é o nó atual da SegTree sendo inspecionado
        'start' é o início do intervalo representado em 'node'
        'end' é o fim do intervalo representado em 'node'
        'l' é o limite inferior da busca
        'r' é o limite superior da busca
    """
    def queryRec(self, node, start, end, l, r):
        if r < start or end < l:
            # [start, end] está fora de [l, r] -- não há interseção
            return 0 # <======= IMPORTANTE
        
        if l <= start and end <= r:
            # [start, end] está contido em [l, r] 
            return self.T[node]

        # [start, end] e [l, r] têm interseção 
        mid = (start + end) // 2
        p1 = self.queryRec(2 * node, start, mid, l, r)
        p2 = self.queryRec(2 * node + 1, mid + 1, end, l, r)

        return (p1 + p2); # <======= IMPORTANTE
    
    """
        Interface para a busca: Soma dos elementos A[l, ..., r]
        'T' é a SegTree
        'n' é o número de elementos no vetor 'A'
        'l' limite inferior da busca
        'r' limite superior da busca
    """
    def query(self, l, r): # Soma(A[l, ..., r])
        return self.queryRec(1, 0, self.n - 1, l, r)
    
    """
        Função Recursiva para atualizar A[idx], fazendo A[idx] += val
        'T' é a SegTree
        'A' é o vetor original com os elementos
        'node' é o nó atual da SegTree sendo inspecionado
        'start' é o início do intervalo representado por 'node' 
        'end' é o fim do intervalo representado por 'node' 
        'idx' é o índice do elemento a ser atualizado
        'val' é o valor a ser somado a A[idx]
    """
    def updateRec(self, node, start, end, idx, val):
        if start == end:
            # Nó folha, atualiza A e T
            self.A[idx] += val
            self.T[node] += val
        else:
            mid = (start + end) // 2
            if start <= idx and idx <= mid:
                # idx está no filho à esquerda 
                self.updateRec(2 * node, start, mid, idx, val)
            else:
                # idx está no filho à direita 
                self.updateRec(2 * node + 1, mid + 1, end, idx, val)

            # Faz atualização do nó pai 
            self.T[node] = self.T[2 * node] + self.T[2 * node + 1]; # <======= IMPORTANTE

    """
        Interface para atualizar A[idx], fazendo A[idx] += val
        'T' é a SegTree
        'A' é o vetor original com os elementos
        'n' é o tamanho de 'A'
        'idx' é o índice do elemento a ser atualizado
        'val' é o valor a ser somado a A[idx]
    """
    def update(self, idx, val): # A[idx] = A[idx] + val
        self.updateRec(1, 0, self.n - 1, idx, val)

if __name__ == '__main__':
    A = [1, 3, 5, 7, 9, 11]

    st = SegTree(A)

    st.update(0, 50)

    print(st)