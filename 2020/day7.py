with open('files/day7.txt') as file:
    rules = {}

    for i in file.readlines():
        bagName = i.split("contain")[0].replace("bags", "").replace(" ", "")
        insideBag = ''.join(i.strip().split("contain")[1]
                             .replace("bags", "").replace("bag", "")
                             .replace(".", "").replace(" ", "")).split(",")
        howMany = []

        for i in range(len(insideBag)):
            if insideBag[i] == "noother":
                howMany.append(0)
                continue
            howMany.append(int(insideBag[i][0]))
            insideBag[i] = insideBag[i][1:]

        line = {bagName: [insideBag, howMany]}

        rules.update(line)

# for i in rules:
#     print(i, rules.get(i))


# part1
def helpMe(whatImLookingFor):
    for i in rules:
        if whatImLookingFor in rules.get(i)[0]:
            if i not in hasShinyGold:
                hasShinyGold.append(i)
            helpMe(i)


# part2
def damnIwantedToUseRegex(start):
    rgs = rules.get(start)
    contains = sum(rgs[1])
    for i in range(len(rgs[0])):
        if rgs[0][i] == "noother":
            return 0
        contains += rgs[1][i] * damnIwantedToUseRegex(rgs[0][i])
    return contains


hasShinyGold = []
helpMe("shinygold")
# print(hasShinyGold)
print(len(hasShinyGold))
print(damnIwantedToUseRegex("shinygold"))


# some more for fun
temp = []
temp2 = []
for i in rules:
    temp.append(i)
    temp2.append(damnIwantedToUseRegex(i))
from numpy import argmax, argmin
print(f"there are {max(temp2)} bags in {temp[argmax(temp2)]}")
print(f"there are {min(temp2)} bags in {temp[argmin(temp2)]}")
