with open('files/day12.txt') as file:
    directions = [i.strip() for i in file.readlines()]

# print(directions)
vert = 0
hori = 0
dir = "east"


def rotatep1(lorr, rot):
    global dir
    if rot == 270:
        if lorr == "L":
            lorr = "R"
        else:
            lorr = "L"
        rot = 90

    if rot == 90:
        if dir == "east":
            dir = "north" if lorr == "L" else "south"
        elif dir == "west":
            dir = "south" if lorr == "L" else "north"
        elif dir == "north":
            dir = "west" if lorr == "L" else "east"
        elif dir == "south":
            dir = "east" if lorr == "L" else "west"
    elif rot == 180:
        if dir == "east":
            dir = "west"
        elif dir == "west":
            dir = "east"
        elif dir == "north":
            dir = "south"
        elif dir == "south":
            dir = "north"


for i in directions:
    if i[0] == "N":
        vert += int(i[1:])
    elif i[0] == "S":
        vert -= int(i[1:])
    elif i[0] == "E":
        hori += int(i[1:])
    elif i[0] == "W":
        hori -= int(i[1:])
    elif i[0] == "L":
        rotatep1("L", int(i[1:]))
    elif i[0] == "R":
        rotatep1("R", int(i[1:]))
    elif i[0] == "F":
        if dir == "east":
            hori += int(i[1:])
        elif dir == "west":
            hori -= int(i[1:])
        elif dir == "north":
            vert += int(i[1:])
        elif dir == "south":
            vert -= int(i[1:])

print(vert, hori, dir)


wayVert = 1
wayHori = 10
shipVert = 0
shipHori = 0


def rotatep2(lorr, rot):
    global wayHori
    global wayVert

    if lorr == "R":
        lorr = "L"
        rot = 360 - rot

    if rot == 90:
        temp = -wayVert
        wayVert = wayHori
        wayHori = temp
    elif rot == 180:
        wayVert = -wayVert
        wayHori = -wayHori
    elif rot == 270:
        temp = -wayHori
        wayHori = wayVert
        wayVert = temp


for i in directions:
    if i[0] == "N":
        wayVert += int(i[1:])
    elif i[0] == "S":
        wayVert -= int(i[1:])
    elif i[0] == "E":
        wayHori += int(i[1:])
    elif i[0] == "W":
        wayHori -= int(i[1:])
    elif i[0] == "L":
        rotatep2("L", int(i[1:]))
    elif i[0] == "R":
        rotatep2("R", int(i[1:]))
    elif i[0] == "F":
        shipVert += int(i[1:]) * wayVert
        shipHori += int(i[1:]) * wayHori
    print(wayHori, wayVert, shipHori, shipVert, shipHori + shipVert)
