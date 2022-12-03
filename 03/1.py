lines = []
with open("input.txt") as f:
    lines = f.read().split("\n")

lowercaseItems = dict(zip(map(chr, range(ord("a"), ord("z") + 1)), range(1, 27)))
uppercaseItems = dict(zip(map(chr, range(ord("A"), ord("Z") + 1)), range(27, 53)))

prioritySum = 0
for line in lines:
    lineHalf = len(line) // 2
    firstHalf = line[:lineHalf]
    secondHalf = line[lineHalf:]
    intersection = set(firstHalf).intersection(secondHalf)

    for char in intersection:
        if char in lowercaseItems:
            prioritySum += lowercaseItems[char]
        else:
            prioritySum += uppercaseItems[char]

print(prioritySum)
