from object import Object

class Bullet(Object):
		
	def __init__(self):
		Object.__init__(self)
		self.direction = 0
		self.speed = 0
		self.pos = 25
		self.color = [0,0,255]
