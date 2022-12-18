import numpy as np

with open("day18/input.txt") as f:
    blocks = [(int(b.split(",")[0]), int(b.split(",")[1]), int(b.split(",")[2])) for b in f.read().splitlines()]

box = np.ones((26,26,26), dtype = np.uint8)
box[1:25, 1:25,1:25] = np.zeros((24,24,24), dtype = np.uint8)

for b in blocks:
    box[b[0]+3, b[1]+3, b[2]+3] = 2 # 0 = empty space, 1 = outside wall, 2 = rock, 3 = flooded

offsets = [np.array([1, 0, 0]), np.array([-1, 0, 0]), np.array([0, 1, 0]), np.array([0, -1, 0]), np.array([0, 0, 1]), np.array([0, 0, -1])]

queue = [(1,1,1)]
while len(queue) != 0:
    c = queue[0]
    del queue[0]
    if box[c[0], c[1], c[2]] == 0:
        box[c[0], c[1], c[2]] = 3
        for offset in offsets:
            queue.append(c+offset)

uncoveredsides = 0
floodedblocks = np.transpose(np.nonzero(box == 3))

for b in floodedblocks:
    for offset in offsets:
        tile = b + offset
        if box[tile[0], tile[1], tile[2]] == 2:
            uncoveredsides += 1

print(uncoveredsides)