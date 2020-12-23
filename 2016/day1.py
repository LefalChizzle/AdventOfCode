# with open("files/day1.txt") as file:
#     instructions = [(i[0], int(i[1:])) for i in file.read().split(", ")]


# print(instructions)

# x = 0
# for i in instructions:
#     if i[0] == "R":
#         x += i[1]
#     elif i[0] == "L":
#         x -= i[1]

# print(x)

DIRECTIONS = 'NWSE'


def read_data(fname):
    data = []
    for step in open("files/day1.txt").readline().split(','):
        step = step.strip()
        data.append((step[0], int(step[1:])))
    return data


def turn(direction_idx, direction):
    if direction == 'R':
        direction_idx += 1
    else:
        direction_idx -= 1
    return direction_idx % len(DIRECTIONS)


def distance(xy):
    x, y = xy
    return abs(x) + abs(y)


def get_coordinates():
    direction_idx = 0
    x = 0
    y = 0
    data = read_data("files/day1.txt")

    for rotate_direction, length in data:
        direction_idx = turn(direction_idx, rotate_direction)
        if DIRECTIONS[direction_idx] == 'N':
            y -= length
        elif DIRECTIONS[direction_idx] == 'S':
            y += length
        elif DIRECTIONS[direction_idx] == 'W':
            x += length
        elif DIRECTIONS[direction_idx] == 'E':
            x -= length
    return x, y


def get_second_coordinates():
    locations = set()

    x = 0
    y = 0
    direction_idx = 0
    data = read_data("files/day1.txt")

    for rotate_direction, length in data:
        direction_idx = turn(direction_idx, rotate_direction)
        if DIRECTIONS[direction_idx] == 'N':
            for i in range(length):
                if (x, y - i) in locations:
                    return x, y - i
                locations.add((x, y - i))
            y -= length
        elif DIRECTIONS[direction_idx] == 'S':
            for i in range(length):
                if (x, y + i) in locations:
                    return x, y + i
                locations.add((x, y + i))
            y += length
        elif DIRECTIONS[direction_idx] == 'W':
            for i in range(length):
                if (x + i, y) in locations:
                    return x + i, y
                locations.add((x + i, y))
            x += length
        elif DIRECTIONS[direction_idx] == 'E':
            for i in range(length):
                if (x - i, y) in locations:
                    return x - i, y
                locations.add((x - i, y))
            x -= length


print(distance(get_coordinates()))
print(distance(get_second_coordinates()))
