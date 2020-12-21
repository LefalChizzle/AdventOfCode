'''
#!/usr/bin/python3

from waho import Intcode

state = 0
x = None
y = None
blocks = set()

def handle_game_output(data):

	global state
	global x
	global y
	global blocks

	if state == 0:
		x = data
	elif state == 1:
		y = data
	elif data == 2:
		blocks.add((x, y))

	state = (state + 1) % 3

ram = Intcode.load("day13.txt")
arcade = Intcode(ram)
arcade.add_output(handle_game_output)
arcade.run()
print(len(blocks))
'''
#!/usr/bin/python3

from waho import Intcode

state = 0
x = None
y = None
score = None
ball_x = None
paddle_x = None

def get_joystick_input():

	global ball_x
	global paddle_x

	if ball_x == None or paddle_x == None:
		return 0
	elif ball_x < paddle_x:
		return -1
	elif ball_x > paddle_x:
		return 1
	else:
		return 0

def handle_game_output(data):

	global state
	global x
	global y
	global score
	global ball_x
	global paddle_x

	if state == 0:
		x = data
	elif state == 1:
		y = data
	elif x == -1 and y == 0:
		score = data
	elif data == 3:
		paddle_x = x
	elif data == 4:
		ball_x = x

	state = (state + 1) % 3

ram = Intcode.load("day13.txt")
ram[0] = 2
arcade = Intcode(ram)
arcade.set_input(get_joystick_input)
arcade.add_output(handle_game_output)
arcade.run()
print(score)
