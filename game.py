
class GamePlan(Object):
	
	def __init__(self):
		self.maxX = 8
		self.maxY = 8
		self.plan = list()
		self.initGamePlan()
	
	def initGamePlan(self):
		for pos in range(self.maxX * self.maxY):
			self.plan.append([0,0,0])

	def resetGamePlan():
		for pos in range(self.maxX * self.maxY):
			self.plan.[pos] = [0,0,0]
