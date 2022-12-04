with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        l, h, w = line.split("x")
        l = int(l)
        h = int(h)
        w = int(w)
        rib = min(l+l+h+h, l+l+w+w, h+h+w+w)
        bow = l*w*h
        sum += rib + bow
    print(sum)
