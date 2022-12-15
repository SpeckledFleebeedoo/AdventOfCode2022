import re

def mark_diamond(grid, center, radius):
    for i in range(-radius, radius+1):
        linenum = center[0] + i
        horizontaldist = radius - abs(i)
        grid[linenum, center[1]-horizontaldist:center[1]+horizontaldist+1] = 1
        pass

with open("day15/input.txt") as f:
    lines = f.read().splitlines()

coordinates = []
for line in lines:
    coordinates.append([int(x) for x in re.findall("-*\d+", line)]) #[SensorX, SensorY, BeaconX, BeaconY]

pairs = []

for coord1 in coordinates:
    s1x, s1y, b1x, b1y = coord1
    radius1 = abs(s1x - b1x) + abs(s1y - b1y)

    # Calculate top and bottom of each diamond
    diamondtop = (s1y - radius1, s1x)
    diamondbottom = (s1y + radius1, s1x)

    # Find diaminds with a distance of 2 between their edge and the top or bottom of the first diamond
    for coord2 in coordinates:
        s2x, s2y, b2x, b2y = coord2
        radius2 = abs(s2x - b2x) + abs(s2y - b2y)
        distancetotop = abs(diamondtop[0] - s2y) + abs(diamondtop[1] - s2x)
        distancetobottom = abs(diamondbottom[0] - s2y) + abs(diamondbottom[1] - s2x)

        # Find squation of line going between diamonds (y=ax+b)
        if distancetotop - radius2 == 2:
            if s2x < diamondtop[1]:
                a = -1
                b = diamondtop[0] + diamondtop[1] - 1
            else:
                a = 1
                b = diamondtop[0] - diamondtop[1] - 1
            pairs.append([a, b])
        if distancetobottom - radius2 == 2:
            if s2x < diamondbottom[1]:
                a = 1
                b = diamondbottom[0] - diamondbottom[1] + 1
            else:
                a = -1
                b = diamondbottom[0] + diamondbottom[1] + 1
            pairs.append([a, b])

# Find intersection between lines (a1x+b1 = a2x * b2)
line1, line2 = pairs
x = (line1[1] - line2[1]) / (line2[0] - line1[0])
y = line1[0] * x + line1[1]

print(x*4000000 + y)