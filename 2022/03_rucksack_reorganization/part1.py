with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        firstComp, secondComp = line[:len(line)//2], line[len(line)//2:]
        for c in firstComp:
            if c in secondComp:
                x = ord(c)
                if x > 64 and x < 91:
                    x -= 64 - 26
                elif x > 96 and x < 123:
                    x -= 96
                else:
                    print("DEAD")
                    exit(1)
                sum += x
                break
    print(sum)