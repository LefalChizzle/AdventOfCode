with open("files/day2.txt") as file:
    inp = file.read()
    
# inp = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2"""

hor = 0
dep = 0
aim = 0
dep2 =0
for i in inp.split("\n"):
    x = i.split(" ")
    # print(i)
    # print(x)
    if x[0] == "forward":
        hor += int(x[1])
        dep2 += aim * int(x[1])
    elif x[0] == "down":
        dep += int(x[1])
        aim += int(x[1])
    elif x[0] == "up":
        dep -= int(x[1])
        aim -= int(x[1])

print(hor,dep,hor*dep, dep2, hor*dep2)