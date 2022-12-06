with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        for i in range(len(line) - 13):
            c = line[i:i+14]
            if len(set(c)) == len(c):
                print(i + 14)
                break