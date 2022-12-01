with open("input.txt") as text:
    contents = text.read()

elfs = contents.split("\n\n")
totals = []

for elf in elfs:
    vals = elf.split("\n")
    vals = [int(val) for val in vals]
    total = sum(vals)
    totals.append(total)

totals.sort()
max = sum(totals[-3:])
print(max)