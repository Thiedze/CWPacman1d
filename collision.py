
class Collision():
	
	def detect(self, gamePlan, pos):
		if(gamePlan[pos] != None and gamePlan[pos].isEnemy == True):
			return True
		else:
			return False
