def equals(l):
    return l.count(l[0]) == len(l)

# equals([maze[i][j], maze[i + 1][j], maze[i][j + 1], maze[i + 1][j + 1]])



if __name__ == '__main__':
    square = []

    for _ in range(4):
        square.append(list(input()))

    # print(solve(0, 0, 'x', 4, 4))
           