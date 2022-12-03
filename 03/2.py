lines = []
with open("input.txt") as f:
    lines = f.read().split("\n")

lowercaseItems = dict(zip(map(chr, range(ord("a"), ord("z") + 1)), range(1, 27)))
uppercaseItems = dict(zip(map(chr, range(ord("A"), ord("Z") + 1)), range(27, 53)))

groups = []
for x, y, z in zip(lines[0::3], lines[1::3], lines[2::3]):
    groups.append([x, y, z])

prioritySum = 0
for group in groups:
    intersection = set(group[0]).intersection(group[1], group[2])

    for char in intersection:
        if char in lowercaseItems:
            prioritySum += lowercaseItems[char]
        else:
            prioritySum += uppercaseItems[char]

print(prioritySum)
