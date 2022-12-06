with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        pair = False
        sand = False
        for i in range(len(line) - 1):
            x = line[i:i+2]
            l_rest = line[:i]
            r_rest = line[i+2:]
            if x in l_rest or x in r_rest:
                pair = True
                break
        for i in range(len(line) - 2):
            if line[i] == line[i+2]:
                sand = True
                break
        if pair and sand:
            sum += 1
    print(sum)