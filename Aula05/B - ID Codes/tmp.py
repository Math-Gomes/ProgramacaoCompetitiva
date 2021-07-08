from sys import stdin, stdout

while True:
    inp = stdin.readline().strip()

    if inp == "#":
        break

    successor = None
    inp = list(inp)
    for i in range(len(inp)-1, 0, -1):
        print('comp inp[{}] > inp[{}] = {}'.format(inp[i], inp[i-1], inp[i] > inp[i-1]))
        if ord(inp[i]) > ord(inp[i-1]):

            successor = ("".join(inp[0:i-1]) if i > 1 else "")

            print('inp[{}] = {}'.format(i, inp[i]), '[' + successor + ']')
            # input()

            min_v, min_i = inp[i], i
            for j in range(i, len(inp)):

                print('min_v = {}, min_i = {}'.format(min_v, min_i))
                print('comp inp[{}] < min_v({}) = {}'.format(inp[j], min_v, inp[j] < min_v))
                print('comp inp[{}] >   inp[{}] = {}'.format(inp[j], inp[i-1], inp[j] > inp[i-1]))

                if inp[j] < min_v and inp[j] > inp[i-1]:
                    min_v, min_i = inp[j], j

            print('min_v = {}, min_i = {}'.format(min_v, min_i))

            successor += min_v
            print(successor)

            print(inp)
            inp[min_i] = inp[i-1]
            print(inp)

            print("".join(sorted(inp[i:])))
            successor += "".join(sorted(inp[i:]))
            print(successor)

            break

    if successor:
        stdout.write("{}\n".format(successor))
    else:
        stdout.write("No Successor\n")
