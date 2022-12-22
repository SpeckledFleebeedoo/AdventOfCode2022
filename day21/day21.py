import re

def evalre(matchobj):
    if "humn" in matchobj.string:
        return matchobj.string
    return eval(matchobj.string)

class Monkey:
    def __init__(self, type, value = None, operation = None, inputs = None):
        self.type = type
        self.value = value
        self.operation = operation
        self.inputs = inputs
        self.inputvals = []
        self.inequation = False

    def execute_operation(self):
        if self.operation == "+":
            self.value = sum(self.inputvals)
        elif self.operation == "-":
            self.value = self.inputvals[0] - self.inputvals[1]
        elif self.operation == "*":
            self.value = self.inputvals[0] * self.inputvals[1]
        elif self.operation == "/":
            self.value = self.inputvals[0] // self.inputvals[1]
        elif self.operation == "==":
            self.value = self.inputvals[0] == self.inputvals[1]


with open("day21/input.txt") as f:
    lines = f.read().splitlines()

monkeys = {}
for line in lines:
    if line[6:].isnumeric():
        monkeys[line[:4]] = Monkey("input", value=int(line[6:]))
    else:
        monkeys[line[:4]] = Monkey("operation", inputs=[line[6:10], line[13:]], operation=line[11], value=None)

def part1(monkeys):
    notsolved = 1
    while notsolved != 0:
        notsolved = 0
        for monkey in monkeys.values():
            if monkey.type == "input":
                continue

            input1, input2 = monkey.inputs
            if monkeys[input1].value != None and monkeys[input2].value:
                monkey.inputvals = [monkeys[input1].value, monkeys[input2].value]
            if len(monkey.inputvals) == 2 and monkey.value == None:
                monkey.execute_operation()
            if monkey.value == None:
                notsolved += 1
        if monkeys["root"].value != None:
            print(monkeys["root"].value)
            break

def part2(monkeys):
    monkeys["root"].operation = "=="
    notallinequation = True
    
    equation = "root"
    while notallinequation:
        added = 0
        for key, monkey in monkeys.items():
            if monkey.inequation:
                continue
            if key == "humn":
                monkey.inequation = True
            if monkey.type == "operation":
                if str.find(equation, key) != -1:
                    eq = f"({monkey.inputs[0]} {monkey.operation} {monkey.inputs[1]})"
                    equation = str.replace(equation, key, eq)
                    added += 1
                    monkey.inequation = True
            if monkey.type == "input":
                if str.find(equation, key) != -1:
                    eq = str(monkey.value)
                    equation = str.replace(equation, key, eq)
                    added += 1
                    monkey.inequation = True
        if added == 0:
            notallinequation = False

part1(monkeys)
# part2(monkeys)