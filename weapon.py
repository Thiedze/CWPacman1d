from bullet import Bullet
import copy

class Weapon():

	def __init__(self):
		self.size = 2
		self.bullet = Bullet()

	def getBullets(self):
		bullets = list()
		for bullet in range(0, self.size):
			bullets.append(copy.copy(self.bullet))
		return bullets
