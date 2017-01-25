from player import Player
from enemy import Enemy
from finish import Finish

class Collision():
	'''
	The collision class. 
	'''
	
	def detectEnemy(self, gamePlan, gameObject):
		'''
		Detect an enemy if:
		
		1. The game object is a player and move on an enemy
		2. The game object is a enemy and move on an player
		:param gamePlan: The game plan
		:param gameObject: The game object to check the collision for
		'''
		if(isinstance(gameObject, Player) and isinstance(gamePlan[gameObject.pos], Enemy)):
			return True
		elif(isinstance(gameObject, Enemy) and isinstance(gamePlan[gameObject.pos], Player)):
			return True
		else:
			return False

	def detectFinish(self, gamePlan, gameObject):
		'''
		Detect if the player reach the finish game object.
		:param gamePlan: The game plan.
		:param gameObject: The game object to check the collision for.
		'''
		if(isinstance(gamePlan[gameObject.pos], Finish)):
			return True
		else:
			return False
