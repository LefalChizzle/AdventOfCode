from waha import Intcode

def get_joystick_input():
    
	global move_x
	global move_y

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

	    
program = Intcode.load('day15.txt')
