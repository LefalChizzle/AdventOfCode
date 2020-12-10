with open('files/day10.txt') as file:
    AdapterJolts = sorted([int(i.strip()) for i in file.readlines()])


# print(AdapterJolts)
phoneJoltage = max(AdapterJolts) + 3
# print(f"Device is rated for {phoneJoltage} jolts")

# *part1
prevJolt = 0
diffCount = [0, 0, 0, 1]
for i in AdapterJolts:
    # print(i, prevJolt)
    diffCount[i - prevJolt] += 1
    prevJolt = i

# print(diffCount[1:])
print(f"part1: {diffCount[1] * diffCount[3]}")


# !Garbage from unsuccessful attempts at part2
def joltify(myJolt):
    if myJolt[-1]+1 not in AdapterJolts:
        return
    else:
        pass
    return joltify(myJolt+[1]), joltify(myJolt+[2]), joltify(myJolt+[3])

# [0] <- [0,1],[0,2],[0,3]
# [0,1] <- [0,1,2], [0,1,3], [0,1,4]

# print(f"??? {joltify([0])}")


def powerset(seq) -> int:
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


def validJolt(chain):
    if len(chain) == 0:
        return False
    if chain[0] == 1 and chain[-1] == 19:
        prevJolt = 0
        for i in chain:
            if i - prevJolt > 3:
                return False
            prevJolt = i
        return True

# power = [1, 2, 3, 4]
# r = [x for x in powerset(AdapterJolts) if validJolt(x)]
# r = [x for x in powerset(AdapterJolts)]
# r.sort()
# print(r)
# for i in r:
    # print(i)

# print(len(r))


longestJolt = [0] + AdapterJolts + [phoneJoltage]
# print(longestJolt)

# *part2 but it actually works
buffer = [-6, -3, 0] + AdapterJolts
runningTotal = [1, 1, 1]
for i in range(3, len(AdapterJolts)):
    nextJoltage = runningTotal[i - 1]
    # print(f"nextJoltage {nextJoltage}")

    for j in [2, 3]:

        if buffer[i] - buffer[i - j] <= 3:
            nextJoltage += runningTotal[i - j]
            # print(nextJoltage)

    runningTotal.append(nextJoltage)
    # print(f"arr {runningTotal}")

# print(runningTotal)
print(f"part2: {runningTotal[-1]}")

# print(len(AdapterJolts))
