from copy import copy
with open("files/day6.txt") as file:
    groups = [i for i in file.read().split("\n\n")]

# print(groups)
ansPart1 = [i.replace("\n", "") for i in groups]
ansPart2 = [0]*len(groups)
for i in range(len(groups)):
    for j in "abcdefghijklmnopqrtsuvwxyz":
        if ansPart1[i].count(j) > 1:  # part1
            ansPart1[i] = ansPart1[i].replace(j, "")
            ansPart1[i] += j

        if groups[i].count(j) == (groups[i].count("\n") + 1):  # part2
            ansPart2[i] += 1


# print("1:", ansPart1)
# print("2:", ansPart2)
yesCount = [len(i) for i in ansPart1]
print(sum(yesCount))
print(sum(ansPart2))
# print(ansPart2[7], len(groups[7]))
