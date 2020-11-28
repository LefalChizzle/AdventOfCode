'''def openSesame(puzzle):
    with open(puzzle) as f:
        return f.readlines()


init = 0
file = openSesame('day1.txt')
freq = []
flag = False
while not(flag):
    for x in file:
        freq.append(init)
        if x[0] == '-':
            print(x)
            init -= int(x[1:len(x)-1])
        elif x[0] == '+':
            print(x)
            #print(x[1:len(x)-1])
            init += int(x[1:len(x)-1])
        if init in freq:
            print('wahooo' +str(init))
            flag = True
            break
        print(init)
print(init)


'''
import itertools
data = [int(x) for x in open("day1.txt").readlines()]
print(sum(data))

freq = 0
seen = {0}
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)
