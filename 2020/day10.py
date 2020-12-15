with open('files/day10.txt') as file:
    AdapterJolts = sorted([int(i.strip()) for i in file.readlines()])


# print(AdapterJolts)
phoneJoltage = max(AdapterJolts) + 3
# print(f"Device is rated for {phoneJoltage} jolts")

# *part1
prevJolt = 0
joltDiff = [0, 0, 0, 1]
for i in AdapterJolts:
    # print(i, prevJolt)
    joltDiff[i - prevJolt] += 1
    prevJolt = i

# print(joltDiff[1:])
print(f"part1: {joltDiff[1] * joltDiff[3]}")


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
joltTotal = [1, 1, 1]
for i in range(3, len(AdapterJolts)):
    nextJoltage = joltTotal[i - 1]
    # print(f"nextJoltage {nextJoltage}")

    for j in [2, 3]:

        if buffer[i] - buffer[i - j] <= 3:
            nextJoltage += joltTotal[i - j]
            # print(nextJoltage)

    joltTotal.append(nextJoltage)
    # print(f"arr {joltTotal}")

# print(joltTotal)
print(f"part2: {joltTotal[-1]}")

print(max(AdapterJolts))
# input()
# print(len(AdapterJolts))
