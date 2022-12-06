datastream = ""
with open("input.txt") as f:
    datastream = f.readline()

for i in range(0, len(datastream) + 1, 1):
    if len(set(datastream[i : i + 4])) == 4:
        print(i + 4)
        break
