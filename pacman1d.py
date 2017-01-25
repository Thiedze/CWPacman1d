'''
Pacman 1D

Run this script to start the game. 

Programmed by Sebastian Thiems
Januar 2017

'''
from game import Game
import time

# Led's on the stripe
leds = 80 
game = Game(leds)

# Endless game loop. To exit press p on the keyboard.
while True:
	game.nextStep()
	time.sleep(0.02)

