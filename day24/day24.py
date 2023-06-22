class Blizzard:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self):
        if self.direction == "v":
            self.position = (self.position[0] + 1, self.position[1])
        elif self.direction == "^":
            self.position = (self.position[0] - 1, self.position[1])
        elif self.direction == ">":
            self.position = (self.position[0], self.position[1] + 1)
        elif self.direction == "<":
            self.position = (self.position[0], self.position[1] - 1)
        
        global mapwidth
        global mapheight
        if self.position[0] == 0:
            self.position = (mapheight-2, self.position[1])
        elif self.position[0] == mapheight-1:
            self.position = (1, self.position[1])
        elif self.position[1] == 0:
            self.position = (self.position[0], mapwidth-2)
        elif self.position[1] == mapheight-1:
            self.position = (self.position[0], 1)
            
with open("day24/inputtest.txt") as f:
    lines = f.read().splitlines()

mapwidth = len(lines[0])-2
mapheight = len(lines[0][0])-2

blizzards = []
boundaries = []
boundaries.append((-1,1))
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in "^v><":
            blizzards.append(Blizzard((y, x), char))
        elif char == "#":
            boundaries.append((y,x))


start = (0, 1)
goal = (mapheight-1, mapwidth-2)

possiblepositions = [start]

turns = 0
while goal not in possiblepositions:
    nextposlist = []
    turns += 1
    for blizzard in blizzards:
        blizzard.move()
    blizzardpositions = [blizzard.position for blizzard in blizzards]
    for pos in possiblepositions:
        up = (pos[0]-1, pos[1])
        if not up in boundaries and not up in blizzardpositions:
            nextposlist.append(up)
        down = (pos[0]+1, pos[1])
        if not down in boundaries and not down in blizzardpositions:
            nextposlist.append(down)
        right = (pos[0], pos[1]+1)
        if not right in boundaries and not right in blizzardpositions:
            nextposlist.append(right)
        left = (pos[0], pos[1]-1)
        if not left in boundaries and not left in blizzardpositions:
            nextposlist.append(left)
        if not pos in boundaries and not pos in blizzardpositions:
            nextposlist.append(pos)
    possiblepositions = list(set(nextposlist))
    pass

print(turns)
