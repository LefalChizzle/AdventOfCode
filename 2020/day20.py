# print(puzzle)

import functools
import itertools
import operator
# noideahowtousethese,ijustgoogledthem
import networkx
import numpy as np

tiles = {}

with open('files/day20.txt') as file:
    # puzzle = [i for i in file.read().strip().split("\n\n")]

    for tiledata in file.read().strip().split("\n\n"):
        a, *tilelines = tiledata.splitlines()
        num = int(a.strip(":").split()[1])
        tiles[num] = np.array([[c == "#" for c in r]
                               for r in tilelines], dtype=np.uint8)


def nptobin(s):
    return int("".join([str(k) for k in s]), 2)

# up and down - convert borders of .# to 01 to make comparing them easier


def get_borders(n):
    return [nptobin(n[0]), nptobin(n[:, -1]), nptobin(n[-1]), nptobin(n[:, 0])]


# numpy is hard so i put them all in one thing
# yield is cool
def get_flips(tile):
    """
    generates each orientation
    """
    res = tile
    for i in range(2):
        for j in range(4):
            yield res
            res = np.rot90(res)
        res = np.flip(tile, 1)


borders = {}

for n, tile in tiles.items():
    borders[n] = set.union(*[set(get_borders(fl)) for fl in get_flips(tile)])

grph = networkx.Graph()

for i, j in itertools.combinations(borders, 2):
    if len(borders[i] & borders[j]) == 2:
        grph.add_edge(i, j)

corners = [n for n in grph if len(grph[n]) == 2]

print("part1:", functools.reduce(operator.mul, corners))


def ext(pt):
    used = set(tile for tile, _ in grd.values())
    tile, img = grd[pt]
    border = get_borders(img)
    for nb in grph[tile]:
        if nb not in used:
            for fl in get_flips(tiles[nb]):
                if get_borders(fl)[0] == border[2]:
                    grd[(pt[0] + 1, pt[1])] = (nb, fl)
                if get_borders(fl)[3] == border[1]:
                    grd[(pt[0], pt[1] + 1)] = (nb, fl)


for fl in get_flips(tiles[corners[0]]):
    grd = {}
    grd[(0, 0)] = (corners[0], fl)
    ext((0, 0))
    if len(grd) == 3:
        break

for i in range(12):
    for j in range(12):
        ext((i, j))

image = np.concatenate([np.concatenate([grd[i, j][1][1:-1, 1:-1]
                                        for j in range(12)], axis=1
                                       )for i in range(12)], axis=0)

monster_str = (
    "                  # \n"
    "#    ##    ##    ###\n"
    " #  #  #  #  #  #   ".splitlines()
)

monster = np.array([[c == "#" for c in r]
                    for r in monster_str], dtype=np.uint8)

for image in get_flips(image):
    count = 0
    for i in range(image.shape[0] - monster.shape[0] + 1):
        for j in range(image.shape[1] - monster.shape[1] + 1):
            check = image[i: i + monster.shape[0], j: j + monster.shape[1]]
            if (check & monster == monster).all():
                count += 1
    if count:
        break

print("part2:", int(np.sum(image) - count * np.sum(monster)))
