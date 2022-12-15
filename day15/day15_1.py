import numpy as np
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

minx, miny, maxx, maxy = 0, 0, 0, 0
for coord in coordinates:
    sx, sy, bx, by = coord
    radius = abs(sx - bx) + abs(sy - by)
    if sx - radius < minx:
        minx = sx - radius
    if sx + radius > maxx:
        maxx = sx + radius
    if sy - radius < miny:
        miny = sy - radius
    if sy + radius > maxy:
        maxy = sy + radius

linenum = 2000000
line = np.zeros(maxx-minx)
for coord in coordinates:
    sx, sy, bx, by = coord
    radius = abs(sx - bx) + abs(sy - by)
    verticaldist = abs(sy-linenum)
    horizontaldist = radius - verticaldist
    if horizontaldist > 0:
        line[sx-horizontaldist-minx:sx+horizontaldist+1-minx] = 1
        if sy == linenum:
            line[sx-minx] = 2
        if by == linenum:
            line[bx-minx] = 3
        

    
print(np.count_nonzero(line==1))

pass