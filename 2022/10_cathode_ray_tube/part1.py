def printReg(cycles, X):
    if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
        strength = cycles*X
        print(f"{cycles}: {X} = {strength}")
        return strength
    else:
        return 0

with open("input.txt", "r") as file:
    X = 1
    cycles = 1
    sum = 0

    for line in file:
        line = line.strip()
        line = line.split()
        inst = line[0]
        if inst == "addx":
            val = int(line[1])
            sum += printReg(cycles, X)
            cycles += 1
            sum += printReg(cycles, X)
            cycles += 1
            X += val
        else:
            sum += printReg(cycles, X)
            cycles += 1
    sum += printReg(cycles, X)
    print(sum)