with open("input.txt", "r") as file:
    sums = []
    sum = 0
    for line in file:
        if line == "\n":
            sums.append(sum)
            sum = 0
        else:
            sum += int(line.strip())
sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])