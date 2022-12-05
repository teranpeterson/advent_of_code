from collections import defaultdict

with open("input.txt", "r") as file:
    d = defaultdict(int)
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0
    d[(santa_x,santa_y)] += 1
    d[(robo_x,robo_y)] += 1
    for line in file:
        line = line.strip()
        for idx, c in enumerate(line):
            if idx % 2 == 0:
                if c == '^':
                    santa_y += 1
                elif c == '>':
                    santa_x += 1
                elif c == 'v':
                    santa_y -= 1
                elif c == '<':
                    santa_x -= 1
                d[(santa_x,santa_y)] += 1
            else:
                if c == '^':
                    robo_y += 1
                elif c == '>':
                    robo_x += 1
                elif c == 'v':
                    robo_y -= 1
                elif c == '<':
                    robo_x -= 1
                d[(robo_x,robo_y)] += 1
    print(len(d))