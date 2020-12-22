def passToBinary(boardingPass):
    boardingPass = boardingPass.strip()
    boardingPass = boardingPass.replace("L", "0")
    boardingPass = boardingPass.replace("F", "0")
    boardingPass = boardingPass.replace("R", "1")
    boardingPass = boardingPass.replace("B", "1")
    return boardingPass


with open("files/day5.txt") as file:
    passes = [passToBinary(i)for i in file.readlines()]


maxseatId = []
for i in passes:
    row = int(i[0:7], base=2)
    column = int(i[7:11], base=2)
    seatId = row*8 + column
    maxseatId.append(seatId)
    # print(row, column, seatId)

part1 = max(maxseatId)
part2 = [i for i in range(min(maxseatId), max(maxseatId))
         if i not in maxseatId][0]

print("part 1: ", part1)
print("part 2: ", part2)

# maxseatId = 0
# for i in passes:
#     row = int(i[0:7],base=2)
#     column = int(i[7:11],base=2)
#     seatId = row*8 + column
#     if seatId > maxseatId:
#         maxseatId = seatId
#     print(row, column, seatId)
# print(maxseatId)

# TODO can process as a single birnary number, dont need to consider columns separately
