with open('files/day8.txt') as file:
    instructions = [i.strip().split() for i in file.readlines()]

executed = [False]*len(instructions)
acc = 0
pc = 0


# part1
while pc < len(instructions):
    if executed[pc]:
        print(f"part1: {acc}")
        break

    executed[pc] = True

    if instructions[pc][0] == "acc":
        acc += int(instructions[pc][1])
        pc += 1
    if instructions[pc][0] == "jmp":
        pc += int(instructions[pc][1])
    if instructions[pc][0] == "nop":
        pc += 1

# part2
for i in range(len(instructions)):
    flag = False
    if instructions[i][0] == "jmp":
        previnst = instructions[i][0]
        instructions[i][0] = "nop"
        flag = True
    elif instructions[i][0] == "nop":
        previnst = instructions[i][0]
        instructions[i][0] = "jmp"
        flag = True

    executed = [False]*len(instructions)
    acc = 0
    pc = 0
    while pc < len(instructions) and pc > -1:
        if executed[pc]:
            break
        executed[pc] = True

        if instructions[pc][0] == "acc":
            acc += int(instructions[pc][1])
            pc += 1
        elif instructions[pc][0] == "jmp":
            pc += int(instructions[pc][1])
        elif instructions[pc][0] == "nop":
            pc += 1
    else:
        print("part2:", acc)

    if flag:
        instructions[i][0] = previnst

# TODO python parses +1 and -1 as ints (because they are duh)
