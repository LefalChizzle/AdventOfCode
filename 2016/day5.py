import hashlib

number = 0
# DoorID = "abc"  # test
DoorID = "abbhdwsy"  # input
part1 = ""
for i in range(8):
    while True:
        str2bin = DoorID + str(number)
        bin2hash = str2bin.encode()
        hash2hex = hashlib.md5(bin2hash)
        result = hash2hex.hexdigest()

        number += 1
        if result[:5] == "00000":
            part1 += result[5]
            break
print(f"part1: {part1}")

number = 0
part2 = [""]*8
while part2.count("") > 0:
    str2bin = DoorID + str(number)
    bin2hash = str2bin.encode()
    hash2hex = hashlib.md5(bin2hash)
    result = hash2hex.hexdigest()
    # print("The hexadecimal equivalent of hash is : ", end="")
    # print(result)
    number += 1
    if result[5] in "12345670" and result[:5] == "00000" and part2[int(result[5])] == "":
        part2[int(result[5])] = result[6]
    else:
        pass
print(f"part2: {''.join(part2)}")
