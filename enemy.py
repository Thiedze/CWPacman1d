from object import Object

class Enemy(Object):

	def __init__(self):
		Object.__init__(self)
		self.color = [0,255,0]
		self.direction =  0
		self.speed = 0
		self.isEnemy = True
