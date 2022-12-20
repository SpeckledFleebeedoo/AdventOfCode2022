def mix(valuelist):
    numvalues = len(values)
    for i in range(numvalues+1):
        for pos, val in enumerate(valuelist):
            if val[1] != i:
                continue
            newpos = (pos + val[0]) % (numvalues-1)
            if newpos == 0:
                del valuelist[pos]
                valuelist.append([val[0], True])
            else:
                del valuelist[pos]
                valuelist.insert(newpos, [val[0], True])
            break
    return valuelist

def calc_coordinates(valuelist, numvalues):
    for i, val in enumerate(valuelist):
        if val[0] == 0:
            break

    #3x Move right 1000
    pos1 = (i + 1000) % numvalues
    if pos1 >= numvalues:
        pos1 = pos1 - numvalues
    pos2 = (i + 2000) % numvalues
    if pos2 >= numvalues:
        pos2 = pos2 - numvalues
    pos3 = (i + 3000) % numvalues
    if pos3 >= numvalues:
        pos3 = pos3 - numvalues
    
    #sum numbers
    n1 = valuelist[pos1][0]
    n2 = valuelist[pos2][0]
    n3 = valuelist[pos3][0]
    print(sum([n1, n2, n3]))

def part1(valuelist):
    numvalues = len(values)
    valuelist = mix(valuelist)

    #Find 0
    calc_coordinates(valuelist, numvalues)

def part2(key, valuelist):
    numvalues = len(values)

    #multiply each number by key
    valuelist = [[val[0]*key, val[1]] for val in valuelist]

    #mix 10 times
    for i in range(10):
        valuelist = mix(valuelist)
        pass
    calc_coordinates(valuelist, numvalues) 

with open("day20/inputtest.txt") as f:
    values = f.read().splitlines()

valuelist = [[int(value), i] for i, value in enumerate(values)]
key = 811589153
part1(valuelist)
# part2(key, valuelist)