import re
from collections import deque
# with open("test.txt") as file:
with open("files/day9.txt") as file:
    kmi = file.read().strip()

# Part 1
x = deque(kmi)
out = ""
# print("".join(x))
pointer = 0
while len(x):
    # print("outer", x)
    if x[0] == "(":
        y = ""
        while x[0] != ")":
            y += x.popleft()
        y += x.popleft()
        r, ln = y[1:-1].split("x")
        s = ""
        for i in range(int(r)):
            # print("inner1", x)
            s += x.popleft()
        for i in range(int(ln)):
            # print("inner2", x)
            out += s

    else:
        out += x.popleft()

# print(out, len(out))
print(f"part1: {len(out)}")


# Part 2

# OOF that didnt work

# x = deque(kmi)
# out = ""
# # print("".join(x))
# pointer = 0
# while True:
#     while len(x):
#         # print("outer", x)
#         if x[0] == "(":
#             y = ""
#             while x[0] != ")":
#                 y += x.popleft()
#             y += x.popleft()
#             r, ln = y[1:-1].split("x")
#             s = ""
#             for i in range(int(r)):
#                 # print("inner1", x)
#                 s += x.popleft()
#             for i in range(int(ln)):
#                 # print("inner2", x)
#                 out += s

#         else:
#             out += x.popleft()
#     print(len(out))
#     if out.count("(") > 0:
#         # print(x)
#         x = deque(out)
#         out = ""
#     else:
#         break

# print(out, len(out))

# retry
def aaa_this_took_so_loooooooooong(text):
    rle = re.search(r"\(([0-9]+)x([0-9]+)\)", text)
    size = 0
    if rle:
        st = len(text[:rle.start()])
        run = (text[rle.end():rle.end()+int(rle.group(1))])
        length = aaa_this_took_so_loooooooooong(run) * int(rle.group(2))
        run = aaa_this_took_so_loooooooooong(
            text[rle.end()+int(rle.group(1)):])
        size = st+length+run
    else:
        size = len(text)
    return size


# damn i thought i was clever for using deque
# i was not
ans2 = aaa_this_took_so_loooooooooong(kmi)


print(f"part2: {ans2}")
