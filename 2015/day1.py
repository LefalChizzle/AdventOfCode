with open('files/day1.txt') as file:
    select = {
        "(": 1,
        ")": -1
    }
    brackets = [select.get(i) for i in file.read()]

print(f"part1: {sum(brackets)}")

for i in range(len(brackets)):
    if sum(brackets[:i]) == -1:
        print(f"part2: {i}")
        break
