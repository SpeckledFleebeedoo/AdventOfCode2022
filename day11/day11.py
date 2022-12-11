class Monkey:
    def __init__(self, helditems: list, operation, test, true, false):
        self.helditems = helditems
        self.operation = operation
        self.test = lambda x: x%test == 0
        self.true = true
        self.false = false
        self.inspected = 0
    
    def inspect(self):
        tothrow = []
        for index, item in enumerate(self.helditems):
            newlevel = self.operation(item)
            reducedlevel = newlevel#//3
            testresult = self.test(reducedlevel)
            if testresult:
                target = self.true
            else:
                target = self.false
            tothrow.append([reducedlevel, target])
            self.inspected += 1
        self.throw(tothrow)
        self.helditems = []

    def throw(self, itemstothrow):
        for worrylevel, targetid in itemstothrow:
            target = monkeylist[targetid]
            target.helditems.append(worrylevel)
        pass

monkeylist = {}

monkeylist[0] = Monkey([59, 74, 65, 86], lambda old: old * 19, 7, 6, 2)
monkeylist[1] = Monkey([62, 84, 72, 91, 68, 78, 51], lambda old: old + 1, 2, 2, 0)
monkeylist[2] = Monkey([78, 84, 96], lambda old: old + 8, 19, 6, 5)
monkeylist[3] = Monkey([97, 86], lambda old: old * old, 3, 1, 0)
monkeylist[4] = Monkey([50], lambda old: old + 6, 13, 3, 1)
monkeylist[5] = Monkey([73, 65, 69, 65, 51], lambda old: old * 17, 11, 4, 7)
monkeylist[6] = Monkey([69, 82, 97, 93, 82, 84, 58, 63], lambda old: old + 5, 5, 5, 7)
monkeylist[7] = Monkey([81, 78, 82, 76, 79, 80], lambda old: old + 3, 17, 3, 4)

# monkeylist[0] = Monkey([79, 98], lambda old: old * 19, 23, 2, 3)
# monkeylist[1] = Monkey([54, 65, 75, 74], lambda old: old + 6, 19, 2, 0)
# monkeylist[2] = Monkey([79, 60, 97], lambda old: old * old, 13, 1, 3)
# monkeylist[3] = Monkey([74], lambda old: old + 3, 17, 0, 1)

pass

for round in range(10000):
    for i, monkey in monkeylist.items():
        monkey.inspect()
    pass

inspectedlist = [monkey.inspected for monkey in monkeylist.values()]
inspectedlist.sort()
top2 = inspectedlist[-2:]
monkeybusiness = top2[0] * top2[1]
print(monkeybusiness)
pass