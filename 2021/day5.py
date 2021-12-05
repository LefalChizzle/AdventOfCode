with open("files/day5.txt") as file:
    inp = file.read()

# inp = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2"""

from collections import Counter

inp = [[tuple(int(k) for k in j.split(",")) for j in i.split(" -> ")] for i in inp.split("\n")]

# print(inp)

vents = Counter()
diags = Counter()

def line(vector):
    vector.sort()
    tail = vector[0]
    head = vector[1]

    if tail[0] == head[0]:
        # print('Vert')
        # print([(tail[0],j) for j in range(tail[1],head[1]+1)])
        vents.update([(tail[0],j) for j in range(tail[1],head[1]+1)])
        diags.update([(tail[0],j) for j in range(tail[1],head[1]+1)])

    elif tail[1] == head[1]:
        # print('Hori')
        # print([(i,tail[1]) for i in range(tail[0],head[0]+1)])
        vents.update([(i,tail[1]) for i in range(tail[0],head[0]+1)])
        diags.update([(i,tail[1]) for i in range(tail[0],head[0]+1)])
    else:
        # print('Diag')
        # print([(i,j) for i,j in zip(range(tail[0],head[0]+1),range(tail[1],head[1]+1))])
        # print([(i,j) for i,j in zip(range(tail[0],head[0]+1),range(tail[1],head[1]-1,-1))])

        diags.update([(i,j) for i,j in zip(range(tail[0],head[0]+1),range(tail[1],head[1]+1))])
        diags.update([(i,j) for i,j in zip(range(tail[0],head[0]+1),range(tail[1],head[1]-1,-1))])


for row in inp:
    line(row)

t = 0
for i in vents.items():
    if i[1] > 1: t += 1
print(t)

d = 0
for i in diags.items():
    if i[1] > 1: d += 1
print(d)
