lines = []
with open("input.txt") as f:
    lines = f.read().split("\n")

values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

totalScore = 0
for line in lines:
    opponentPick = line[0]
    instruction = line[2]
    opponentValue = values[opponentPick]

    if instruction == "X":
        totalScore += 0
        if opponentValue - 1 == 0:
            totalScore += 3
        else:
            totalScore += opponentValue - 1
    elif instruction == "Y":
        totalScore += 3 + opponentValue
    else:
        totalScore += 6
        if opponentValue + 1 == 4:
            totalScore += 1
        else:
            totalScore += opponentValue + 1

print(totalScore)
