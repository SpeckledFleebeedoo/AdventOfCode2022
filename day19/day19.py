class Blueprint:
    def __init__(self, line: str):
        linesplit = line.split(" ")
        self.index = int(linesplit[1].strip(":"))
        self.ore_robot_cost = int(linesplit[6])
        self.clay_robot_cost = int(linesplit[12])
        self.obsidian_robot_cost = (int(linesplit[18]), int(linesplit[21]))
        self.geode_robot_cost = (int(linesplit[27]), int(linesplit[30]))
    
    def check_buildable_bots(self, resources):
        buildable = [0, 0, 0, 0]
        if resources[0] >= self.ore_robot_cost:
            buildable[0] = 1
        if resources[0] >= self.clay_robot_cost:
            buildable[1] = 1
        if resources[0] >= self.obsidian_robot_cost[0] and resources[1] >= self.obsidian_robot_cost[1]:
            buildable[2] = 1
        if resources[0] >= self.geode_robot_cost[0] and resources[2] >= self.geode_robot_cost[1]:
            buildable[3] = 1
        return buildable

class Node:
    def __init__(self, parent, action, resources, bots, time, buildable_bots):
        if parent == None:
            self.is_root = True
        self.parent: Node = parent
        # 0: wait, 1: ore bot, 2: clay bot, 3: obsidian bot, 4: geode bot
        self.action: str = action
        self.resources: list[int] = resources
        self.bots: list[int] = bots
        self.time: int = time
        self.buildable_bots: list[int] = buildable_bots

maxtime = 32
nodes_visited = 0
qualitylevels = []

with open("day19/input.txt") as f:
    lines = f.readlines()

blueprints: list[Blueprint] = []

# for line in lines:
for i in range(3):
    blueprints.append(Blueprint(lines[i]))

for bp in blueprints:
    root = Node(parent=None, action=0, resources=[0,0,0,0], bots=[1,0,0,0], time=0, buildable_bots=[0,0,0,0])
    queue = [root]
    top_node = root

    while len(queue) > 0:
        current = queue[-1]
        queue.pop()
        nodes_visited += 1

        timeleft = maxtime - current.time
        if timeleft == 0:
            if current.resources[3] >= top_node.resources[3]:
                top_node = current
            continue

        buildable_robots = bp.check_buildable_bots(current.resources)
        filtered_buildable_robots = buildable_robots[:]

        current.resources = [current.resources[i] + current.bots[i] for i in range(4)]
        
        # Maximum number of geodes that can still be generafted from current state
        max_future_geodes = current.bots[3] * timeleft + timeleft * (timeleft + 1) / 2
        if current.resources[3] + max_future_geodes <= top_node.resources[3]:
            continue

        # Check if more robots are needed, don't build if not.
        if current.bots[0] >= max(bp.ore_robot_cost, bp.clay_robot_cost, bp.obsidian_robot_cost[0], bp.geode_robot_cost[0]):
            filtered_buildable_robots[0] = 0
        
        if current.bots[1] >= bp.obsidian_robot_cost[1]:
            filtered_buildable_robots[1] = 0
        
        if current.bots[2] >= bp.geode_robot_cost[1]:
            filtered_buildable_robots[2] = 0
        
        # Avoid waiting when all robots can be built
        if not buildable_robots == [1, 1, 1, 1]:
            wait_node = Node(current, "wait", current.resources[:], current.bots[:], current.time + 1, buildable_robots)
            queue.append(wait_node)

        # Avoid being able to build a robot, waiting and then still building the same robot
        
        for i, can_build in enumerate(filtered_buildable_robots):
            if not can_build:
                continue

            new_resources = current.resources[:]
            new_bots = current.bots[:]

            if i == 0:
                if current.parent.action == "wait" and current.parent.buildable_bots[0]:
                    continue

                new_resources[0] -= bp.ore_robot_cost
                new_bots[0] += 1
                action = "ore bot"

            elif i == 1:
                if current.parent.action == "wait" and current.parent.buildable_bots[1]: # For some reason this line breaks a single blueprint in part 1...
                    continue

                new_resources[0] -= bp.clay_robot_cost
                new_bots[1] += 1
                action = "clay bot"

            elif i == 2: 
                if current.parent.action == "wait" and current.parent.buildable_bots[2]:
                    continue

                new_resources[0] -= bp.obsidian_robot_cost[0]
                new_resources[1] -= bp.obsidian_robot_cost[1]
                new_bots[2] += 1
                action = "obsidian bot"

            elif i == 3:

                new_resources[0] -= bp.geode_robot_cost[0]
                new_resources[2] -= bp.geode_robot_cost[1]
                new_bots[3] += 1
                action = "geode bot"

            queue.append(Node(current, action, new_resources, new_bots, current.time + 1, buildable_robots))

    print(bp.index, top_node.bots, top_node.resources, nodes_visited)
    # qualitylevels.append(bp.index * top_node.resources[3])
    qualitylevels.append(top_node.resources[3])

# print(sum(qualitylevels))
print(qualitylevels[0] * qualitylevels[1] * qualitylevels[2])