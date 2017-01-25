import sys
import select
import tty

class Controlling():
	'''
	The controlling class.
	'''

	def __init__(self, leds):
		'''
		Set the user input keys:
		* LEFT 		= a
		* RIGHT 	= d
		* FIRE		= h
			
		:param leds: The led's count
		'''
		self.leds = leds
		self.LEFT = "a"
		self.RIGHT = "d"
		self.NOTHING = ""
		self.FIRE = "h"
		tty.setraw(sys.stdin.fileno())

	def getUserInput(self):
		'''
		Get the user input. 
		'''
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

	def userInput(self, gameObject):
		'''
		Interpret the user input.
		:param gameObject: The game object for the user input actions. 
		'''
		userInput = self.getUserInput()
		if(userInput == self.LEFT):
			gameObject.pos -= (gameObject.speed * gameObject.direction)
			if(gameObject.pos < 0):
				gameObject.pos = 0
		elif(userInput == self.RIGHT):
			gameObject.pos += (gameObject.speed * gameObject.direction)
			if(object.pos > (self.leds) - 1):
				gameObject.pos = self.leds - 1
		elif(userInput == self.FIRE):
			gameObject.firedWeapon = True

	def moveObject(self, gameObject):
		'''
		Move the game object.
		:param gameObject: The game object.
		'''
		if(gameObject.movingCount == 0):
			gameObject.pos += (gameObject.speed * gameObject.direction)
			if(gameObject.pos == 0 and gameObject.direction == -1):
				gameObject.pos = self.leds - 1
			elif(gameObject.pos == self.leds - 1 and gameObject.direction == 1):
				gameObject.pos = 0
			gameObject.movingCount = gameObject.resetMovingCount
		else:
			gameObject.movingCount -= 1 
	
	
