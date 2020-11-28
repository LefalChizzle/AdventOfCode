def openSesame(puzzle):
    with open(puzzle) as f:
        return list(map(int, f.read().split(',')))

def digitFinder(number,digit):#finds the desired digit of a number from the right
     #is there actually no better way to do this?
    number = str(number)
    if digit >= len(number):
        return 0
    elif number[-2:] == '99':
        return 99
    elif digit == 0:#makes sure that its actually an opcode and not a random number
        if int(number[-2:]) == int(number[-1:]):
            return int(number[-1:])
        else:
            return 69 #not an opcode ^^
    else:
        return int(number[-digit-1])

def getParameter(dist):#Provides the parameter, avoids creating 3 paras for an opcode that only wants 1
    if digitFinder(program[pointer],dist+1) == 0 : #positionmode //it decided the mode too now i guess
        parameter = program[pointer + dist]
    elif digitFinder(program[pointer],dist+1) == 1 : #immediatemode
        parameter = pointer + dist
    elif digitFinder(program[pointer],dist+1) == 2 : #relative mode AAAAAAA
        #
        #print('p1',length,relbase + program[pointer + dist],relbase,pointer,dist)
        #ffs()
        parameter = relbase  + program[pointer + dist]
    x = 0
    while (relbase + program[pointer + dist]) > len(program):
        #print('p2',len(program),relbase + program[pointer + dist],relbase,pointer,dist)
        program.append(0)
        #print('help',str(x))
        x += 1
        
            
            
    return parameter

def ffs():
    print('boi')

def Intcode(program):#, noun, verb):in case they decide to bring back this thing later
    #program[1] = noun
    #program[2] = verb
    global pointer
    global relbase
    relbase = 0
    pointer = 0
    while pointer < len(program):
        #print('I',relbase, pointer, program)
        opcode = digitFinder(program[pointer],0)#finds the opcode
        if opcode == 99:
            print("Done")
            break
        elif opcode == 1 :#1-ADD
            program[getParameter(3)] = program[getParameter(1)] + program[getParameter(2)]
            pointer += 4
        elif opcode == 2 :#2-MULTIPLY
            program[getParameter(3)] = program[getParameter(1)] * program[getParameter(2)]
            pointer += 4
        elif opcode == 3 :#3-INPUT
            program[getParameter(1)] = int(input("Opcode 3 wants an input: "))
            pointer += 2
        elif opcode == 4 :#4-OUTPUT
            print("Opcode 4 would like to tell you", str(program[getParameter(1)]))
            pointer += 2
        elif opcode == 5 :#5-JUMP IF NOT ZERO
            if program[getParameter(1)] != 0 :
                pointer = program[getParameter(2)]
            else :
                pointer += 3
        elif opcode == 6 :#6-JUMP IF ZERO
            if program[getParameter(1)] == 0 :
                pointer = program[getParameter(2)]
            else :
                pointer += 3
        elif opcode == 7 :#7-LESS THAN
            if program[getParameter(1)] < program[getParameter(2)] :
                program[getParameter(3)] = 1
            else :
                program[getParameter(3)] = 0
            pointer += 4
        elif opcode == 8 :#8-EQUAL TO
            if program[getParameter(1)] == program[getParameter(2)] :
                program[getParameter(3)] = 1
            else :
                program[getParameter(3)] = 0
            pointer += 4
        elif opcode == 9 :#9-RELATIVE BASE OFFSET
            relbase += program[getParameter(1)]
            pointer += 2
        else:#Not an opcode
            print("What does that mean")
            break
        

def doathing(prog):
    global program
    program = openSesame(prog)
    Intcode(program)















