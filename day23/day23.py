with open("day23/input.txt") as f:
    lines = f.read().splitlines()

elves = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        elves.append([y, x])

wantedcoordinates = []
for elf in elves:
    if [elf[0]-1, elf[1]-1] not in elves and [elf[0]-1, elf[1]] not in elves and [elf[0]-1, elf[1]+1] not in elves: #north
        wantedcoordinates.append([elf[0]-1, elf[1]])
    elif [elf[0]+1, elf[1]-1] not in elves and [elf[0]+1, elf[1]] not in elves and [elf[0]+1, elf[1]+1] not in elves: #south
        wantedcoordinates.append([elf[0]+1, elf[1]])
    elif [elf[0]-1, elf[1]-1] not in elves and [elf[0], elf[1]-1] not in elves and [elf[0]+1, elf[1]-1] not in elves: #west
        wantedcoordinates.append([elf[0], elf[1]-1])
    elif [elf[0]-1, elf[1]+1] not in elves and [elf[0], elf[1]+1] not in elves and [elf[0]+1, elf[1]+1] not in elves: #east
        wantedcoordinates.append([elf[0], elf[1]+1])
    else: wantedcoordinates.append(elf)

