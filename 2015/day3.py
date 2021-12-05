with open("files/day3.txt") as file:
    inp = file.read()
    
# inp = '^v'
# inp = '^>v<'
# inp = '^v^v^v^v^v'

visitedp1 = set()

santap1 = (0,0)

visitedp1.add(santap1)

travel = lambda x, y: (x[0]+y[0],x[1]+y[1])


for i in inp:
    if i == '>':
        santap1 = travel(santap1,(1,0))
        visitedp1.add(santap1)
    elif i == '<':
        santap1 = travel(santap1,(-1,0))
        visitedp1.add(santap1)
    elif i == '^':
        santap1 = travel(santap1,(0,1))
        visitedp1.add(santap1)
    elif i == 'v':
        santap1 = travel(santap1,(0,-1))
        visitedp1.add(santap1)

# print(visitedp1)
print(len(visitedp1))


visitedp2 = set()

santap2 = (0,0)
robosanta = (0,0)

visitedp2.add(santap2)
roboflag = False
for i in inp:
    # print(visitedp2,santap2,robosanta)
    if roboflag:
        if i == '>':
            robosanta = travel(robosanta,(1,0))
            visitedp2.add(robosanta)
        elif i == '<':
            robosanta = travel(robosanta,(-1,0))
            visitedp2.add(robosanta)
        elif i == '^':
            robosanta = travel(robosanta,(0,1))
            visitedp2.add(robosanta)
        elif i == 'v':
            robosanta = travel(robosanta,(0,-1))
            visitedp2.add(robosanta)
    else:
        if i == '>':
            santap2 = travel(santap2,(1,0))
            visitedp2.add(santap2)
        elif i == '<':
            santap2 = travel(santap2,(-1,0))
            visitedp2.add(santap2)
        elif i == '^':
            santap2 = travel(santap2,(0,1))
            visitedp2.add(santap2)
        elif i == 'v':
            santap2 = travel(santap2,(0,-1))
            visitedp2.add(santap2)

    roboflag = not roboflag

# print(visitedp2)
print(len(visitedp2))