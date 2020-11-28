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
    return parameter

def Intcode(program,inp1,inp2):#, noun, verb):in case they decide to bring back this thing later
    #program[1] = noun
    #program[2] = verb
    global pointer
    pointer = 0
    day7flag = 0
    while pointer < len(program):
        opcode = digitFinder(program[pointer],0)#finds the opcode
        if opcode == 99:
            print("Done")
            break
        elif opcode == 1 :#1
            program[getParameter(3)] = program[getParameter(1)] + program[getParameter(2)]
            pointer += 4
        elif opcode == 2 :#2
            program[getParameter(3)] = program[getParameter(1)] * program[getParameter(2)]
            pointer += 4
        elif opcode == 3 :#3
            #program[getParameter(1)] = int(input("Opcode 3 wants an input: "))
            if day7flag == 0:
                program[getParameter(1)] = inp1
                day7flag += 1
            else :
                program[getParameter(1)] = inp2
            pointer += 2
        elif opcode == 4 :#4
            #print("Opcode 4 would like to tell you", str(program[getParameter(1)]))
            return (program[getParameter(1)])
            print("lol")
            pointer += 2
        elif opcode == 5 :#5
            if program[getParameter(1)] != 0 :
                pointer = program[getParameter(2)]
            else :
                pointer += 3
        elif opcode == 6 :#6
            if program[getParameter(1)] == 0 :
                pointer = program[getParameter(2)]
            else :
                pointer += 3
        elif opcode == 7 :#7
            if program[getParameter(1)] < program[getParameter(2)] :
                program[getParameter(3)] = 1
            else :
                program[getParameter(3)] = 0
            pointer += 4
        elif opcode == 8 :#8
            if program[getParameter(1)] == program[getParameter(2)] :
                program[getParameter(3)] = 1
            else :
                program[getParameter(3)] = 0
            pointer += 4
        else:#Not an opcode
            print("What does that mean")
            break

possibilities = []
def permutations(string, step = 0):
	if step == len(string):
		# we've gotten to the end, print the permutation
		possibilities.append("".join(string))
	for i in range(step, len(string)):
		# copy the string (store as array)
		string_copy = [c for c in string]
		# swap the current index with the step
		string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
		#recurse on the portion of the stringthat has not been swapped yet
		permutations(string_copy, step + 1)



program = openSesame('day7.txt')
permutations('01234')
signalmax = 0
sequencebest = 0
for sequence in possibilities :
    nextphase =0
    for phase in sequence :
        #print(nextphase, end =' ')
        nextphase = Intcode(program,int(phase),nextphase)
        #print(nextphase)
    if int(nextphase) > int(signalmax) :
        signalmax = nextphase
        sequencebest = sequence
print(signalmax, sequencebest)















