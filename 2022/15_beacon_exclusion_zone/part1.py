from math import inf

def calculateDist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

sensors = {}
y = 2000000
alt = set()

xMin = inf
xMax = -inf
yMin = inf
yMax = -inf
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        sensorX = int(line[2][2:-1])
        sensorY = int(line[3][2:-1])
        beaconX = int(line[8][2:-1])
        beaconY = int(line[9][2:])
        if beaconY == y:
            alt.add((beaconX, beaconY))
        if sensorY == y:
            print("You might care")
        manhattan = calculateDist(sensorX, sensorY, beaconX, beaconY)
        sensors[(sensorX, sensorY)] = manhattan
        xMin = min(xMin, sensorX-manhattan)
        xMax = max(xMax, sensorX+manhattan)
        yMin = min(yMin, sensorY-manhattan)
        yMax = max(yMax, sensorY+manhattan)

count = 0

for x in range(xMin, xMax+1):
    for sensor, manhattan in sensors.items():
        if calculateDist(x, y, sensor[0], sensor[1]) <= manhattan:
            count += 1
            break

print(count - len(alt))