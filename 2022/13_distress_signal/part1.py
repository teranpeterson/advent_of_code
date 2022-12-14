import json

def compareLists(left, right):
    for j in range(max(len(left), len(right))):
        try:
            l = left[j]
        except:
            return True
        try:
            r = right[j]
        except:
            return False
        if isinstance(l, list) and isinstance(r, list):
            x = compareLists(l, r)
            if x == None:
                continue
            else:
                return x
        elif isinstance(l, list) and isinstance(r, int):
            y = compareLists(l, [r])
            if y == None:
                continue
            else:
                return y
        elif isinstance(l, int) and isinstance(r, list):
            z = compareLists([l], r)
            if z == None:
                continue
            else:
                return z
        elif r < l:
            return False
        elif l < r:
            return True
        else:
            continue
    return None

signals = []
with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            continue
        signals.append(json.loads(line))

sum = 0
for i in range(len(signals)//2):
    if compareLists(signals[i*2], signals[i*2+1]):
        sum += i+1
print(sum)

# 1, 2, 4, and 6