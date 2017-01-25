from neopixel import *

class Drawing():
	'''
	The drawing class.
	'''
	
	def __init__(self, leds):
		self.leds = leds
		self.strip = Adafruit_NeoPixel(leds, 18, 800000, 5, False, 255)
		self.strip.begin()
		self.emptyPlaceColor = [0, 0, 0]

	def gamePlan(self, plan):
		'''
		Draw the game plan. (Send to the stripe)		
		:param plan: The game plan to draw.
		'''
		for led in range(self.leds):
			if(plan[led] == None):
				self.strip.setPixelColorRGB(led, self.emptyPlaceColor[0], self.emptyPlaceColor[1], self.emptyPlaceColor[2])
			else:
				self.strip.setPixelColorRGB(led, plan[led].color[0], plan[led].color[1], plan[led].color[2])
		self.strip.show()
		
