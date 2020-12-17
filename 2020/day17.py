from time import time
from collections import Counter

# print(zed0)


def griddyboi(d):

    coords = [()]
    for x in range(d):
        coords = [x + (i,) for i in [-1, 0, 1] for x in coords]
    # print(coords)
    coords.remove((tuple([0 for i in range(d)])))
    # print(" ")
    # print(coords)

    with open('files/day17.txt') as file:
        zed0 = file.read().splitlines()
        state = set((d - 2) * (0,) + (i, j) for i, v in enumerate(zed0)
                    for j, v in enumerate(v) if v == '#')

    # print("")
    # print(state)

    for i in range(6):
        state = set(pos for pos, cnt in Counter(
            tuple(map(sum, zip(pos, n)))
            for pos in state for n in coords).items()
            if cnt == 3 or pos in state and cnt == 2)

    return(len(state))


for i in range(3, 5):
    x = time()
    y = griddyboi(i)
    z = time()
    print(f"part{i-2}: {y}, in {z-x}")


# for i in range(11):
#     x = time()
#     y = griddyboi(i)
#     z = time()
#     print(f"{i} dimensions: {y}, in {z-x}")

# start = time()
# griddyboi(7)
# p1 = time()
# print(p1-start)

# one = time()
# griddyboi(3)
# two = time()
# print(two-one)
# griddyboi(4)
# three = time()
# print(three - two)
