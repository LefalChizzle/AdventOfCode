from math import prod
from copy import deepcopy

with open("files/day3.txt") as file:
    original = [list(i.strip()) for i in file.readlines()]

countlist = []
slopelist = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for slope in slopelist:
    count = 0
    trees = deepcopy(original)
    for i in range(len(trees)):
        if i*slope[1] > len(trees):
            break

        trees[i*slope[1] % len(trees)][i*slope[0] % len(trees[i])] = "X" \
            if trees[i*slope[1] % len(trees)][i*slope[0] %
                                              len(trees[i])] == "#" else "O"

        count += 1 if trees[i*slope[1] %
                            len(trees)][i*slope[0] %
                                        len(trees[i])] == "X" else 0

        # print("".join(trees[i]), count, i, i*3, slope)

    countlist.append(count)
# print(trees)

print("part1:", countlist[1])
print("part2:", " * ".join(map(str, countlist)), "=", prod(countlist))
