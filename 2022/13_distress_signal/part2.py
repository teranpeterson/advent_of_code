import json
import functools

def compareLists(left, right):
    for j in range(max(len(left), len(right))):
        try:
            l = left[j]
        except:
            return -1
        try:
            r = right[j]
        except:
            return 1
        if isinstance(l, list) and isinstance(r, list):
            x = compareLists(l, r)
            if x == 0:
                continue
            else:
                return x
        elif isinstance(l, list) and isinstance(r, int):
            y = compareLists(l, [r])
            if y == 0:
                continue
            else:
                return y
        elif isinstance(l, int) and isinstance(r, list):
            z = compareLists([l], r)
            if z == 0:
                continue
            else:
                return z
        elif r < l:
            return 1
        elif l < r:
            return -1
        else:
            continue
    return 0

signals = []
with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            continue
        signals.append(json.loads(line))

signals.append(json.loads("[[2]]"))
signals.append(json.loads("[[6]]"))

signals.sort(key=functools.cmp_to_key(compareLists))

a = signals.index(json.loads("[[2]]"))+1
b = signals.index(json.loads("[[6]]"))+1
print(a*b)
# 1, 2, 4, and 6