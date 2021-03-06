'''
def getImage(file):
    with open(file) as f:
        return f.readline()

def getLayers(image,dimx,dimy):
    chunks, chunk_size = len(image), dimx*dimy
    image = [ image[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    print(image)
    return image


n = 0
l = 10000
m = 0
for i in getLayers(getImage('day8.txt'),25,6):
    if int(i.count('0')) < l :
        l = i.count('0')
        n = m
    m+=1

print(str(l).count('1') * str(l).count('2'))
print(i)    
#print(l,n,i)
    
'''
def split(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def count(l, v):
    return sum(map(lambda x: 1 if x == v else 0, l))

def collapse(layers):
    return [next(filter(lambda v: v != 2, lay)) for lay in zip(*layers)]

def draw(img):
    for r in img: print(*['#' if x == 1 else ' ' for x in r])

lenx, leny = 25, 6
data = [int(x) for x in open('day8.txt').read().strip('\n')]

# Part 1
layers = split(data, lenx*leny)
best = min(layers, key=lambda l: count(l, 0))
print(count(best, 1) * count(best, 2))

# Part 2
img = split(collapse(layers), lenx)
draw(img)
