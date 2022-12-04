# A = X = ROCK
# B = Y = PAPER
# C = Z = SCISSORS

A_X = 3 + 1
A_Y = 6 + 2
A_Z = 0 + 3
B_X = 0 + 1
B_Y = 3 + 2
B_Z = 6 + 3
C_X = 6 + 1
C_Y = 0 + 2
C_Z = 3 + 3

with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        if line.strip() == "A X":
            sum += A_X
        elif line.strip() == "A Y":
            sum += A_Y
        elif line.strip() == "A Z":
            sum += A_Z
        elif line.strip() == "B X":
            sum += B_X
        elif line.strip() == "B Y":
            sum += B_Y
        elif line.strip() == "B Z":
            sum += B_Z
        elif line.strip() == "C X":
            sum += C_X
        elif line.strip() == "C Y":
            sum += C_Y
        elif line.strip() == "C Z":
            sum += C_Z
        else:
            print(line)
    print(sum)