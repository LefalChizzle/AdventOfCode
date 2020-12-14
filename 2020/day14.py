with open('files/test.txt') as file:
    instructions = [i.strip().split(" = ") for i in file.readlines()]


def get_bin(x, n=0):
    """
    thanks stackoverflow

    Get the binary representation of x.

    Parameters
    ----------
    x : int
    n : int
        Minimum number of digits. If x needs less digits in binary, the rest
        is filled with zeros.

    Returns
    -------
    str
    """
    return format(x, 'b').zfill(n)


def applyMask(mask, number):
    binNumber = get_bin(int(number), 36)
    newNumber = []
    for i in range(len(binNumber)):
        if mask[i] == '1' or mask[i] == '0':
            newNumber.append(mask[i])
        else:
            newNumber.append(binNumber[i])
    return "".join(newNumber)

# this was not the wae
# def p2applyMask(mask, number):
#     print("yo", mask, number)
#     binNumber = get_bin(int(number), 36)
#     newNumber = []
#     lotsanewnums = []
#     for i in range(len(binNumber)):
#         if mask[i] == '1' or mask[i] == 'X':
#             newNumber.append(mask[i])
#         else:
#             newNumber.append(binNumber[i])
#     return "".join(newNumber)

# im going to use recursion because why t f not


memoryp1 = {}
memoryp2 = {}
for i, j in instructions:
    if i == 'mask':
        memoryp1.update({i: j})
        memoryp2.update({i: j})

    elif i[0:3] == 'mem':
        new = int(applyMask(memoryp1.get('mask'), j), base=2)
        # print(i, new, memory)
        memoryp1.update({i: str(new)})

        # newMem = i[0:3] str(int(applyMask(memoryp2.get('mask'), i[4:-1]), base=2))
        print(p2applyMask(memoryp2.get('mask'), i[4:-1]))
        # memoryp2.update({newMem: j})

# print(memory)
print(sum([int(j) for i, j in memoryp1.items() if i != 'mask']))
print(memoryp2)
# print(sum([int(j) for i, j in memoryp2.items() if i != 'mask']))
