import numpy as np

with open("day18/input.txt") as f:
    blocks = [(int(b.split(",")[0]), int(b.split(",")[1]), int(b.split(",")[2])) for b in f.read().splitlines()]

uncoveredsides = 0
for b in blocks:
    above = (b[0], b[1], b[2]+1)
    if not above in blocks:
        uncoveredsides += 1
    below = (b[0], b[1], b[2]-1)
    if not below in blocks:
        uncoveredsides += 1
    before = (b[0], b[1]-1, b[2])
    if not before in blocks:
        uncoveredsides += 1
    after = (b[0], b[1]+1, b[2])
    if not after in blocks:
        uncoveredsides += 1
    left = (b[0]-1, b[1], b[2])
    if not left in blocks:
        uncoveredsides += 1
    right = (b[0]+1, b[1], b[2])
    if not right in blocks:
        uncoveredsides += 1

print(uncoveredsides)