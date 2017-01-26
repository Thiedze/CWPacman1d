from bullet import Bullet
import copy

class Weapon():
	'''
	The weapon class.
	'''

	def __init__(self):
		self.size = 2
		self.fired = False
		self.bullet = Bullet()

	def getBullets(self):
		'''
		Get the bullets for the weapon. 
		'''
		bullets = list()
		for _ in range(0, self.size):
			bullets.append(copy.copy(self.bullet))
		return bullets
