t = int(input())

for case in range(t):
    salaries = list(map(int, input().split()))
    salaries.sort()
    print('Case {}: {}'.format(case + 1, salaries[1]))