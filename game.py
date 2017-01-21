from collision import Collision

class Game():
	
	def __init__(self, maxX , maxY):
		self.maxX = maxX
		self.maxY = maxY
		self.collision = Collision()
		self.plan = list()
		self.initGamePlan()
		self.lost = False
	
	#def fireWeapon(self, player):
		

	def setObject(self, object):
		if(self.collision.detect(self.plan, object.pos) == False):
			self.plan[object.pos] = object
		else:
			self.lost = True			

	def initGamePlan(self):
		for pos in range(self.maxX * self.maxY):
			self.plan.append(None)

	def resetGamePlan(self):
		for pos in range(self.maxX * self.maxY):
			self.plan[pos] = None
