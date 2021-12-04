with open("files/day2.txt") as file:
    inp = file.read()

# inp = """1x10x1
# 2x3x4"""

inp = inp.split("\n")
print(inp)

t = 0
r = 0
for i in inp:
    w = sorted([int(j) for j in i.split('x')])
    x = [w[0]*w[1], w[1]*w[2], w[0]*w[2]]
    y = sum(x) 
    z = 2*y + x[0]
    a = 2*w[0]+ 2*w[1]+ w[0]*w[1]*w[2]
    t = t + z
    r = r + a
print(t)
print(r)