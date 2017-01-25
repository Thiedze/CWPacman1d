from gameobject import GameObject

class Finish(GameObject):
	'''
	The finish game object class.
	'''
		
	def __init__(self):
		GameObject.__init__(self)
		self.direction = 0
		self.isFinish = True
		self.speed = 0
		self.pos = 30
		self.color = [255,255,0]
