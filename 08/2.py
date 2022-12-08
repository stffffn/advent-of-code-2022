trees = []
with open("input.txt") as f:
    trees = f.read().split("\n")


def getScenicScore(curTree, trees):
    scenicScore = 0
    for tree in trees:
        scenicScore += 1
        if tree >= curTree:
            break
    return scenicScore


scenicScores = []
for index, row in enumerate(trees[1 : len(trees) - 1 : 1]):
    treesBefore = trees[: index + 1]
    treesAfter = trees[index + 2 :]
    for i in range(1, len(row) - 1):
        above = [int(x[i]) for x in treesBefore]
        below = [int(x[i]) for x in treesAfter]
        curTree = int(row[i])
        left = [int(x) for x in row[:i]]
        right = [int(x) for x in row[i + 1 :]]

        scenicScores.append(
            getScenicScore(curTree, reversed(above))
            * getScenicScore(curTree, reversed(left))
            * getScenicScore(curTree, below)
            * getScenicScore(curTree, right)
        )

print(max(scenicScores))
