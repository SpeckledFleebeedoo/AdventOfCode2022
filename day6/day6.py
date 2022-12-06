with open("day6/input.txt") as f:
    data = f.read()

for i in range(14, len(data)):
    chars = set(data[i-14:i])
    if len(chars) == 14:
        print(i)
        break