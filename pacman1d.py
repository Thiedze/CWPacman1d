from game import Game
import time

leds = 80
game = Game(leds)

while True:
	game.nextStep()
	time.sleep(0.02)
	#time.sleep(2)

