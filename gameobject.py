
class GameObject():
	'''
	The game object.
	'''

	def __init__(self):
		self.pos = 0
		self.color = [255,255,255]
		self.direction = 1
		self.speed = 1
		self.hasWeapon = False
		self.firedWeapon = False
		self.movingCount = 20
		self.resetMovingCount = self.movingCount 
