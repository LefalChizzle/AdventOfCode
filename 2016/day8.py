import os


def display() -> None:
    for i in screen:
        print(" ".join(i))


def decode(line: str) -> (str, int, int):
    line = line.split(" ")
    if line[0][1] == 'e':  # rect
        return (RECT, int(line[1][:line[1].index("x")]),
                int(line[1][line[1].index("x")+1:]))
    elif line[1][0] == 'c':  # rotate column
        return (RCOL, int(line[2][2:]), int(line[4]))
    elif line[1][0] == 'r':  # rotate row
        return (RROW, int(line[2][2:]), int(line[4]))


def RECT(A: int, B: int) -> None:
    for y in range(B):
        for x in range(A):
            screen[y][x] = '#'


def RCOL(A: int, B: int) -> None:
    prev = [i[A] for i in screen]
    # print(prev)
    post = prev[-B:] + prev[:-B]
    # print(post)
    for i in range(len(post)):
        # print(screen[i][A], post[i])
        screen[i][A] = post[i]


def RROW(A: int, B: int) -> None:
    prev = screen[A]
    post = prev[-B:]+prev[:-B]
    screen[A] = post


with open('files/day8.txt') as file:
    instructions = [decode(i.strip()) for i in file.readlines()]


# X = 7  # test
# Y = 3  # test
X = 50  # actual
Y = 6  # actual
screen = [['.']*X for i in range(Y)]

for command, A, B in instructions:
    os.system('cls')
    command(A, B)
    display()

p1 = sum([i.count("#") for i in screen])
print(f"part1: {p1}")
