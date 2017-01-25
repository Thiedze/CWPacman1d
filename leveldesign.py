from player import Player
from enemy import Enemy
from finish import Finish

class Leveldesign():
	'''
	The level design class. 
	
	Design here the level. Every level should have a player and a finish. 
	'''

	def __init__(self, leds):
		self.leds = leds
		self.level = list()
		self.level.append(self.getFirstLevel())
		self.level.append(self.getSecondLevel())

	def getFirstLevel(self):
		'''
		The first level.
		'''
		level= list()
		level.append(Player())
		for enemyPos in range(20, 22):
			enemy = Enemy()
			enemy.pos = enemyPos
			level.append(enemy)
		finish = Finish()
		finish.pos = self.leds - 1
		level.append(finish)
		return level


	def getSecondLevel(self):
		'''
		The second level.
		'''
		level= list()
		level.append(Player())
		for enemyPos in range(7, self.leds - 1):
			if(enemyPos % 20 == 0):
				enemy = Enemy()
				enemy.pos = enemyPos
				level.append(enemy)
		finish = Finish()
		finish.pos = self.leds - 1
		level.append(finish)
		return level
