from time import time
with open('files/day19.txt') as file:
    inputs = file.read().split("\n\n")
    rules = {i[0:i.index(":")]: [x.split(" ")
                                 for x in i[i.index(":") + 2:].split(" | ")]
             for i in inputs[0].splitlines()}
    checks = inputs[1].split()

# print(checks)
# print(rules)


def whycantiuseprocedural(rules, ruleno, string, startrule):
    currentrule = rules.get(ruleno)
    if currentrule[0][0][0] == '"':
        if startrule < len(string) \
                and currentrule[0][0][1] == string[startrule]:
            return {startrule + 1}
        else:
            return set()
    else:
        bottom = set()
        for subrule in currentrule:
            temp = {startrule}
            for linkedrule in subrule:
                temptwo = set()
                for loc in temp:
                    temptwo = temptwo.union(whycantiuseprocedural(
                        rules, linkedrule, string, loc))
                temp = temptwo
            bottom = bottom.union(temp)
        return bottom


start = time()
matchp1 = [len(x) in whycantiuseprocedural(rules, '0', x, 0) for x in checks]
# print(match)

mid = time()
rules.update({"8": [["42"], ["42", "8"]]})
rules.update({"11": [["42", "31"], ["42", "11", "31"]]})
matchp2 = [len(x) in whycantiuseprocedural(rules, '0', x, 0) for x in checks]
end = time()

print(f"part1: {matchp1.count(True)}, in {mid-start}")
print(f"part2: {matchp2.count(True)}, in {end-mid},\nin {end-start}")
