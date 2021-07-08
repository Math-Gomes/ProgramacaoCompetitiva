def has_parity_property(matrix):
    for row in matrix:
        if sum(row) % 2 != 0:
            return False

    for col in [*zip(*matrix)]:
        if sum(col) % 2 != 0:
            return False

    return True

def change_bits(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0 if matrix[i][j] else 1 # Troca o bit
            if has_parity_property(matrix):
                return True, i + 1, j + 1
            else:
                matrix[i][j] = 0 if matrix[i][j] else 1 # Desfaz a troca de bit
    return False, 0, 0

while True:
    n = int(input())

    if not n:
        break

    matrix = [list(map(int, input().split())) for _ in range(n)]

    if has_parity_property(matrix):
        print('OK')
    else:
        change_bits_work, i, j = change_bits(matrix)

        if change_bits_work:
            print('Change bit ({},{})'.format(i, j))
        else:
            print('Corrupt')
