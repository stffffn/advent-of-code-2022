lines = []
with open("input.txt") as f:
    lines = f.read().split("\n")

values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

totalScore = 0
for line in lines:
    opponentPick = line[0]
    yourPick = line[2]
    totalScore += values[yourPick]
    comparator = values[opponentPick] - values[yourPick]

    if comparator == 0:
        totalScore += 3
    elif comparator == -1 or comparator == 2:
        totalScore += 6

print(totalScore)
