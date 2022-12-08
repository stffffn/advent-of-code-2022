trees = []
with open("input.txt") as f:
    trees = f.read().split("\n")

treesAtStartAndEnd = len(trees[0]) * 2
treesAtTheEdge = (len(trees) - 2) * 2
treesTotal = treesAtStartAndEnd + treesAtTheEdge

for index, row in enumerate(trees[1 : len(trees) - 1 : 1]):
    treesBefore = trees[: index + 1]
    treesAfter = trees[index + 2 :]
    for i in range(1, len(row) - 1):
        above = [int(x[i]) for x in treesBefore]
        below = [int(x[i]) for x in treesAfter]
        curTree = int(row[i])
        left = [int(x) for x in row[:i]]
        right = [int(x) for x in row[i + 1 :]]

        if (
            all(topTree < curTree for topTree in above)
            or all(bottomTree < curTree for bottomTree in below)
            or all(leftTree < curTree for leftTree in left)
            or all(rightTree < curTree for rightTree in right)
        ):
            treesTotal += 1


print(treesTotal)
