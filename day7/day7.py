class Folder:
    def __init__(self, name, previous):
        self.name = name
        self.previous = previous
        self.children = {}   #{name: object}
        self.files = []      # [(size, name)]

    def addchild(self, name):
        if name not in self.children:
            child = Folder(name, self)
            self.children[name] = child
            pass
    
    def addfile(self, name, size):
        if name not in self.files:
            self.files.append((int(size), name))

    def getsize(self):
        self.size = 0
        for f in self.files:
            self.size += f[0]
        for c in self.children:
            self.size += self.children[c].getsize()
        return self.size
    
    def findlargeenoughdir(self):
        for c in self.children:
            self.children[c].findlargeenoughdir()
        if self.getsize() > spacetoclear:
            largeenoughdirectories.append(self)

with open("day7/input.txt") as f:
    lines = f.read().splitlines()

rootfolder = Folder("/", None)
currentfolder = rootfolder

for line in lines:
    if line == "$ cd /":
        continue
    if line[0] == "$":
        if line[2:4] == "cd":
            nextfolder = line[5:]
            if nextfolder == "..":
                currentfolder = currentfolder.previous
            else:
                currentfolder = currentfolder.children[nextfolder]

        elif line[2:3] == "ls":
            pass
    
    else:
        linewords = line.split()
        if linewords[0].isnumeric() == True:
            currentfolder.addfile(linewords[1], linewords[0])
        elif linewords[0] == "dir":
            currentfolder.addchild(linewords[1])

pass

# smalldirectories = []
# rootfolder.checksmalldir()
# smalldirectorysizes = [d.size for d in smalldirectories]
# print(sum(smalldirectorysizes))
pass
maxspace = 40_000_000
usedspace = rootfolder.getsize()
spacetoclear = usedspace - maxspace

largeenoughdirectories = []

rootfolder.findlargeenoughdir()
directorysizes = [d.size for d in largeenoughdirectories]
print(min(directorysizes))