def compare(l1, l2):
    i = 0
    while True:
        try:
            a = type(l1)
            b = type(l2)
            if a == int and b == int:
                if l1 < l2:
                    return True
                elif l1 > l2:
                    return False
                else: 
                    return None
            elif a == list and b == list:
                result = compare(l1[i], l2[i])
                if result is not None:
                    return result
                else: i += 1
            elif a == list and b == int:
                return compare(l1, [l2])
            elif a == int and b == list:
                return compare([l1], l2)
        except IndexError:
            if len(l1) < len(l2):
                return True
            elif len(l1) > len(l2):
                return False
            else: 
                return None

with open("day13/input.txt") as f:
    packets = [eval(p) for p in f.read().splitlines() if p != ""]

div1 = [[2]]
packets.append(div1)
div2 = [[6]]
packets.append(div2)
swaps = 10000

while swaps > 0:
    swaps = 0
    for i in range(len(packets)-1):
        p1 = packets[i]
        p2 = packets[i+1]
        ordered = compare(p1, p2)
        if not ordered:
            packets[i], packets[i+1] = packets[i+1], packets[i]
            swaps += 1

div1index = packets.index(div1) + 1
div2index = packets.index(div2) + 1
print(div1index * div2index)