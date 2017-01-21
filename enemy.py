from object import Object

class Enemy(Object):

	def __init__(self):
		Object.__init__(self)
		self.pos = 8
		self.color = [255,0,0]
		self.direction =  -1
		self.speed = 0
