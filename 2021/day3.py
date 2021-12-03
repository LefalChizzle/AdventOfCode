with open("files/day3.txt") as file:
    inp = file.read()

# inp = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""


x = inp.split("\n")

arr = [0]*len(x[0])

for i in x:
    for j in range(len(i)):
        arr[j] += int(i[j])

# print(arr)
gamma = ['1' if i > len(x)/2 else '0' for i in arr]
epsilon = ['0' if i > len(x)/2 else '1' for i in arr]
decgam = int("".join(gamma),base=2)
deceps = int("".join(epsilon),base=2)

# print(decgam, deceps)
print(decgam*deceps)



y = [i for i in x]
bits = len(y[0])
for i in range(len(y[0])):
    count = sum([int(n[i]) for n in y])

    if count-(len(y)-count) >= 0:
        y = [n for n in y if n[i] == '1']
    else:
        y = [n for n in y if n[i] == '0']
    if len(y)==1:break
oxygen = int("".join(y[0]),base=2)





for i in range(len(x[0])):
    count = sum([int(n[i]) for n in x])

    if count-(len(x)-count) >= 0:
        x = [n for n in x if n[i] == '0']
    else:
        x = [n for n in x if n[i] == '1']

    if len(x)==1:break

carbon = int("".join(x[0]),base=2)

print(carbon * oxygen)
