from gameobject import GameObject

class Bullet(GameObject):
	'''
	The bullet game object class.
	'''
		
	def __init__(self):
		GameObject.__init__(self)
		self.direction = 0
		self.speed = 0
		self.pos = 25
		self.color = [0,0,255]
