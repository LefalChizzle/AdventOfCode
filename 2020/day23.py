import time
# inp = 389125467  # test
inp = 476138259  # actual input

# part1
start_time = time.time()

table = list(str(inp))

pos = 0
current = int(table[pos])
destination = 0
posd = 0
hand = [0, 0, 0]
for i in range(100):
    # print(table)
    hand = [table[(pos + 1) % len(table)],
            table[(pos + 2) % len(table)],
            table[(pos + 3) % len(table)]]
    # print(hand)
    table.remove(hand[0])
    table.remove(hand[1])
    table.remove(hand[2])

    destination = int(current)
    while True:
        # print(destination, destination, hand)
        if destination == 1:
            destination = len(table)+3
        else:
            destination -= 1
        if str(destination) not in hand:
            break

    posd = table.index(str(destination)) + 1
    # print(table)
    # print(hand)
    # print(destination, posd)
    for j, x in enumerate(hand):
        table.insert(posd + j, x)
    # print(current, pos)
    # refreshing value in case it was changed
    pos = table.index(str(current))
    pos = pos + 1 if pos != len(table)-1 else 0
    current = table[pos]
# print(table)
one = table.index('1')
order = "".join(table[one+1:] + table[:one])
end_time = time.time()
print(f"part1: {order} in {end_time-start_time}")


# part 2
start_time = time.time()


table = list(map(int, str(inp)))
# print(table)

longtable = list(range(1, 1000000+2))
# longtable = {i: i+1 for i in range(1, 1_000_000+2)}
# print(longtable[-1])

# my_zip = [(table[i], (table[1:]+[len(table)+1])[i])
#           for i in range(len(table))]
# for i, j in my_zip:
for i, j in zip(table, table[1:] + [table[-1] + 1]):
    longtable[i] = j

longtable[1_000_000] = table[0]  # make circular
current = table[0]

for i in range(10_000_000):
    hand = []
    hand.append(longtable[current])
    hand.append(longtable[hand[0]])
    hand.append(longtable[hand[1]])

    destination = (current - 2) % 1_000_000 + 1
    # while True:
    #     # print(destination, destination, hand)
    #     if destination == 1:
    #         destination = len(table)+3
    #     else:
    #         destination -= 1
    #     if str(destination) not in hand:
    #         break
    while destination in hand:
        destination = (destination - 2) % 1_000_000 + 1

    # change current to point at the one that hand 3 current points at
    # change hand 3 to point at the one that destination currently points at
    # change destination to point at hand 1
    # change current to the cup following current
    longtable[current] = longtable[hand[2]]
    longtable[hand[2]] = longtable[destination]
    longtable[destination] = hand[0]
    current = longtable[current]

c1 = longtable[1]
c2 = longtable[c1]
ans2 = c1*c2
end_time = time.time()
print(f"part2: {c1} * {c2} = {ans2} in {end_time-start_time}")
