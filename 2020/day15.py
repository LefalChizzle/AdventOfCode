startnos = [15, 5, 1, 4, 7, 0]

# print(startnos)


def isItThatEasy(iwantthis):
    dictionariesarevuseful = {j: i+1 for i, j in enumerate(startnos)}
    # print(dictionariesarevuseful)

    previous = startnos[-1]

    # "initial" (current position, current position) you want to get to
    for i in range(len(startnos)+1, iwantthis + 1):
        if previous in dictionariesarevuseful:
            current = i - 1 - dictionariesarevuseful[previous]
        else:
            current = 0

        dictionariesarevuseful[previous] = i-1
        previous = current

    print(previous)


isItThatEasy(2020)
isItThatEasy(30000000)
