with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        l, h, w = line.split("x")
        l = int(l)
        h = int(h)
        w = int(w)
        dim = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        sum += dim + slack
    print(sum)