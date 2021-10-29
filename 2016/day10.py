import re

# with open('test.txt') as file:
with open('files/day10.txt') as file:
    instructions = file.read()

# Part 1

bot_regex = r'bot (\d+) gives low to (\b.+\b) (\d+) and high to (\b.+\b) (\d+)'
matches = re.finditer(bot_regex, instructions, re.MULTILINE)

distrules = {}
for match in matches:
	distrules.update({int(match.group(1)):((match.group(2),int(match.group(3))),(match.group(4),int(match.group(5))))})

# print(distrules)

val_regex = r'value (\d+) goes to bot (\d+)'


robohands = {}
outputs = {}

PARTONEVALONE = 17
PARTONEVALTWO = 61
PARTONEANSWER = []

def give(value, bot, isOutput):
	if isOutput:
		outputs.update({bot:outputs.setdefault(bot, [])+[value]})
	elif robohands.get(bot):
		if (PARTONEVALONE==value and PARTONEVALTWO==robohands[bot]) or (PARTONEVALONE==robohands[bot] and PARTONEVALTWO==value):
			PARTONEANSWER.append(bot)
			print(f"THE ANSWER IS {bot}")
		if robohands[bot] < value:
			give(robohands.get(bot),distrules.get(bot)[0][1], distrules.get(bot)[0][0] == 'output')
			give(value,distrules.get(bot)[1][1], distrules.get(bot)[1][0] == 'output')
		else:
			give(robohands.get(bot), distrules.get(bot)[1][1], distrules.get(bot)[1][0] == 'output')

			give(value, distrules.get(bot)[0][1], distrules.get(bot)[0][0] == 'output')

		robohands.pop(bot)

	else:
		robohands.update({bot:value})

matches = re.finditer(val_regex, instructions, re.MULTILINE)
for match in matches:
	# print(f'value {match.group(1)} goes to bot {match.group(2)}')
	give(int(match.group(1)), int(match.group(2)), False)
	# print("---")
	# print(robohands)
	# print()
	# print(outputs)



print(f'Part1: {PARTONEANSWER[0]}')

#part 2
print(f'Part2: {outputs[0][0]*outputs[1][0]*outputs[2][0]}')





# class chipbot:
# 	def __init__(self, id, give_lo, give_hi):
# 		self.id = id
# 		self.hands = []
	
# 	def give(self, microchip):
# 		self.hands.append(microchip)
# 		if len(self.hands) == 2:
# 			self.give()

# 	def give(self):
# 		pass


# print()
# print()

# x = {}
# x.update({1:[2]})
# x.update({1:x.setdefault(1, [])+[4]})
# x.update({2:x.setdefault(2, [])+[17]})
# print(x)