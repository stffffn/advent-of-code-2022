import re
from collections import defaultdict

lines = []
with open("input.txt") as f:
    delimiter = "$ cd"
    lines = [line.replace("\n", "") for line in f.readlines()]

dirs = defaultdict(int)
pathOrder = []
for line in lines:
    if line.startswith("$ cd"):
        targetPath = line[5:]
        if targetPath == "..":
            pathOrder.pop()
        else:
            pathOrder.append(targetPath)
    else:
        fileSize = sum([int(size) for size in re.findall("[0-9]+", line)])
        for i in range(1, len(pathOrder) + 1):
            dirs["".join(pathOrder[:i])] += fileSize

totalDiskSpace = 70000000
spaceNeeded = 30000000
maxFilledSpace = totalDiskSpace - spaceNeeded
currentlyUsedSpace = dirs["/"]
toBeDeleted = currentlyUsedSpace - maxFilledSpace

smallestSizes = []
for dir in dirs:
    if dirs[dir] >= toBeDeleted:
        smallestSizes.append(dirs[dir])

print(min(smallestSizes))
