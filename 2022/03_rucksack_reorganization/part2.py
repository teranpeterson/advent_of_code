from collections import defaultdict

with open("input.txt", "r") as file:
    sum = 0
    triDict = defaultdict(int)
    for line in file:
        lineDict = defaultdict(int)
        for c in line:
            lineDict[c] += 1
            if lineDict[c] == 1:
                triDict[c] += 1
                if triDict[c] == 3:
                    x = ord(c)
                    if x > 64 and x < 91:
                        x -= 64 - 26
                    elif x > 96 and x < 123:
                        x -= 96
                    else:
                        print("DEAD")
                        exit(1)
                    sum += x
                    triDict.clear()
                    break
    print(sum)