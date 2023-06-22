def decodeSNAFU(num:str):
    charmap = {"2": 2,
               "1": 1,
               "0": 0,
               "-": -1,
               "=": -2}
    value = 0
    for i, char in enumerate(num[::-1]):
        magnitude = 5**i
        value += (magnitude * charmap[char])
    return value

def encodeSNAFU(num:int):
    charmap = {2: "2",
               1: "1",
               0: "0",
               -1: "-",
               -2: "="}

    value = {}
    remainder = num
    while remainder != 0:
        i = 0
        while (5**(i+1))/2 < abs(remainder):
            i += 1
        c = 1
        if abs(remainder) > 2*5**i - (5**(i))/2:
            c = 2
        if remainder < 0:
            c = -c
        remainder -= c*5**i
        value[i] = charmap[c]

        for i in range(max(value.keys()), -1, -1):
            if not i in value.keys():
                value[i] = charmap[0]
        # value = sorted(value)

    value = "".join(value.values())
    return value

with open("day25/input.txt") as f:
    lines = f.read().splitlines()

totalfuel = 0
for line in lines:
    totalfuel += decodeSNAFU(line)
print(encodeSNAFU(totalfuel))

"""
2====: 938
12222: 937
10000: 625
1====: 313
 2222: 312


 1=1: 16
 1=0: 15
 1=-: 14
 1==: 13
  22: 12
  21: 11
  20: 10
  2-: 9
  2=: 8
  12: 7
  11: 6
  10: 5
  1-: 4
  1=: 3
   2: 2
   1: 1

"""