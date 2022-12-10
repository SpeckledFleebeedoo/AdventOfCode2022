
def drawDisplay(display):
    a = display.copy()
    for i, r in enumerate(a):
        a[i] = "".join(r)
    print("\n".join(a))

with open("day10/input.txt") as f:
    lines = f.read().splitlines()

cycle = 1
register = 1

signalstrengths = []
cyclestocheck = [x for x in range(19, 221, 40)]
display = [[" " for _ in range(40)]for _ in range(6)]
row = 0
col = 0
spritepos = 0

instruction = None
currentline = 0
wait = False

while cycle <= 239:
    #draw on display
    row = (cycle)//40
    col = (cycle) % 40
    if abs(register - (col-1)) <= 1:
        display[row][col-1] = "#"
    # else:
    #     display[row][col-1] = ":"
    drawDisplay(display)

    if instruction:
        # Execute instruction
        register += instruction
        instruction = None
    else:
        # Read next instruction
        line = lines[currentline]
        currentline += 1
        if line[0:4] == "noop":
            instruction = None
        elif line[0:4] == "addx":
            instruction = int(line[5:])
    
    if cycle in cyclestocheck:
        signalstrengths.append((cycle + 1) * register)

    cycle += 1

print(sum(signalstrengths))

drawDisplay(display)
pass