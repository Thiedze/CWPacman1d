from gameobject import GameObject

class Enemy(GameObject):
	'''
	The enemy game object class.
	'''

	def __init__(self):
		GameObject.__init__(self)
		self.color = [0,255,0]
		self.direction = -1
		self.speed = 2
		self.hitCount = 2
