with open("files/day5.txt") as file:
    passes = [i.strip().replace("L", "0").replace("F", "0").replace("R", "1")
              .replace("B", "1")for i in file.readlines()]

maxseatId = []
for i in passes:
    row = int(i[0:7], base=2)
    column = int(i[7:11], base=2)
    seatId = row*8 + column
    maxseatId.append(seatId)
    # print(row, column, seatId)

print("Part 1: ", end=" ")
print(max(maxseatId))
print("Part 2: ", end=" ")
print([i for i in range(min(maxseatId), max(maxseatId))
      if i not in maxseatId][0])


# maxseatId = 0
# for i in passes:
#     row = int(i[0:7],base=2)
#     column = int(i[7:11],base=2)
#     seatId = row*8 + column
#     if seatId > maxseatId:
#         maxseatId = seatId
#     print(row, column, seatId)
# print(maxseatId)
