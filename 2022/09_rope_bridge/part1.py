from collections import defaultdict

with open("input.txt", "r") as file:

    d = defaultdict(int)

    Hx = 0
    Hy = 0
    Tx = 0
    Ty = 0

    for line in file:
        line = line.strip()
        direction, distance = line.split()
        for i in range(int(distance)):
            if direction == "R":
                Hx += 1
            elif direction == "L":
                Hx -= 1
            elif direction == "U":
                Hy += 1
            elif direction == "D":
                Hy -= 1
            x_diff = Hx-Tx
            y_diff = Hy-Ty
            if y_diff == 0 and x_diff > 1:
                Tx += 1
            elif y_diff == 0 and x_diff < -1:
                Tx -= 1
            elif x_diff == 0 and y_diff > 1:
                Ty += 1
            elif x_diff == 0 and y_diff < -1:
                Ty -= 1
            elif abs(y_diff) > 1 or abs(x_diff) > 1:
                if y_diff > 0:
                    Ty += 1
                else:
                    Ty -= 1
                if x_diff > 0:
                    Tx += 1
                else:
                    Tx -= 1
            d[(Tx, Ty)] += 1
    print(len(d))