import numpy as np

def findviewdist(viewpath, tree):
    try:
        view = np.argwhere(viewpath >= tree)[0][0] + 1
    except:
        view = viewpath.size
    return view

with open("day8/input.txt") as f:
    lines = f.read().splitlines()

treeheightgrid = np.array([[int(d) for d in list(line)] for line in lines])
scenicscoregrid = np.zeros(treeheightgrid.shape)

treestocheck = treeheightgrid[1:-1, 1:-1]

for j, row in enumerate(treestocheck):
    for i, tree in enumerate(row):
        x, y = i+1, j+1

        east = treeheightgrid[y, x+1:]
        eastview = findviewdist(east, tree)
        west = np.flip(treeheightgrid[y, :x])
        westview = findviewdist(west, tree)
        north = np.flip(treeheightgrid[:y, x])
        northview = findviewdist(north, tree)
        south = treeheightgrid[y+1:, x]
        southview = findviewdist(south, tree)
        scenicscoregrid[y, x] = eastview * westview * northview * southview

print(scenicscoregrid.max())