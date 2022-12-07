goal = 30000000 - (70000000 - 45349983)
target = 70000000

def computeDirSums(x):
    if isinstance(x, dict):
        sum = 0
        for key in x.keys():
            sum += computeDirSums(x[key])
        global goal
        global target
        if sum >= goal and sum < target:
            target = sum
        return sum
    elif isinstance(x, int):
        return x
    else:
        print("DEAD")
        exit(1)

with open("input.txt", "r") as file:
    pwd = []
    fs = {
        "/": {}
    }
    for line in file:
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    pwd.pop()
                elif line[2] == "/":
                    pwd.clear()
                    pwd.append("/")
                else:
                    pwd.append(line[2])
            elif line[1] == "ls":
                pass
        elif line[0] == "dir":
            temp = fs
            for key in pwd:
                temp = temp[key]
            temp[line[1]] = {}
        elif line[0].isdigit():
            temp = fs
            for key in pwd:
                temp = temp[key]
            temp[line[1]] = int(line[0])

    computeDirSums(fs)
    print(target)
