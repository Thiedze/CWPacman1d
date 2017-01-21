
class Object():

	def __init__(self):
		self.pos = 0
		self.color = [255,255,255]
		self.direction = 1
		self.speed = 1

	def addPositionToGame(self, game, moving):
		self.pos = moving.change(self.pos, self.direction , self.speed)
		game.setObject(self)
