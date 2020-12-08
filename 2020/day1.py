with open("files/day1.txt") as file:
    expenses = [int(i.strip()) for i in file.readlines()]

# part1
for i in expenses:
    for j in expenses:
        if i + j == 2020:
            part1 = i * j

print("part1:", part1)

# part2
for i in expenses:
    for j in expenses:
        for k in expenses:
            if i + j + k == 2020:
                part2 = i * j * k

print("part2:", part2)
