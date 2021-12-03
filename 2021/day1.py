with open("files/day1.txt") as file:
    inp = file.read()

# test
# inp = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263"""

help = [int(i) for i in inp.split()]



count = 0
for i in range(len(help)):
    if help[i-1]<help[i]: count += 1

count2 = 0
for i in range(len(help)-3):
    if help[i]+help[i+1]+help[i+2] < help[i+1]+help[i+2]+help[i+3]:
         count2 += 1



print(count)
print(count2)