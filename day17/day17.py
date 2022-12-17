import numpy as np

#Read data
with open("day17/input.txt") as f:
    instructions = f.read()
print(len(instructions))

#Define sequence of rocks
rocks = [
    np.array([1, 1, 1, 1]),
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

for r in range(1000000000000):
    rock = rocks[r%5]
    if r%1000==0:
        print(r)

    #Space between current map and new rock
    addon = np.array([[1,0,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,0,1]])
    if len(rock.shape) == 1:
        width = rock.shape[0]
        height = 1
    else:
        width = rock.shape[1]
        height = rock.shape[0]
    
    #Piece of map with new rock
    rockaddon = np.array([[1,0,0,0,0,0,0,0,1] for _ in range(height)])
    rockpos = (0, 3)
    touchdown = False
    
    #Stack existing map, empty space and rock
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
        testmap = map[0:50].copy()
        testmap[trycoords[0]:trycoords[0]+height, trycoords[1]:trycoords[1]+width] += rock
        if not 2 in testmap:
            rockpos = trycoords

        #Place landed rock in map, strip empty lines from top of map
        else:
            touchdown = True
            map[rockpos[0]:rockpos[0]+height, rockpos[1]:rockpos[1]+width] += rock
            for row in map:
                if np.count_nonzero(row) == 2:
                    map = np.delete(map, 0, 0)
        toremove = len(map) - 50
        if toremove > 0:
            map = np.delete(map, np.s_[51:], 0)
        totalheight += toremove

print(map.shape[0]-1+totalheight)   #Correct for floor...