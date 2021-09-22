# {
#   [S (valor), n_eggs (peso)]
# }
def respect_constraint(state, max_n_eggs):
    if abs(state[0][0] - state[1][0]) <= 500:
        if state[0][1] <= max_n_eggs and state[1][1] <= max_n_eggs:
            return True
    return False

def expand(state, price, max_n_eggs):
    possibilities = []

    s = []
    for i in range(len(state)):
        s.append(state[:])
        s[i][0] += price[i]
        s[i][1] += 1
        # if respect_constraint(s, max_n_eggs):
        possibilities.append(s)
    print(possibilities)
    return possibilities


if __name__ == '__main__':
    n_eggs = int(input())
    prices = [list(map(int, input().split())) for _ in range(n_eggs)]
    
    a = [0, 0]
    b = [0, 0]
    state = [a, b]

    max_n_eggs = (n_eggs // 2) + (n_eggs %  2)
    print(*prices, sep='\n')
    for p in prices:
        expand(state, p, max_n_eggs)
        # print(state)
        

    