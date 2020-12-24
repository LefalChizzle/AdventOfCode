import re
with open('files/day7.txt') as file:
    ips = [i.strip() for i in file.readlines()]


def has_ABBA(word: str) -> bool:
    for i in range(len(word) - 3):
        if word[i:i+2] == word[i+3:i+1:-1] and word[i] != word[i+1]:
            return True
    else:
        return False


valid = 0
ssl = 0
for i in ips:
    reg = re.findall(r'(\w+)|\[(\w+)\]', i)

    failed = False
    in_side = " ".join([x[0] for x in reg if x[0] != ""])
    outside = " ".join([x[1] for x in reg if x[1] != ""])
    valid += 1 if has_ABBA(in_side) and not has_ABBA(outside) else 0

    # print(check, reg)

    valid += 1 if failed else 0

    for a, b, c in zip(outside, outside[1:], outside[2:]):
        if a == c and a != b and (b+a+b in in_side):
            ssl += 1
            break

print(f"part1: {valid}")
print(f"part2: {ssl}")


# Super concise version
def abba(x: str) -> bool:
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))


lines = [re.split(r'\[([^\]]+)\]', line.strip())
         for line in open('files/day7.txt')]
parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
print('part1:', sum(abba(sn) and not abba(hn) for sn, hn in parts))
print('part2:', sum(any(a == c and a != b and b+a+b in hn for a,
                        b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts))
