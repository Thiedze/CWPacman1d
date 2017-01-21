import math
import unicornhat
from random import randint

class WS2812():
	
	def __init__(self, maxX, maxY):
		self.maxX = maxX
		self.maxY = maxY

	def getPixel(self, pos):
		x = int(math.floor(pos / self.maxX))
		if(x%2 == 0):
			y = pos % (self.maxX * 2)
		else:
			y = abs((self.maxX -1) - (pos % self.maxX))
		return(x,y)

	def drawGame(self, game):
		for pos in range(len(game.plan)):
			x,y = self.getPixel(pos)
			if(game.lost == True):
				unicornhat.set_pixel(x, y, randint(0,255), randint(0,255), randint(0,255))
			else:
				if(game.plan[pos] == None):
					unicornhat.set_pixel(x, y, 0,0,0)
				else:
					unicornhat.set_pixel(x, y, game.plan[pos].color[0], game.plan[pos].color[1], game.plan[pos].color[2])
		unicornhat.show()	
