with open("files/day3.txt") as file:
    inp = [tuple(map(int, i.strip().split())) for i in file.readlines()]
count = 0
for triangle in inp:
    count += 1 if (max(triangle) < sum(triangle)/2) else 0
print(count)
x = []
for i in range(0, len(inp), 3):
    x.append((inp[i][0], inp[i+1][0], inp[i+2][0]))
    x.append((inp[i][1], inp[i+1][1], inp[i+2][1]))
    x.append((inp[i][2], inp[i+1][2], inp[i+2][2]))
count = 0
for triangle in x:
    count += 1 if (max(triangle) < sum(triangle)/2) else 0
print(count)
