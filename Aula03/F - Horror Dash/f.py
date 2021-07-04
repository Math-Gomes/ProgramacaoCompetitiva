t = int(input())

for case in range(t):
    _, *speeds = list(map(int, input().split()))
    print('Case {}: {}'.format(case + 1, max(speeds)))
