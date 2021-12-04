with open("files/day4.txt") as file:
    inp = file.read()

# inp = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""


numbers, *boards = inp.split("\n\n")
numbers = numbers.split(',')
boards = [[j.split() for j in i.split("\n")] for i in boards]

x = 5
y = 5

# print(numbers)
# print("---")
# print(boards)

def inBoard(board, number):
    # return number in board
    return number in [j for sub in board for j in sub]

def markBoard(board, number):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == number: board[row][col] = '/'

def checkWin(board):
    return 5 in [i.count('/') for i in board]+[i.count('/') for i in [[j[k] for j in board] for k in range(len(board))]]


winningscoresinorder = []
wonboards = []
for call in numbers:
    for b in range(len(boards)):
        if b in wonboards:continue
        # print(call)
        # print(board)
        if inBoard(boards[b],call):
            markBoard(boards[b], call)
        # print(checkWin(board))
        if checkWin(boards[b]):
            unmarked = sum([int(j) for i in boards[b] for j in i if j != '/'])
            # print(call, unmarked,unmarked*int(call))
            wonboards.append(b)
            winningscoresinorder.append(unmarked*int(call))

# print(wonboards)
print(winningscoresinorder)
print(winningscoresinorder[0])
print(winningscoresinorder[-1])
# board = [['/', '/', '/', '/', '/'], ['/', '/', '15', '/', '19'], ['18', '8', '/', '26', '20'], ['22', '/', '/', '6', '/'], ['/', '/', '12', '3', '/']]
# checkWin(board)


