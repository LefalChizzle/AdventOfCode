import time
from math import prod

with open('files/day13.txt') as file:
    timestamp = int(file.readline().strip())
    busIDswithX = file.readline().strip().split(',')

busIDs = [i for i in busIDswithX if i != 'x']
# print(busIDswithX)
# print(timestamp)
# print(busIDs)

count = 0
flag = True
while flag:
    for i in busIDs:
        if (timestamp + count) % int(i) == 0:
            flag = False
            bus = int(i)
            waittime = timestamp + count

    count += 1

print(f"part1: {(waittime - timestamp) * bus}")
# flag = True
# while flag:
#     for i in range(len(busIDswithX)):
#         if busIDswithX[i] == 'x':
#             continue
#         elif (i+timestamp % int(busIDswithX[i])) == 0:
#             flag = True
#         else:
#             flag = False
#     print(timestamp)
#     timestamp += 1
# print(timestamp)

# part2
# ? startTime = time.time()
deltaTimes = [[i, int(j)] for i, j in enumerate(busIDswithX) if j != "x"]
offset = deltaTimes[0][0] + deltaTimes[0][1]
completed = 1
increment = prod([i[1] for i in deltaTimes[:completed]])

while completed < len(deltaTimes):
    temp = [((offset + i) % j == 0) for i, j in deltaTimes[:completed+1]]

    if False not in temp:
        completed += 1
        increment = prod([i[1] for i in deltaTimes[:completed]])
        if completed == len(deltaTimes):
            print(f"part2: {offset}")
            # ? endTime = time.time()

    offset += increment

# ?print(f"start: {startTime}\nend: {endTime}\ntimetaken: {endTime-startTime}")
