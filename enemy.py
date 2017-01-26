from gameobject import GameObject

class Enemy(GameObject):
	'''
	The enemy game object class.
	'''

	def __init__(self):
		GameObject.__init__(self)
		self.hitCount = 1
		self.life = 10
		self.color = [0, 255, 0]
		self.direction = -1
		self.speed = 2
		
