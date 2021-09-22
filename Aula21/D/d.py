from sys import setrecursionlimit

def jump(i):
    if dp[i] < 0:
        if i == (n - 1): 
            dp[i] = 0
        elif (i + 2) < n:
            dp[i] = min(
                jump(i + 1) + abs(stones[i] - stones[i + 1]),
                jump(i + 2) + abs(stones[i] - stones[i + 2]),
            )
        elif (i + 1) < n:
            dp[i] = jump(i + 1) + abs(stones[i] - stones[i + 1])

    return dp[i]


if __name__ == '__main__':
    setrecursionlimit(100100)

    n = int(input())
    stones = list(map(int, input().split()))
    dp = [-1] * n

    print(jump(0))
