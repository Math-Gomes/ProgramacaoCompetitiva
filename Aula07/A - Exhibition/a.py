k = int(input())

for case in range(1, k + 1):
    n_friends = int(input())

    stamps = {}
    for i in range(n_friends):
        _, *collection = list(map(int, input().split()))

        for stamp in collection:
            stamps.setdefault(stamp, set()).add(i)

    unique_stamps = [0] * n_friends
    for v in stamps.values():
        if len(v) == 1:
            unique_stamps[[*v][0]] += 1
    
    n_unique_stamps = sum(unique_stamps)
    if not n_unique_stamps:
        unique_stamps = map(lambda x: x + 1, unique_stamps)

    percent = map(lambda x: x / sum(unique_stamps), unique_stamps)
    result = ' '.join(map(lambda x: '{:.6%}'.format(x), percent))

    print('Case {}:'.format(case), result)
