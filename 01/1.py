blocks = []
with open("input.txt") as f:
    blocks = f.read().split("\n\n")

allCalories = []
for block in blocks:
    values = block.split()
    sum = 0
    for value in values:
        sum += int(value)
    allCalories.append(sum)

maxValue = 0
for calories in allCalories:
    if calories > maxValue:
        maxValue = calories

print(maxValue)
