with open("day20/inputtest.txt") as f:
    values = f.read().splitlines()

valuelist = [[int(value), False] for value in values]
numvalues = len(values)

for i in range(numvalues+1):
    for pos, val in enumerate(valuelist):
        if not val[1]:
            newpos = pos + val[0]
            if newpos > 0:
                newpos += 1
                if newpos > numvalues:
                    newpos = newpos % numvalues
                
                valuelist.insert(newpos, [val[0], True])
                del valuelist[pos]
            elif newpos == 0:
                valuelist.append([val[0], True])
                del valuelist[pos]
            else: 
                valuelist.insert(newpos, [val[0], True])
                del valuelist[pos]
            break

pass