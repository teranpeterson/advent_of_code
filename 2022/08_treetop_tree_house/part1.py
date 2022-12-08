forestMap = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        forestMap.append(list(line))

l = len(forestMap[0])
h = len(forestMap)

bitMap = [[0]*l for _ in range(h)]

top_height = [-1] * l
left_height = [-1] * h
for i in range(l):
    for j in range(h):
        c = int(forestMap[i][j])
        if c > left_height[i]:
            bitMap[i][j] = 1
            left_height[i] = c
        if c > top_height[j]:
            bitMap[i][j] = 1
            top_height[j] = c

bottom_height = [-1] * l
right_height = [-1] * h
for i in range(l-1, -1, -1):
    for j in range(h-1, -1, -1):
        c = int(forestMap[i][j])
        if c > right_height[i]:
            bitMap[i][j] = 1
            right_height[i] = c
        if c > bottom_height[j]:
            bitMap[i][j] = 1
            bottom_height[j] = c

counter = 0
for i in range(l):
    for j in range(h):
        c = int(bitMap[i][j])
        if c == 1:
            counter += 1
        print(c, end="")
    print()
print(counter)