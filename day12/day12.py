import numpy as np
from collections import deque
from time import sleep

heights = "SabcdefghijklmnopqrstuvwxyzE"

class Tile:
    def __init__(self, char, y, x):
        self.y = y
        self.x = x
        self.height = heights.index(char)
        self.parent = None
        self.chainlen = 0
        self.visited = False

with open("day12/input.txt") as f:
    lines = f.read().splitlines()

map = []

for l, line in enumerate(lines):
    map.append([])
    for p, char in enumerate(line):
        tile = Tile(char, l, p)
        map[l].append(tile)
        if char == "S":
            root = tile
        if char == "E":
            goal = tile

def adjacenttiles(map, node):
    adjacent = []
    if node.y > 0:
        top = map[node.y-1][node.x]
        if top.height - node.height <= 1:
            adjacent.append(top)
    if node.y < len(map)-1:
        bottom = map[node.y+1][node.x]
        if bottom.height - node.height <= 1:
            adjacent.append(bottom)
    if node.x > 0:
        left = map[node.y][node.x-1]
        if left.height - node.height <= 1:
            adjacent.append(left)
    if node.x < len(map[0])-1:
        right = map[node.y][node.x+1]
        if right.height - node.height <= 1:
            adjacent.append(right)
    return adjacent

def BFS(goal, root, map):
    q = deque() #Tile objects
    root.visited = True
    q.append(root)
    while len(q) != 0:
        # writeVisitedMap(map)
        nodetocheck = q[0]
        q.popleft()
        # if map[nodetocheck[0]][nodetocheck[1]].height == 1:
        if nodetocheck == goal:
            return nodetocheck
        for tile in adjacenttiles(map, nodetocheck):
            if not tile.visited:
                tile.visited = True
                tile.parent = nodetocheck
                tile.chainlen = nodetocheck.chainlen + 1
                q.append(tile)

def writeVisitedMap(map):
    global out
    out = ""
    for l in map:
        for c in l:
            if c.visited:
                out += ":"
            else:
                out += "."
        out += "\n"
    with open("day12/output.txt", "w") as f:
        f.write(out)
    # sleep(0.05)

def drawPath(goal):
    global lines
    # lines = out.splitlines()
    currenttile = goal
    for i in range(goal.chainlen+1):
        x = currenttile.x
        y = currenttile.y
        line = list(lines[y])
        line[x] = "■"
        lines[y] = "".join(line)
        currenttile = currenttile.parent
    out = "\n".join(lines)
    with open("day12/output.txt", "w") as f:
        f.write(out)

result = BFS(goal, root, map)
print(result.chainlen)
drawPath(result)
pass
