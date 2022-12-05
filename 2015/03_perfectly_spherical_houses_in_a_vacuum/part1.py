from collections import defaultdict

with open("input.txt", "r") as file:
    d = defaultdict(int)
    x = 0
    y = 0
    d[(x,y)] += 1
    for line in file:
        line = line.strip()
        for c in line:
            if c == '^':
                y += 1
            elif c == '>':
                x += 1
            elif c == 'v':
                y -= 1
            elif c == '<':
                x -= 1
            d[(x,y)] += 1
    print(len(d))