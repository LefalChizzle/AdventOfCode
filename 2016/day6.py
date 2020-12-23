from collections import Counter
with open('files/day6.txt') as file:
    messages = [i.strip() for i in file.readlines()]

print(messages)

p1 = ""
p2 = ""
for i in range(len(messages[0])):
    track = Counter([j[i] for j in messages])
    p1 += track.most_common(1)[0][0]
    p2 += track.most_common()[-1][0]
print(f"part1: {p1}")
print(f"part2: {p2}")
