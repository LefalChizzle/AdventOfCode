import re
from collections import Counter
with open('files/day4.txt') as file:
    imp = re.findall(r'([a-z-]+)(\d+)\[(\w+)\]', file.read())


def seize_her_augustus(shift):
    alph = "abcdefghijklmnopqrstuvwxyz"
    x = shift % 26
    # this is the gigachad method of doing ciphers in python
    return str.maketrans(alph, alph[x:] + alph[:x])


ans1 = 0
for roomname, _, checksum in imp:
    _ = int(_)
    letters = ''.join(c for c in roomname if c in "abcdefghijklmnopqrstuvwxyz")
    tops = [(-n, c) for c, n in Counter(letters).most_common()]
    ranked = ''.join(c for n, c in sorted(tops))
    if ranked.startswith(checksum):
        ans1 += _
        deroomnamed = roomname.translate(seize_her_augustus(_))
        if 'object' in deroomnamed:
            print(deroomnamed, _)
        # print(deroomnamed, _)


# print(imp)
# for room in imp:
#     print(room[0])
#     count = 0
print(ans1)
