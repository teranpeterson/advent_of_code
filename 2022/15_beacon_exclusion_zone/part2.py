from math import inf

def calculateDist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

sensors = {}

xMin = 0
xMax = 4000000
yMin = 0
yMax = 4000000
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        sensorX = int(line[2][2:-1])
        sensorY = int(line[3][2:-1])
        beaconX = int(line[8][2:-1])
        beaconY = int(line[9][2:])
        manhattan = calculateDist(sensorX, sensorY, beaconX, beaconY)
        sensors[(sensorX, sensorY)] = manhattan

for y in range(yMin, yMax+1):
    x = xMin
    while x < xMax+1:
        clean = True
        for sensor, manhattan in sensors.items():
            if calculateDist(x, y, sensor[0], sensor[1]) <= manhattan:
                x = sensor[0] + (manhattan - abs(sensor[1] - y)) + 1
                clean = False
                break
        if clean:
            print(f"{x},{y} = {x*4000000+y}")
            exit(0)