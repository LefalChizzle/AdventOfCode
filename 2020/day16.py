from math import prod
with open('files/day16.txt') as file:
    readin = file.read().split("\n\n")
    valid = readin[0].split("\n")
    myticket = tuple(map(int, readin[1].split("\n")[-1].split(",")))
    nearby = [tuple(map(int, i.split(",")))
              for i in readin[2].split("\n")[1:]]


print(valid)
for i in range(len(valid)):
    valid[i] = valid[i][valid[i].index(": ")+1:]
    valid[i] = (int(valid[i][:valid[i].index("-")]),
                int(valid[i][valid[i].index("-")+1:valid[i].index(" o")]),
                int(valid[i][valid[i].index("r ")+2:].split("-")[0]),
                int(valid[i][valid[i].index("r ")+2:].split("-")[1]))


def is_valid(tick) -> bool:
    for i in valid:
        yes = tick >= i[0] and tick <= i[1] or tick >= i[2] and tick <= i[3]

        if yes:
            return True
    return False


def singleis_valid(word, tick) -> bool:
    i = valid[word]
    yes = tick >= i[0] and tick <= i[1] or tick >= i[2] and tick <= i[3]

    if yes:
        return True
    return False


print(nearby)
scan_error = []
torem = []
for i in range(len(nearby)):
    for j in nearby[i]:
        if not is_valid(j):
            scan_error.append(j)
            torem.append(i)

validnearby = [nearby[i] for i in range(len(nearby)) if i not in torem]

print(sum(scan_error))

print(validnearby)

wordorder = {}
for i in range(len(valid)):
    temp = []
    for columncouldbe in range(len(valid)):
        if all([singleis_valid(columncouldbe, ticket[i])for ticket in validnearby]):
            temp.append(columncouldbe)
    wordorder[i] = temp

print(wordorder)
# print(len(valid))


def ffs(dictionary):
    for i in dictionary:
        if len(dictionary.get(i)) > 1:
            return True
    return False


# print(j)
while ffs(wordorder):
    for i in wordorder:
        # print("iloop", wordorder)
        if len(wordorder[i]) == 1:
            # print("yay", wordorder)
            for j in wordorder:
                temp = wordorder[j]
                # print(type(temp))
                # print(temp, wordorder[j], wordorder[i])
                if i != j:
                    # print("almost", wordorder)
                    try:
                        temp.remove(wordorder.get(i)[0])
                    except ValueError:
                        pass
                    wordorder[j] = temp
                    # print("here", wordorder)

# print(valid)
# print(myticket)
# print(nearby)
print(wordorder)

print(myticket)
print([myticket[wordorder[i][0]] for i in range(6)])
