import numpy as np

#Read data
with open("day17/input.txt") as f:
    instructions = f.read()

#Define sequence of rocks
rocks = [
    np.array([[1, 1, 1, 1]]),
    np.array([[0,1,0],
              [1,1,1],
              [0,1,0]]),
    np.array([[0,0,1],
              [0,0,1],
              [1,1,1]]),
    np.array([[1],
              [1],
              [1],
              [1]]),
    np.array([[1,1],
              [1,1]])
]

#Map starts as floor only
map = np.array([[1,1,1,1,1,1,1,1,1]])

i = 0   #Instruction counter
totalheight = 0
knownstates = []
heights = []

for r in range(2022):
    rock = rocks[r%5]

    #Space between current map and new rock
    addon = np.array([[1,0,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,0,1]])
    width = rock.shape[1]
    height = rock.shape[0]
    
    #Piece of map with new rock
    rockaddon = np.array([[1,0,0,0,0,0,0,0,1] for _ in range(height)])
    rockpos = (0, 3)
    touchdown = False
    
    #Stack existing map, empty space and rock
    rowsadded = len(rockaddon) + len(addon)
    map = np.concatenate((rockaddon, addon, map), axis=0)
    while not touchdown:
        #Read current instruction
        gasjet = instructions[i%len(instructions)]
        i += 1
        if gasjet == ">":
            trycoords = (rockpos[0], rockpos[1]+1)
        elif gasjet == "<":
            trycoords = (rockpos[0], rockpos[1]-1)

        #Create copy of map and add rock array to it
        testmap = map.copy()
        testmap[trycoords[0]:trycoords[0]+height, trycoords[1]:trycoords[1]+width] += rock

        #Check if rock overlaps with edges
        if not 2 in testmap:
            rockpos = trycoords

        #Repeat for moving down
        trycoords = (rockpos[0]+1, rockpos[1])
        testmap = map.copy()
        testmap[trycoords[0]:trycoords[0]+height, trycoords[1]:trycoords[1]+width] += rock
        if not 2 in testmap:
            rockpos = trycoords

        #Place landed rock in map, strip empty lines from top of map
        else:
            map[rockpos[0]:rockpos[0]+height, rockpos[1]:rockpos[1]+width] += rock
            touchdown = True

    #Trim map
    for y, row in enumerate(map):
        if np.count_nonzero(row) != 2:
            rowsremoved = y
            break 
    map = np.delete(map, np.s_[:y], 0)

    totalheight += (rowsadded - rowsremoved)
    heights.append(totalheight)

    #Calculate state
    s1, s2, s3, s4, s5, s6, s7 = [np.where(map[:,i] == 1)[0][0] for i in range(1, 8)]
    state = [i%len(instructions), r%len(rocks), s1, s2, s3, s4, s5, s6, s7]
    if state in knownstates:
        index = knownstates.index(state)
        break

    #Trim bottom of map
    knownstates.append(state)
    lowest = max(s1, s2, s3, s4, s5, s6, s7)
    map = np.delete(map, np.s_[lowest+21:], 0)

preloopheight = heights[index]
loopheight = totalheight - preloopheight
rocksinloop = r - index
loopstofill = (1000000000000 - index) // rocksinloop
rocksremaining = (1000000000000 - index) % rocksinloop
loopheight = loopstofill * loopheight
totalheight = heights[index + rocksremaining] + loopheight - 1

print(totalheight)