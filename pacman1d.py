from game import Game
from ws2812 import WS2812
from player import Player
from enemy import Enemy 
from moving import Moving
import time

from ws2812 import WS2812

x = 8
y = 10

game = Game(x, y)
ws2812 = WS2812(x, y)
player = Player()
enemy = Enemy()
moving = Moving(x, y)

while True:
	game.resetGamePlan()
	player.addPositionToGame(game, moving)
	#enemy.addPositionToGame(game, moving)
	ws2812.drawGame(game)
	
	
