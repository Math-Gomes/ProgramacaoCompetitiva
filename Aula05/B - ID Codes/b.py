while True:
    code = input()

    if code == '#':
        break

    successor = ""

    for i in range(len(code) - 1, 0, -1):
        if code[i] > code[i - 1]:
            low_i, low = i, code[i]

            for j in range(i, len(code)):
                if code[j] < low and code[j] > code[i - 1]:
                    low_i, low = j, code[j]

            code = list(code)
            code[low_i] = code[i - 1]

            successor = "".join(code[0:i - 1]) + low + "".join(sorted(code[i:]))

            break

    print("{}".format(successor) if successor else "No Successor")
