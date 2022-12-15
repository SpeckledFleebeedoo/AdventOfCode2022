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

grid = np.zeros((maxy-miny, maxx-minx))
# center = (8,8) #y, x
# radius = 6
# mark_diamond(grid, center, radius)
pass