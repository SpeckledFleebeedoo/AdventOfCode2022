import numpy as np
from PIL import Image

def printmap(map):
    map = map[:, 330:671]
    img = Image.new("RGB", (340, 180), "white")
    for y in range(165):
        for x in range(340):
            if map[y, x] == 1:
                img.putpixel((x, y+8), (0, 0, 0))
            elif map[y, x] == 2:
                img.putpixel((x, y+8), (194, 178, 128))
    img.save("day14/output.png")

with open("day14/input.txt") as f:
    lines = f.read().splitlines()
    # xmax: 504
    # xmin: 449
    # ymax: 161

map = np.zeros((165, 1000), dtype=np.uint8)
map[163] = 1
for line in lines:
    coordinates = line.split(" -> ")
    for i in range(len(coordinates)-1):
        x1, y1 = [int(c) for c in coordinates[i].split(",")]
        x2, y2 = [int(c) for c in coordinates[i+1].split(",")]
        xmax = max(x1, x2)
        xmin = min(x1, x2)
        ymax = max(y1, y2)
        ymin = min(y1, y2)
        map[ymin:ymax+1, xmin:xmax+1] = 1
        pass

finished = False
while not finished:
    sandpos = [0, 500]
    while True:
        if map[0, 500] == 2:
        # if sandpos[0] == 170:
            finished = True
            break
        scanarea = map[sandpos[0]+1, sandpos[1]-1:sandpos[1]+2]
        if scanarea[1] == 0:
            sandpos[0] += 1
        elif scanarea[0] == 0:
            sandpos[0] += 1
            sandpos[1] -= 1
        elif scanarea[2] == 0:
            sandpos[0] += 1
            sandpos[1] += 1
        else:
            map[sandpos[0], sandpos[1]] = 2
            break

print(np.count_nonzero(map==2))
printmap(map)