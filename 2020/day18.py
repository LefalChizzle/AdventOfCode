import re


def recursion(question):
    # print(question)
    rejects = re.search(r"(\((\d+)(([+*])(\d+))+\))", question)
    if rejects is not None:
        return recursion(
            question.replace(rejects.groups()[0],
                             str(recursion(rejects.groups()[0][1:-1])), 1))

    rejects = re.search(r"(\d+)([+*])(\d+)", question)
    if rejects is not None:
        x = rejects.groups()[0]
        op = rejects.groups()[1]
        y = rejects.groups()[2]
        return recursion(
            question.replace(rejects.group(),
                             str(int(x) + int(y) if op == "+"
                                 else int(x) * int(y)), 1))

    return int(question)


def regex(question):
    # print(question)
    rejects = re.search(r"(\((\d+)(([+*])(\d+))+\))", question)
    if rejects is not None:
        return regex(
            question.replace(rejects.groups()[0],
                             str(regex(rejects.groups()[0][1:-1])), 1))

    rejects = re.search(r"(\d+)\+(\d+)", question)
    if rejects is not None:
        return regex(
            question.replace(rejects.group(),
                             str(int(rejects.groups()[0])
                                 + int(rejects.groups()[1])), 1))

    rejects = re.search(r"(\d+)\*(\d+)", question)
    if rejects is not None:
        return regex(
            question.replace(rejects.group(),
                             str(int(rejects.groups()[0])
                                 * int(rejects.groups()[1])), 1))

    return int(question)


with open("files/day18.txt") as file:
    homework = [i.replace(" ", "") for i in file.readlines()]

x = 0
y = 0
for i in homework:
    x += recursion(i)
    y += regex(i)

print(f"part1: {x}")
print(f"part2: {y}")
