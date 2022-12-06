with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        n = 0
        dup = False
        cln = True
        for i in range(len(line)):
            if line[i] in "aeiou":
                n += 1
            if i >= len(line) - 1:
                break
            s = line[i:i+2]
            if s == "ab" or s == "cd" or s == "pq" or s == "xy":
                cln = False
                break
            if line[i] == line[i+1]:
                dup = True
        if n >= 3 and dup and cln:
            sum += 1
    print(sum)