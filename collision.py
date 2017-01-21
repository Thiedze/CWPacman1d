
class Collision():
	
	def detect(self, gamePlan, pos):
		if(gamePlan[pos] != None):
			return True
		else:
			return False
