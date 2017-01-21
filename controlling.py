import sys
import select
import tty

class Controlling():

	def __init__(self, leds):
		self.leds = leds
		self.LEFT = "a"
		self.RIGHT = "d"
		self.NOTHING = ""
		self.FIRE = "h"
		tty.setraw(sys.stdin.fileno())

	def getUserInput(self):
		while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
			sys.stdout.flush()
			char = sys.stdin.read(1)
			if char:
				print char
				if(char == self.RIGHT):
					return self.RIGHT
				elif(char == self.LEFT):
					return self.LEFT
				elif(char == self.FIRE):
					return self.FIRE
				elif(char == "p"):
					exit()
			else: 
				return self.NOTHING
		else:
			return self.NOTHING

	def userInput(self, object):
		userInput = self.getUserInput()
		if( userInput == self.LEFT ):
			object.pos -= (object.speed * object.direction)
			if(object.pos < 0):
				object.pos = 0
		elif( userInput == self.RIGHT ):
			object.pos += (object.speed * object.direction)
			if(object.pos > (self.leds) - 1):
				object.pos =  self.leds - 1
		elif( userInput == self.FIRE ):
			object.firedWeapon = True
	
	
