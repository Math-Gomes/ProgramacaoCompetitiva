F = [[]]

def get_weight(item):
    return item[0]

def get_value(item):
    return item[1]

def MFKnapsack(i, j):
    if F[i][j] < 0:
        if j < get_weight(items[i]):
            value = MFKnapsack(i - 1, j)
        else:
            value = max(
                MFKnapsack(i - 1, j),
                get_value(items[i]) + MFKnapsack(i - 1, j - get_weight(items[i]))
            )
        F[i][j] = value
    return F[i][j]

if __name__ == '__main__':
    n_items, W = map(int, input().split())

    items = [(-1, -1)]
    for _ in range(n_items):
        w, v = map(int, input().split())
        items.append((w, v))

    F = [[0] * (W + 1)] + [[0] + [-1] * W for _ in range(n_items)]

    print(MFKnapsack(n_items, W))
