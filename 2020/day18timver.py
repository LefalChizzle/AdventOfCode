
import re

ops = {
    1: r"(\d+)\^(\d+)",
    2: r"(\d+)\*(\d+)",
    3: r"(\d+)\/(\d+)",
    4: r"(\d+)\+(\d+)",
    5: r"(\d+)\-(\d+)"
}


def tim(question):
    # print(question)
    rejects = re.search(r"(\((\d+)(([+*])(\d+))+\))", question)
    if rejects is not None:
        return tim(question.replace(rejects.groups()[0],str(tim(rejects.groups()[0][1:-1])), 1))

    rejects = re.search(ops[1][0], question)
    if rejects is not None:
        return tim(question.replace(rejects.group(), str(int(rejects.groups()[0]) ** int(rejects.groups()[1])), 1))

    rejects = re.search(ops[2][0], question)
    if rejects is not None:
        return tim(question.replace(rejects.group(), str(int(rejects.groups()[0]) * int(rejects.groups()[1])), 1))

    rejects = re.search(ops[3][0], question)
    if rejects is not None:
        return tim(question.replace(rejects.group(), str(int(rejects.groups()[0]) / int(rejects.groups()[1])), 1))

    rejects = re.search(ops[4][0], question)
    if rejects is not None:
        return tim(question.replace(rejects.group(), str(int(rejects.groups()[0]) + int(rejects.groups()[1])), 1))

    rejects = re.search(ops[5][0], question)
    if rejects is not None:
        return tim(question.replace(rejects.group(),str(int(rejects.groups()[0]) - int(rejects.groups()[1])), 1))

    return int(question)

# todo refactor to allow user to pick a operation order


timput = "5+3*2"
print(tim(timput.replace(" ", "")))
timput = "4 * 3 + 5 * 6 ^ 2"
print(tim(timput.replace(" ", "")))
timput = input("Question: ")
print(tim(timput.replace(" ", "")))
