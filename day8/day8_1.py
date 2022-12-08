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
visibilitygrid = np.ones(treeheightgrid.shape)

treestocheck = treeheightgrid[1:-1, 1:-1]
visibilitygrid[1:-1, 1:-1] = np.zeros(treestocheck.shape)

for j, row in enumerate(treestocheck):
    for i, tree in enumerate(row):
        x, y = i+1, j+1
        east = treeheightgrid[y, x+1:].max()
        west = treeheightgrid[y, :x].max()
        north = treeheightgrid[:y, x].max()
        south = treeheightgrid[y+1:, x].max()
        if tree > east or tree > west or tree > north or tree > south:
            visibilitygrid[y, x] = 1

numvisibletrees = np.count_nonzero(visibilitygrid)
print(numvisibletrees)