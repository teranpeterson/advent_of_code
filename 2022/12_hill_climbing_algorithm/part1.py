from collections import defaultdict
from math import inf

def searchMap(old, x, y, count, path):
    if path[(x,y)]:
        return inf
    path[(x,y)] = True
    if x < 0 or x > len(map[0])-1 or y < 0 or y > len(map)-1:
        return inf
    new = map[y][x]
    if new == "E":
        if ord('z') - ord(old) > 1:
            return inf
        return count
    if ord(new) - ord(old) > 1:
        return inf
    else:
        return min(searchMap(new, x+1, y, count+1, path.copy()), searchMap(new, x-1, y, count+1, path.copy()), searchMap(new, x, y+1, count+1, path.copy()), searchMap(new, x, y-1, count+1, path.copy()))

map = []

Sx = -1
Sy = -1
Ex = -1
Ey = -1
with open("input.txt", "r") as file:
    for idx, line in enumerate(file):
        line = line.strip()
        row = []
        for jdx, c in enumerate(line):
            row.append(c)
            if c == "S":
                Sx = jdx
                Sy = idx
                row.pop()
                row.append('a')
            elif c == "E":
                Ex = jdx
                Ey = idx
        map.append(row)

print(searchMap("a", Sx, Sy, 0, defaultdict(bool)))