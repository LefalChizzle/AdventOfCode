with open("files/day2.txt") as file:
    passwords = [i.strip().split() for i in file.readlines()]
    for i in range(len(passwords)):
        passwords[i][1] = passwords[i][1][0:-1]
        passwords[i][0] = [int(i) for i in passwords[i][0].split("-")]

# part1
truecount = 0
for i in passwords:
    if (i[2].count(i[1]) >= int(i[0][0]) and i[2].count(i[1]) <= int(i[0][1])):
        truecount += 1
    print(i, truecount)

print(truecount)


# part2
truecount = 0
for i in passwords:
    if (i[2][i[0][0]-1] == i[1] or i[2][i[0][1]-1] == i[1]) and \
         not(i[2][i[0][0]-1] == i[1] and i[2][i[0][1]-1]) == i[1]:
        truecount += 1
    print(i, truecount)

print(truecount)
