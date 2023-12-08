with open('input.txt', 'r') as file:
    res = 0
    for line in file:
        first = -1
        last = -1
        for c in line:
            if c.isnumeric():
                if first == -1:
                    first = int(c)
                last = int(c)
        res += int(str(first) + str(last))

    print(res)
