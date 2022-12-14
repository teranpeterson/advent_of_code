from collections import defaultdict

def computeSand(rocks, xSand, ySand, floor):
    if rocks[(xSand, ySand)]:
        return False
    elif floor-ySand <= 1:
        rocks[(xSand, ySand)] = True
        return True
    elif not rocks[(xSand, ySand+1)]:
        return computeSand(rocks, xSand, ySand+1, floor)
    elif not rocks[(xSand-1, ySand+1)]:
        return computeSand(rocks, xSand-1, ySand+1, floor)
    elif not rocks[(xSand+1, ySand+1)]:
        return computeSand(rocks, xSand+1, ySand+1, floor)
    else:
        rocks[(xSand, ySand)] = True
        return True

def printRocks(rocks, xMin, xMax, yMin, yMax):
    for y in range(yMin, yMax+1):
        for x in range(xMin, xMax+1):
            if rocks[(x,y)]:
                print("#", end="")
            elif (x,y) == (500,0):
                print("+", end="")
            elif y == yMax:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

xMin = 500
xMax = 500
yMin = 0
yMax = 0
rocks = defaultdict(bool)

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        points = line.split(" -> ")
        for i in range(len(points)-1):
            x1, y1 = points[i].split(",")
            x2, y2 = points[i+1].split(",")
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            xMin = min(xMin, x1, x2)
            xMax = max(xMax, x1, x2)
            yMin = min(yMin, y1, y2)
            yMax = max(yMax, y1, y2)

            if (x2 - x1 == 0 and y2 - y1 == 0) or (x2 - x1 != 0 and y2 - y1 != 0):
                print("Oops")
                exit(1)
            elif x2 - x1 > 0:
                for i in range(x2-x1+1):
                    rocks[(x1+i, y1)] = True
            elif x2 - x1 < 0:
                for i in range(abs(x2-x1)+1):
                    rocks[(x2+i, y1)] = True
            elif y2 - y1 > 0:
                for i in range(y2-y1+1):
                    rocks[(x1, y1+i)] = True
            elif y2 - y1 < 0:
                for i in range(abs(y2-y1)+1):
                    rocks[(x1, y2+i)] = True
            else:
                print("Oops")
                exit(1)

floor = yMax + 2

printRocks(rocks, xMin, xMax, yMin, floor)

count = 0
while True:
    if computeSand(rocks, 500, 0, floor):
        count += 1
    else:
        printRocks(rocks, xMin, xMax, yMin, floor)
        print(count)
        exit(0)