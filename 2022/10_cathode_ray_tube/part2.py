def printReg(d, X):
    cycles = d % 40
    if X == cycles or X + 1 == cycles or X + 2 == cycles:
        print("#", end="")
    else:
        print(".", end="")
    if cycles == 0:
        print()

with open("input.txt", "r") as file:
    X = 1
    cycles = 1

    for line in file:
        line = line.strip()
        line = line.split()
        inst = line[0]
        if inst == "addx":
            val = int(line[1])
            printReg(cycles, X)
            cycles += 1
            printReg(cycles, X)
            cycles += 1
            X += val
        else:
            printReg(cycles, X)
            cycles += 1