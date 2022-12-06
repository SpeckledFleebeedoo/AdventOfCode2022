from collections import deque

def readstacks(containers):
    numstacks = int(containers[-1].split()[-1])
    stacks = [deque() for i in range(numstacks)]
    for line in containers[:-1]:
        for stack in range(numstacks):
            container = line[4*stack:4*stack+4].strip("[] ")
            if container != "":
                stacks[stack].appendleft(container)
    return stacks

def movecontainers(instruction, stacks):
    commands = instruction.split(" ")
    numcontainers = int(commands[1])
    source = int(commands[3]) - 1
    destination = int(commands[5]) - 1
    liftedstack = list(stacks[source])[-numcontainers:]
    stacks[destination] += deque(liftedstack)
    for _ in range(numcontainers):
        stacks[source].pop()
    pass

    return stacks
            
with open("day5/input.txt") as f:
    lines = f.read().splitlines()

for i, line in enumerate(lines):
    if line == "":
        containers = lines[:i]
        moves = lines[i+1:]
        break

containerstacks = readstacks(containers)
for line in moves:
    containerstacks = movecontainers(line, containerstacks)
output = ""
for stack in containerstacks:
    output += stack[-1]
print(output)