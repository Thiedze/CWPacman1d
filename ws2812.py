import math
import unicornhat

class WS2812(Object):
	
	def __init__(self, maxX, maxY):
		self.maxX = maxX
		self.maxY = maxY

	def getPixel(pos):
		x = int(math.floor(pos / self.maxX))
		if(x%2 == 0):
			y = pos % (self.maxX * 2)
		else:
			y = abs((self.maxX -1) - (pos % self.maxX))
		return(x,y)

	def transmitGamePlan(game):
		for pos in range(len(game.plan)):
			x,y = getPixel(pos)
			unicornhat.set_pixel(x, y, game.plan[pos][0], game.plan[pos][1], game.plan[pos][2])
		unicornhat.show()	
