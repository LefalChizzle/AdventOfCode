with open("files/day1.txt") as file:
    expenses = [int(i.strip()) for i in file.readlines()]

print(expenses)

# part1
for i in expenses:
    for j in expenses:
        if i + j == 2020:
            print(i, j,  i * j)

# part2
for i in expenses:
    for j in expenses:
        for k in expenses:
            if i + j + k == 2020:
                print(i, j, k,  i * j * k)
