import numpy as np

def checktile(map, coord):
    if map[coord[0], coord[1]] == 2:
        return False
    elif map[coord[0], coord[1]] == 1:
        return True

def walk(instruction, map, state):
    additionfactors = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    for _ in range(instruction):
        newcoords = state[0:2]+additionfactors[state[2]]
        newcoords[0] = newcoords[0]%(len(map[0])-1)
        newcoords[1] = newcoords[1]%(len(map[:,0])-1)
        if map[newcoords[0], newcoords[1]] == 0:
            if state[2] == 0:
                if checktile(map, (state[0], np.nonzero(map[state[0]])[0][0])):
                    state[0:2] = (state[0], np.nonzero(map[state[0]])[0][0])
                else:
                    break
            elif state[2] == 1:
                if checktile(map, (np.nonzero(map[:, state[0]])[0][0], state[1])):
                    state[0:2] = (np.nonzero(map[:, state[0]])[0][0], state[1])
                else:
                    break
            elif state[2] == 2:
                if checktile(map, (state[0], np.nonzero(map[state[0]])[0][-1])):
                    state[0:2] = (state[0], np.nonzero(map[state[0]])[0][-1])
                else:
                    break
            elif state[2] == 3:
                if checktile(map, (np.nonzero(map[:, state[0]])[0][-1], state[1])):
                    state[0:2] = (np.nonzero(map[:, state[0]])[0][-1], state[1])
                else:
                    break
        else: 
            if checktile(map, state[0:2]+additionfactors[state[2]]):
                # state[0:2] += additionfactors[state[2]]
                state[0] += additionfactors[state[2]][0]
                state[1] += additionfactors[state[2]][1]
            else:
                break
    return state

with open("day22/input_map.txt") as m:
    maplines = m.read().splitlines()
with open("day22/input_instruction.txt") as f:
    instructions = f.read()

mapwidth = max([len(l) for l in maplines])
mapheight = len(maplines)
charmapping = {".": 1, "#": 2, " ": 0}

map = np.zeros((mapheight, mapwidth), dtype=np.int8)
for y, line in enumerate(maplines):
    for x, char in enumerate(line):
        map[y, x] = charmapping[char]

state = np.array([0, np.nonzero(map[0])[0][0], 0])

i = 0
while i < len(instructions):
    if instructions[i].isnumeric():
        if instructions[i+1].isnumeric():
            instruction = int(instructions[i:i+2])
            i += 2
        else:
            instruction = int(instructions[i])
            i += 1
        state = walk(instruction, map, state)
    elif instructions[i] == "R":
        state[2] += 1
        state[2] = state[2]%4
        i += 1
    elif instructions[i] == "L":
        state[2] -= 1
        state[2] = state[2]%4
        i += 1

print(state[0]*1000 + state[1]*4 + state[2])