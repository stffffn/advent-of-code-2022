lines = []
with open("input.txt") as f:
    lines = [list(line.split(",")) for line in f.read().split("\n")]

sum = 0
for line in lines:
    firstElf = list(map(int, line[0].split("-")))
    secondElf = list(map(int, line[1].split("-")))
    firstElfRange = list(range(firstElf[0], firstElf[1] + 1))
    secondElfRange = list(range(secondElf[0], secondElf[1] + 1))

    if set(firstElfRange).intersection(secondElfRange):
        sum += 1

print(sum)
