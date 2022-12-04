with open("input.txt", "r") as file:
    i = 0
    j = 0
    for line in file:
        for char in line:
            j += 1
            if char == "(":
                i += 1
            elif char == ")":
                i -= 1
            else:
                print("DEAD")
                exit(1)
            if i < 0:
                print(j)
                exit(0)