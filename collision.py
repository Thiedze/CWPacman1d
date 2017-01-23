from player import Player
from enemy import Enemy
from finish import Finish

class Collision():
	
	def detectEnemy(self, gamePlan, object):
		if(isinstance(object, Player) and isinstance(gamePlan[object.pos], Enemy)):
			return True
		elif(isinstance(object, Enemy) and isinstance(gamePlan[object.pos], Player)):
			return True
		else:
			return False

	def detectFinish(self, gamePlan, object):
		if(isinstance(gamePlan[object.pos], Finish)):
			return True
		else:
			return False
