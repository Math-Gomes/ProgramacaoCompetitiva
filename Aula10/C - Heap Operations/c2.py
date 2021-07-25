from heapq import heappush, heappop

def insert(heap, item):
    heappush(heap, item)

def removeMin(heap):
    return heappop(heap)

def getMin(heap):
    return heap[0]

if __name__ == '__main__':
    logs = []
    heap = []
    n = int(input())
    for _ in range(n):
        command = input().split()
        if command[0] == 'insert':
            x = int(command[1])
            insert(heap, x)
            logs.append('insert {}'.format(x))
        elif command[0] == 'getMin':
            x = int(command[1])
            while True:
                if not heap:
                    insert(heap, x)
                    logs.append('insert {}'.format(x))

                min = getMin(heap)
                if x == min:
                    logs.append('getMin {}'.format(x))
                    break
                elif x > min:
                    removeMin(heap)
                    logs.append('removeMin')
                else:
                    insert(heap, x)
                    logs.append('insert {}'.format(x))
        else:
            if not heap:
                x = 1
                insert(heap, x)
                logs.append('insert {}'.format(x))
            removeMin(heap)
            logs.append('removeMin')
    print(len(logs))
    print('\n'.join(logs))