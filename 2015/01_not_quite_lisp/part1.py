with open("input.txt", "r") as file:
    i = 0
    for line in file:
        for char in line:
            if char == "(":
                i += 1
            elif char == ")":
                i -= 1
            else:
                print("DEAD")
                exit(1)
    print(i)