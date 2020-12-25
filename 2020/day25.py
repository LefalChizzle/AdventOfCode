inp = """18356117
5909654""".split()

# inp = """5764801
# 17807724""".split()

card_pub = int(inp[0])
door_pub = int(inp[1])

#start 1
start = 1
subject_no = 7
loopsize = 0
while True:
    loopsize += 1
    start = start * subject_no
    start = start % 20201227
    if start == card_pub:
        print(loopsize)
        break

start = 1
subject_no = 7
loopsize = 0
while True:
    loopsize += 1
    start *= subject_no
    start %= 20201227
    if start == door_pub:
        print(loopsize)
        break

start = 1
for i in range(loopsize):
    start *= card_pub 
    start %= 20201227
print(start)