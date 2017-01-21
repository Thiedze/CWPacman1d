import sys
import select
import tty

class Moving():

	def __init__(self, maxX, maxY):
		self.maxX = maxX
		self.maxY = maxY
		tty.setraw(sys.stdin.fileno())

	def getDirection(self):
		while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
			sys.stdout.flush()
			char = sys.stdin.read(1)
			if char:
				print char
				if(char == "d"):
					return 1
				elif(char == "a"):
					return -1
				elif(char == "p"):
					exit()
			else: 
				return 0
		else:
			return 0

	def change(self, currentPos, direction, speed):
		newPos = currentPos + (speed * self.getDirection())
		if(newPos > (self.maxX * self.maxY) - 1):
				newPos =  self.maxX * self.maxY - 1
		if(newPos < 0):
				newPos = 0	
		return newPos
	
	
