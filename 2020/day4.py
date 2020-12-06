with open("files/day4.txt") as file:
    passports = [eval("{'"+i.strip().replace("\n", " ").replace(" ", "', '")
                 .replace(":", "':'")+"'}")
                 for i in file.read().split("\n\n")]
    # print(passports)

p1count = 0
p2count = 0
for i in passports:
    # count += 1 if len(i) == (8 if "cin" in i.keys() else 7) else 0
    print(i)
    if ("byr" in i.keys() and "iyr" in i.keys() and "eyr" in i.keys() and "hgt"
            in i.keys() and "hcl" in i.keys() and "ecl" in i.keys() and "pid"
            in i.keys()):

        valid = [False]*7

        valid[0] = int(i.get("byr")) >= 1920 and 2002 >= int(i.get("byr"))

        valid[1] = int(i.get("iyr")) >= 2010 and 2020 >= int(i.get("iyr"))

        valid[2] = int(i.get("eyr")) >= 2020 and 2030 >= int(i.get("eyr"))

        # if i.get("hgt")[-2] == "c": valid[3] = int(i.get("hgt")[:-2]) >= 150
        # and 193 >= int(i.get("hgt")[:-2])
        # elif i.get("hgt")[-2] == "i": valid[3] = int(i.get("hgt")[:-2]) >=\
        # 59 and 76 >= int(i.get("hgt")[:-2])

        valid[3] = (int(i.get("hgt")[:-2]) >= 150 and
                    193 >= int(i.get("hgt")[:-2]) if i.get("hgt")[-2] == "c"
                    else int(i.get("hgt")[:-2]) >= 59 and
                    76 >= int(i.get("hgt")[:-2]) if
                    i.get("hgt")[-2] == "i" else False)

        valid[4] = (i.get("hcl")[0] == "#" and
                    False not in [i in "0123456789abcdef" for i in
                    list(i.get("hcl")[1:])])

        valid[5] = (i.get("ecl") in
                    ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

        valid[6] = len(i.get("pid")) == 9

        print(valid)

        p1count += 1
        p2count += 1 if False not in valid else 0

print(p1count, p2count)
