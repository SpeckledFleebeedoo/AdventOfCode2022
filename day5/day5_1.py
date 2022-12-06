from collections import deque

def readstacks(containers):
    numstacks = int(containers[-1].strip()[-1])
    stacks = [deque() for i in range(numstacks)]
    for line in containers[:-1]:
        line = line.strip()
        for stack in range(numstacks):
            container = line[4*stack:4*stack+4].strip("[] ")
            if container != "":
                stacks[stack].appendleft(container)
    return stacks

def movecontainers(instruction, stacks):
    commands = instruction.strip().split(" ")
    numcontainers = int(commands[1])
    source = int(commands[3]) - 1
    destination = int(commands[5]) - 1
    for i in range(numcontainers):
        stacks[destination].append(stacks[source][-1])
        stacks[source].pop()
    return stacks
            
with open("day5/input.txt") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip() == "":
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