# A = ROCK 1
# B = PAPER 2
# C = SCISSORS 3

# X = LOSE 0
# Y = DRAW 3
# Z = WIN 6

A_X = 0 + 3
A_Y = 3 + 1
A_Z = 6 + 2
B_X = 0 + 1
B_Y = 3 + 2
B_Z = 6 + 3
C_X = 0 + 2
C_Y = 3 + 3
C_Z = 6 + 1

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