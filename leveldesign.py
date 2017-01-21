from player import Player
from enemy import Enemy

class Leveldesign():

	def __init__(self, leds):
		self.leds = leds
		self.level = list()
		self.level.append(self.getFirstLevel())
		self.level.append(self.getSecondLevel())

	def getFirstLevel(self):
		level= list()
		level.append(Player())
		for enemyPos in range(8, 10):
			enemy = Enemy()
			enemy.pos = enemyPos
			level.append(enemy)
		return level


	def getSecondLevel(self):
		level= list()
		level.append(Player())
		for enemyPos in range(8, self.leds - 1):
			if(enemyPos % 4 == 0):
				enemy = Enemy()
				enemy.pos = enemyPos
				level.append(enemy)
		return level
