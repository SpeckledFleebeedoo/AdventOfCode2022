with open("day3/input.txt") as f:
    rucksacks = f.readlines()

rucksacks = [r.strip() for r in rucksacks]

order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Part 1
total = 0
for r in rucksacks:
    l = int(len(r)/2)
    c1, c2 = r[:l], r[l:]
    common = None
    for c in c1:
        if c in c2:
            common = c
            prio = order.index(common) + 1
            total += prio
            break

print(total)

#Part 2
total = 0
numgroups = int(len(rucksacks)/3)
for g in range(numgroups):
    i = 3*g
    r1, r2, r3 = rucksacks[i:i+3]
    common = None
    for c in r1:
        if c in r2 and c in r3:
            common = c
            prio = order.index(common) + 1
            total += prio
            break

print(total)



