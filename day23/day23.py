from PIL import Image

def check_surroundings(elf, elves):
    if ((elf[0]-1, elf[1]-1) not in elves and
        (elf[0]-1, elf[1]) not in elves and
        (elf[0]-1, elf[1]+1) not in elves and
        (elf[0], elf[1]+1) not in elves and
        (elf[0]+1, elf[1]+1) not in elves and
        (elf[0]+1, elf[1]) not in elves and
        (elf[0]+1, elf[1]-1) not in elves and
        (elf[0], elf[1]-1) not in elves):
        return True
    return False

def check_north(elf, elves):
    if (elf[0]-1, elf[1]-1) not in elves and (elf[0]-1, elf[1]) not in elves and (elf[0]-1, elf[1]+1) not in elves: #north
        return True
    return False

def check_south(elf, elves):
    if (elf[0]+1, elf[1]-1) not in elves and (elf[0]+1, elf[1]) not in elves and (elf[0]+1, elf[1]+1) not in elves: #south
        return True
    return False

def check_west(elf, elves):
    if (elf[0]-1, elf[1]-1) not in elves and (elf[0], elf[1]-1) not in elves and (elf[0]+1, elf[1]-1) not in elves: #west
        return True
    return False

def check_east(elf, elves):
    if (elf[0]-1, elf[1]+1) not in elves and (elf[0], elf[1]+1) not in elves and (elf[0]+1, elf[1]+1) not in elves: #east
        return True
    return False

def draw_map(elves, xmin, xmax, ymin, ymax):
    xoffset = -xmin
    yoffset = -ymin
    lines = [["." for x in range(xmax-xmin+1)] for y in range(ymax-ymin+1)]
    for elf in elves:
        lines[elf[0]+yoffset][elf[1]+xoffset] = "#"
    lines = ["".join(line) for line in lines]
    out = "\n".join(lines)
        
    with open("day23/output.txt", "w+") as f:
        f.write(out)

def draw_frame(elves, xmin, xmax, ymin, ymax):
    xoffset = -xmin
    yoffset = -ymin
    frame = Image.new("RGB", (140, 140), "grey")
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax):
            if (y, x) in elves:
                position  = (x+xoffset, y+yoffset)
                frame.putpixel(position, (30, 255, 30))
    return frame

with open("day23/input.txt") as f:
    lines = f.read().splitlines()

elves = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            elves.append((y, x))

directions = [check_north, check_south, check_west, check_east]
steps = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
dir = 0

xmin = min([elf[1] for elf in elves])
xmax = max([elf[1] for elf in elves])
ymin = min([elf[0] for elf in elves])
ymax = max([elf[0] for elf in elves])
# draw_map(elves, xmin, xmax, ymin, ymax)

frames = []
frames.append(draw_frame(elves, -15, 118, -12, 116))

elvesmoved = True
rounds = 0
# for i in range(10):
while elvesmoved == True:
    elvesmoved = False
    wantedcoordinates = []
    for elf in elves:
        if check_surroundings(elf, elves):
            wantedcoordinates.append(elf)
        elif directions[dir](elf, elves):
            wantedcoordinates.append((elf[0]+steps[dir][0], elf[1]+steps[dir][1]))
        elif directions[(dir+1)%4](elf, elves):
            wantedcoordinates.append((elf[0]+steps[(dir+1)%4][0], elf[1]+steps[(dir+1)%4][1]))
        elif directions[(dir+2)%4](elf, elves):
            wantedcoordinates.append((elf[0]+steps[(dir+2)%4][0], elf[1]+steps[(dir+2)%4][1]))
        elif directions[(dir+3)%4](elf, elves):
            wantedcoordinates.append((elf[0]+steps[(dir+3)%4][0], elf[1]+steps[(dir+3)%4][1]))
        else: wantedcoordinates.append(elf)

    movecoordinates = []
    for elf, coordinate in zip(elves, wantedcoordinates):
        if wantedcoordinates.count(coordinate) > 1:
            movecoordinates.append((elf[0], elf[1]))
        else:
            movecoordinates.append(coordinate)
            if coordinate != elf:
                elvesmoved = True

    for i, coordinate in enumerate(movecoordinates):
        elves[i] = coordinate
    
    dir = (dir + 1) % 4
    
    xmin = min([elf[1] for elf in elves])
    xmax = max([elf[1] for elf in elves])
    ymin = min([elf[0] for elf in elves])
    ymax = max([elf[0] for elf in elves])
    if rounds%10 == 0 or elvesmoved == False:
        # draw_map(elves, xmin, xmax, ymin, ymax)
        frames.append(draw_frame(elves, -15, 118, -12, 116))
        print(rounds)

    rounds += 1

# area = (xmax-xmin+1) * (ymax-ymin+1)
# emptytiles = area - len(elves)
# print(emptytiles)
print(rounds)
frames[0].save("day23/day23.gif", save_all = True, append_images=frames[1:])

#Final result: 128*134