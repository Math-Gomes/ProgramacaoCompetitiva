if __name__ == '__main__':
    n = int(input())
    p = [0] + list(map(int, input().split()))

    path = [n]
    while path[-1] != 1:
        path.append(p[path[-1] - 1])

    print(*path[::-1])
