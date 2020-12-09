from copy import copy
with open('files/day9.txt') as file:
    codes = [int(i.strip()) for i in file.readlines()]

print(codes)
master = copy(codes)

preamble = []
invalid = 0
for i in range(25):
    preamble.append(codes.pop(0))
while invalid == 0:

    # print(preamble)
    # print(codes)

    twoSums = []
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            if i != j:
                if (pair := preamble[i]+preamble[j]) not in twoSums:
                    twoSums.append(pair)

    # print(twoSums)

    if codes[0] not in twoSums:
        invalid = codes[0]
        print(invalid, "is not valid!")

    if len(codes) > 1:
        preamble.pop(0)
        preamble.append(codes.pop(0))

    # print(preamble)
    # print(codes)

for i in range(len(master)):
    total = 0
    for j in range(len(master)):
        total = sum(master[i:j])
        if total == invalid:
            minimum = sorted(master[i:j])[0]
            maximum = sorted(master[i:j])[-1]
            print(i, j, minimum, maximum, minimum + maximum)
