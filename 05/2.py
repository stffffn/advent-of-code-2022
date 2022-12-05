import re

crates = []
instructions = []
with open("input.txt") as f:
    lines = f.read().split("\n\n")
    crates = lines[0].split("\n")
    instructions = lines[1].split("\n")

columnMargin = 1
columnWidth = 3 + columnMargin
numberOfStacks = (len(crates[0]) + columnMargin) // columnWidth

stacks = [[] for _ in range(numberOfStacks)]
for i, row in enumerate(crates):
    if i == len(crates) - 1:
        break
    for j in range(0, len(row), columnWidth):
        stackIndex = j // columnWidth
        x = row[j : j + columnWidth]
        if x.isspace() == False:
            stacks[stackIndex].append(*re.findall("[A-Za-z]", x))

for instruction in instructions:
    amount, origin, target = [int(i) for i in re.findall("[0-9]+", instruction)]
    cratesToMove = stacks[origin - 1][:amount]
    del stacks[origin - 1][:amount]
    stacks[target - 1] = [*cratesToMove, *stacks[target - 1]]

solution = "".join([stack[0] for stack in stacks])
print(solution)
