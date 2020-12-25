with open("files/day24.txt") as file:
    inp = [i.strip() for i in file.readlines()]


dirs = []
for x in range(len(inp)):
    temp = []
    for i in range(len(inp[x])):
        if inp[x][i-1] == "n" or inp[x][i-1] == "s":
            temp.append(inp[x][i-1]+inp[x][i])
        elif inp[x][i] != "s" and inp[x][i] != "n":
            temp.append(inp[x][i])
    # print(temp)
    dirs.append(temp)

flipped = set()
for instrs in dirs:
    coords = 0+0j
    for i in instrs:
        if i == 'e':
            coords += 1+0j
        elif i == 'se':
            coords += 1-1j
        elif i == 'sw':
            coords += 0-1j
        elif i == 'w':
            coords += -1+0j
        elif i == 'nw':
            coords += -1+1j
        elif i == 'ne':
            coords += 0+1j
    # print(coords)
    if coords not in flipped:
        flipped.add(coords)
    else:
        flipped.remove(coords)
print(f"part1: {len(flipped)}")


# part 2
axes = ['e', 'se', 'sw', 'w', 'nw', 'ne']


def get_all_neighbours(cell: complex) -> set:
    neighbours = set([cell + (1+0j),  # e
                      cell + (1-1j),  # se
                      cell + (0-1j),  # sw
                      cell + (-1+0j),  # w
                      cell + (-1+1j),  # nw
                      cell + (0+1j)])  # ne
    return neighbours


alive = flipped
for i in range(100):
    newalive = set()
    newdead = set()

    floor = set()
    for tile in alive:
        floor.add(tile)
        floor.update(get_all_neighbours(tile))

    for tile in floor:
        adj_alive = len(alive.intersection(get_all_neighbours(tile)))

        if tile not in alive and adj_alive == 2:
            newalive.add(tile)
        elif tile in alive and (adj_alive == 0 or adj_alive > 2):
            newdead.add(tile)

    alive.difference_update(newdead)
    alive.update(newalive)
    # print(len(alive))

print(f"part2: {len(alive)}")
