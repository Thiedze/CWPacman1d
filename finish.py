from object import Object

class Finish(Object):
		
	def __init__(self):
		Object.__init__(self)
		self.direction = 0
		self.isFinish = True
		self.speed = 0
		self.pos = 30
		self.color = [255,255,0]
