with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        for i in range(len(line) - 3):
            c = line[i:i+4]
            if len(set(c)) == len(c):
                print(i + 4)
                break