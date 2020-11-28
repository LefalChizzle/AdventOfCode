def openSesame(file):
    with open(file) as f:
        return f.read().split('\n')
#print(openSesame('day22.txt'))

deck = [i for i in range(0,1007)]
#print(deck)
