from object import Object

class Player(Object):

	def __init__(self):
		Object.__init__(self)
		self.direction = 0
		self.color = [0,255,0]


