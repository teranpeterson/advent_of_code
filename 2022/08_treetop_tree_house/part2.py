forestMap = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        forestMap.append(list(line))

l = len(forestMap[0])
h = len(forestMap)

max = 0

for i in range(l):
    for j in range(h):
        c = int(forestMap[i][j])
        left = 0
        left_j = j
        while left_j > 0:
            left_j -= 1
            left += 1
            if int(forestMap[i][left_j]) >= c:
                break
        
        right = 0
        right_j = j
        while right_j < l - 1:
            right_j += 1
            right += 1
            if int(forestMap[i][right_j]) >= c:
                break
        
        up = 0
        up_i = i
        while up_i > 0:
            up_i -= 1
            up +=1
            if int(forestMap[up_i][j]) >= c:
                break
        
        down = 0
        down_i = i
        while down_i < h - 1:
            down_i += 1
            down += 1
            if int(forestMap[down_i][j]) >= c:
                break
        
        score = right * left * up * down
        if score > max:
            max = score

print(max)
