from object import Object

class Enemy(Object):

	def __init__(self):
		Object.__init__(self)
		self.color = [0,255,0]
		self.direction = -1
		self.speed = 2
		self.hitCount = 2
