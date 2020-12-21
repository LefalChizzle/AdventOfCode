def openSesame(file):
    with open(file) as f:
        return(f.read().split())

def prettyPrint(grid):
    for i in grid:
        print(i)
        
def setKeyDoorLoc(ltr,grid):
    keyLoc1 = [(i,j.find(ltr.lower())) for i,j in enumerate(grid)]
    doorLoc1 = [(i,j.find(ltr.upper())) for i,j in enumerate(grid)]
    keyLoc = [(i,j) for i,j in keyLoc1 if j != -1][0]
    try:
        doorLoc = [(i,j) for i,j in doorLoc1 if j != -1][0]
    except:
        doorLoc = (-1,-1)
        
    return (keyLoc,doorLoc)


def getPlayerLoc(grid):
    player1 = [(i,j.find('@')) for i,j in enumerate(grid)]
    player = [(i,j) for i,j in player1 if j != -1][0]
    return(player)


def getNoKeys(grid):
    big = 'a'
    for i in grid:
        for j in i:
            if j in alphabet and j > big:
                big = j
    return big
    
def getKeyDoorLoc(keys,grid):
    x = {}
    for key in keys:
        x.update({key:setKeyDoorLoc(key,grid)})
    return x
        
'''        
def reachable_keys(cur_distmap, keys):
    return {
        (pos, d, keydoor)
        for pos, d, keydoor, blockers in cur_distmap
        if keydoor not in keys and (keydoor == keydoor.lower() or keydoor.lower() in keys) and not (blockers - keys)
    }  # not visited and is key or openable door and reachable
'''

###Theres only one shortest path between any two keys/doors
###this means its viable to calculate all distances before starting movement

    


alphabet = ''.join(sorted("qwertyuiopasdfghjklzxcvbnm"))

tunnels = openSesame('day18.txt')

keys = alphabet[:alphabet.find(getNoKeys(tunnels))+1]

keysAndDoors = getKeyDoorLoc(keys, tunnels)


prettyPrint(tunnels)
currentPos = getPlayerLoc(tunnels)



#print(keysAndDoors)


'''part 2 is 1540'''
def move(direction,playerloc):
    '''
    if direction = 'w':
        
        
    elif direction = 's':
    elif direction = 'a':
    elif direction = 'd':
    '''
    try:
        
        print("You are: \nX") #Remind player where he or she is (\n means new line)
        control = input("Move left, right, up, down, or stop?") #Ask what player wants to do
        control = control.lower() #Converts player input to lowercase
        if control == "a": #If left
            char_x = char_x - 1
        elif control == "d":# If right
            char_x = char_x + 1
        elif control == "w": #If up
            char_y = char_y - 1
        elif control == "s": #If down
            char_y = char_y + 1
        #elif control == "stop": #If player wants to stop
         #   go = False
        #elif control is not "left" or control is not "right" or control is not "down" or control is not "up":
         #   print("Please enter a proper direction") #If it's not one of those commands
        arena[prev_char_y][prev_char_x] = "O" #Removes previous player position marker
        arena[char_y][char_x] = "X" #Adds current player position marker (Y, X) instead of (X, Y)
        prev_char_y = char_y #Sets the previous y to the current y
        prev_char_x = char_x #Sets the previous x to current x
        list_to_string(arena) #Prints map
    except IndexError:
        print("That's out of range, please pick somewhere else to move")
        char_y = prev_char_y
        char_x = prev_char_x
        arena[char_y][char_x] = "X"
        list_to_string(arena)
    
    


while True:
    direction = input('dir: ')
    prettyPrint(tunnels)















def HeresAListOfThingsThatPremLikesToSuck():
    while True :
        for i in range(24):
            print("DICK")
        print("BALLS")

    
