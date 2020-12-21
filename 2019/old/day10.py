'''lol = open('10question.txt','r')
x=''
for i in lol:
    x += i
    
grid = x.split('\n')



def lineOfSight(r,c):
    anglelist = []
    upanddown = [False,False,False,False]#up,down,left,right
    for y in range(0,len(grid)-1):
        for x in range(0,len(grid[0])):
            if x == c and y ==r :
                print('lolsame')
                continue
            elif x == c:
                if y < r:#upordown
                    upanddown[0] = True
                elif y > r:
                    upanddown[1] = True
                continue
            elif y == r:
                if x < c:#leftorright
                    upanddown[2] = True
                elif x > c:
                    upanddown[3] = True
                continue
                    
            if grid[x][y]=='#':
                angle = (y-r)/(x-c)
                

                if angle in anglelist:
                    print('skipped')
                    continue
                else:
                    print('notskipped')
                    
                    anglelist.append(angle)
                    
    value = len(anglelist) + upanddown.count(True)
    return value
    print('done')
print(grid)
leaderCoords = [0,0]
leaderScore = 0
for row in range(0,len(grid)-1):
    for column in range(0,len(grid[0])):#why is the length of a string
        current = grid[row][column]     #different to the length of a list
                                        #with the same number of values
                                        #ffs python
        if current == '.':
            print('dot')
            continue
        else:
            currentScore = lineOfSight(row,column)
            print(currentScore)
        if currentScore > leaderScore:
            leaderScore = currentScore
            leaderCoords[0] = column
            leaderCoords[1] = row
        print('column')
    print('row')
            
print(leaderCoords,leaderScore)
'''
from operator import itemgetter, attrgetter
from math import atan2, pi, hypot
# Position Object
class Pt(list):
    def __init__(s, x, y):
        s.value = y + x * 100
        s.x, s.y = x, y
    def __sub__(s, pt):
        return (pt.x - s.x, pt.y - s.y)
    def laser(s, n = 200):
        ys = {k: v for k,_,v in s}
        return ys[sorted(ys)[n-1]]
    def refresh(s):
        for pt in Pt.Field:
            if pt is not s:
                offset = s - pt; theta = atan2(*offset)
                yield (pi - theta, hypot(*offset), pt.value)
    def Identify(field):
        Pt.Field = (*field,)
        for pt in Pt.Field:
            pt += sorted(pt.refresh(), reverse = True)
            pt.targets = len({*map(itemgetter(0), pt)})
        return max(Pt.Field, key = attrgetter('targets'))
# Read Asteroid Grid
Station = Pt.Identify(Pt(x, y) for y, ln
    in enumerate(open('10question.txt'))
for x, o in enumerate(ln) if o == '#')
# Display Results
print("Silver:", Station.targets)
print("Gold:", Station.laser())
