import heapq

pq, cmds, result = [], [], []

for _ in range(int(input())):
    cmds.append(input().split())

for cmd in cmds:
    op = cmd[0]

    if len(cmd) > 1:
        value = int(cmd[1])

    if op == 'insert':
        heapq.heappush(pq, value)
    
    elif op == 'getMin':
        if len(pq) == 0:
            heapq.heappush(pq, value)
            result.append('insert {}'.format(value))
        else:
            if value < pq[0]:
                heapq.heappush(pq, value)
                result.append('insert {}'.format(value))
            elif value > pq[0]: 
                while len(pq) > 0 and value > pq[0]:
                    heapq.heappop(pq)
                    result.append('removeMin')
                
                if len(pq) == 0 or pq[0] != value:
                    heapq.heappush(pq, value)
                    result.append('insert {}'.format(value))

    else: # op == 'removeMin'
        if len(pq) == 0:
            heapq.heappushpop(pq, 1)
            result.append('insert 1')
        elif len(pq) > 0:
            heapq.heappop(pq)

    result.append(' '.join(cmd))

print(len(result))

for cmd in result:
    print(cmd)
