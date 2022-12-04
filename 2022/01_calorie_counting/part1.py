with open("input.txt", "r") as file:
    max = 0
    sum = 0
    for line in file:
        if line == "\n":
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(line.strip())
print(max)