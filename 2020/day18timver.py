import re

ops = {
    1: r"(\d+|\d+\.\d+)\^(\d+\.\d+|\d+)",
    2: r"(\d+|\d+\.\d+)\*(\d+\.\d+|\d+)",
    3: r"(\d+|\d+\.\d+)\/(\d+\.\d+|\d+)",
    4: r"(\d+|\d+\.\d+)\+(\d+\.\d+|\d+)",
    5: r"(\d+|\d+\.\d+)\-(\d+\.\d+|\d+)"
}

funcs = {
    1: lambda x, y: x ** y,
    2: lambda x, y: x * y,
    3: lambda x, y: x / y,
    4: lambda x, y: x + y,
    5: lambda x, y: x - y
}


def tim(question):
    print(question)
    rejects = re.search(r"(\((\d+)((.)(\d+))+\))", question)
    if rejects is not None:
        return tim(question.replace(rejects.groups()[0], str(tim(rejects.groups()[0][1:-1])), 1))
    for priority in order:
        rejects = re.search(ops[priority], question)
        if rejects is not None:
            return tim(question.replace(rejects.group(), str(funcs[priority](float(rejects.groups()[0]), float(rejects.groups()[1]))), 1))
    return float(question)


order = [int(i)for i in input("Order: ")]
timput = input("Question: ").replace(" ", "")
print(tim(timput))
