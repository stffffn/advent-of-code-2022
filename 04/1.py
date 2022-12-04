lines = []
with open("input.txt") as f:
    lines = [list(line.split(",")) for line in f.read().split("\n")]

sum = 0
for line in lines:
    firstElf = list(map(int, line[0].split("-")))
    secondElf = list(map(int, line[1].split("-")))

    if firstElf[0] >= secondElf[0] and firstElf[1] <= secondElf[1]:
        sum += 1
    elif firstElf[0] <= secondElf[0] and firstElf[1] >= secondElf[1]:
        sum += 1

print(sum)
