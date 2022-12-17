import re

class Node:
    def __init__(self, flowrate: int, connections: list[str]):
        self.connections = connections
        self.flowrate = flowrate
        self.opened = False

with open("day16/input.txt") as f:
    lines = f.read().splitlines()

nodes = {}

for line in lines:
    id = line[6:8]
    flowrate = int(re.findall(r"\d+", line)[0])
    words = line.split()
    connections = [word.strip(",") for word in words[9:]]
    nodes[id] = Node(flowrate, connections)

currentnode = "AA"
for step in range(30):



"""
1: find remaining value of all nodes
    value = (minutes left - minutes to get to and open node) * node flow rate
2: go to node with highest value
3: repeat for 30 steps
"""