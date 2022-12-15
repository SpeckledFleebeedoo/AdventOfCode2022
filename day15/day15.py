import numpy as np

grid = np.zeros((16, 16))
center = (8,8) #y, x
radius = 6

for i in range(-radius, radius+1):
    linenum = center[0] + i
    horizontaldist = radius - abs(i)
    grid[linenum, center[1]-horizontaldist:center[1]+horizontaldist+1] = 1
    pass
pass