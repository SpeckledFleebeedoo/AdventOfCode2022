def moveSegment(headcoordinate, tailcoordinate):
    #move tail right
    if headcoordinate["y"] == tailcoordinate["y"] and headcoordinate["x"] - tailcoordinate["x"] > 1:
        tailcoordinate["x"] = headcoordinate["x"] - 1
    #move tail left
    elif headcoordinate["y"] == tailcoordinate["y"] and tailcoordinate["x"] - headcoordinate["x"] > 1:
        tailcoordinate["x"] = headcoordinate["x"] + 1
    #move tail up
    elif headcoordinate["x"] == tailcoordinate["x"] and headcoordinate["y"] - tailcoordinate["y"] > 1:
        tailcoordinate["y"] = headcoordinate["y"] - 1
    #move tail down
    elif headcoordinate["x"] == tailcoordinate["x"] and tailcoordinate["y"] - headcoordinate["y"] > 1:
        tailcoordinate["y"] = headcoordinate["y"] + 1
    #move tail up right
    elif (headcoordinate["x"] - tailcoordinate["x"] == 2 and headcoordinate["y"] > tailcoordinate["y"]) or (headcoordinate["y"] - tailcoordinate["y"] == 2 and headcoordinate["x"] > tailcoordinate["x"]):
        tailcoordinate["x"] += 1
        tailcoordinate["y"] += 1
    #move tail up left
    elif (headcoordinate["x"] - tailcoordinate["x"] == -2 and headcoordinate["y"] > tailcoordinate["y"]) or (headcoordinate["y"] - tailcoordinate["y"] == 2 and headcoordinate["x"] < tailcoordinate["x"]):
        tailcoordinate["x"] -= 1
        tailcoordinate["y"] += 1
    #move tail down left
    elif (headcoordinate["x"] - tailcoordinate["x"] == -2 and headcoordinate["y"] < tailcoordinate["y"]) or (headcoordinate["y"] - tailcoordinate["y"] == -2 and headcoordinate["x"] < tailcoordinate["x"]):
        tailcoordinate["x"] -= 1
        tailcoordinate["y"] -= 1
    #move tail down right
    elif (headcoordinate["x"] - tailcoordinate["x"] == 2 and headcoordinate["y"] < tailcoordinate["y"]) or (headcoordinate["y"] - tailcoordinate["y"] == -2 and headcoordinate["x"] > tailcoordinate["x"]):
        tailcoordinate["x"] += 1
        tailcoordinate["y"] -= 1
    return tailcoordinate

with open("day9/input.txt") as f:
    lines = f.read().splitlines()

segmentcoordinates = [{"x": 0, "y": 0} for _ in range(10)]
visitedsquares = []

for instruction in lines:
    direction, distance = instruction.split()
    for i in range(int(distance)):
        for i, segment in enumerate(segmentcoordinates):
            if i == 0:
                if direction == "R":
                    segment["x"] += 1
                elif direction == "L":
                    segment["x"] -= 1
                elif direction == "U":
                    segment["y"] += 1
                elif direction == "D":
                    segment["y"] -= 1
            else:
                segment = moveSegment(segmentcoordinates[i-1], segment)

        visitedsquares.append((segmentcoordinates[-1]["x"], segmentcoordinates[-1]["y"]))

visitedsquares = set(visitedsquares)
print(len(visitedsquares))