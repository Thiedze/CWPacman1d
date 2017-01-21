import math
from neopixel import *
from random import randint

class Drawing():
	
	def __init__(self, leds):
		self.leds = leds
		self.strip = Adafruit_NeoPixel(leds, 18, 800000, 5, False, 255)
		self.strip.begin()

	def gamePlan(self, plan):
		for led in range(self.leds):
			if(plan[led] == None):
				self.strip.setPixelColorRGB(led, 0,0,0)
			else:
				self.strip.setPixelColorRGB(led, plan[led].color[0], plan[led].color[1], plan[led].color[2])
		self.strip.show()
		
