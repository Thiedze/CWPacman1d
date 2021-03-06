from collision import Collision
from leveldesign import Leveldesign
from drawing import Drawing
from controlling import Controlling
from player import Player
from bullet import Bullet
from enemy import Enemy
import copy


class Game():
	'''
	This class is the main class of the project. 
	It holds the game logic and coordinates the game flow.  
	'''	
	
	def __init__(self, leds):
		'''
		Init the game plan and set the start level (0)
		
		:param leds: Led's on the stripe
		'''
		self.leds = leds
		self.collision = Collision()
		self.leveldesign = Leveldesign(self.leds)
		self.drawing = Drawing(leds)
		self.controlling = Controlling(leds)
		self.plan = list()
		self.initGamePlan()
		self.level = 0

	def fireWeapon(self, gameObject):
		'''
		Fire the weapon. No check if the game object has a weapon.
		:param gameObject: The game object that fired
		'''
		bullets = gameObject.weapon.getBullets()
		for pos in range(0, gameObject.weapon.size):
			if((gameObject.pos + pos + 1) < self.leds):
				bullets[pos].pos = gameObject.pos + pos + 1
				if(isinstance(self.plan[gameObject.pos + pos + 1], Enemy)):
					self.plan[gameObject.pos + pos + 1].hitCount += 1
					if(self.plan[gameObject.pos + pos + 1].hitCount == self.plan[gameObject.pos + pos + 1].life):
						self.plan[gameObject.pos + pos + 1] = bullets[pos]
				elif(self.plan[gameObject.pos + pos + 1] == None):
					self.plan[gameObject.pos + pos + 1] = bullets[pos]
			if((gameObject.pos - pos - 1) >= 0):
				bullets[pos].pos = gameObject.pos - pos - 1
				self.plan[gameObject.pos - pos - 1] = bullets[pos]

	def lostLife(self, gameObject):
		'''
		Lost a life.
		:param gameObject: The game object that lost a life
		'''
		gameObject.life -= 1
		self.setLevel(self.leveldesign.level[self.level])
		
	def lostGame(self, gameObject):
		'''
		Lost the game. Reset to level 0.
		:param gameObject:
		'''
		self.level = 0
		gameObject.life = gameObject.resetLife
		self.setLevel(self.leveldesign.level[self.level])

	def hitByEnemy(self, gameObject):
		'''
		Check if the object is a player and hits an enemy or visa versa. 
		:param gameObject: The game object to check ifhit by an enemy
		'''
		if(isinstance(self.plan[gameObject.pos], Player) and self.plan[gameObject.pos].life <= 1):
			self.lostGame(self.plan[gameObject.pos])
		elif(isinstance(gameObject, Player) and gameObject.life < 1):
			self.lostGame(gameObject)
		else:
			if(isinstance(self.plan[gameObject.pos], Player)):
				self.lostLife(self.plan[gameObject.pos])
			elif(isinstance(gameObject, Player)):
				self.lostLife(gameObject)		

	def reachFinish(self):
		'''
		Reach the level finish and set the new level.
		'''
		self.level += 1
		if(self.level >= len(self.leveldesign.level)):
			self.level = 0
		self.setLevel(self.leveldesign.level[self.level])

	def checkBullets(self):
		for gameObject in self.plan:
			if(isinstance(gameObject, Bullet)):
				return True
		return False

	def runGameLogic(self, gameObject):
		'''
		Run the game logic. 
		1. Check the collision if the game object hits an enemy
		2. If not hit an enemy -> Check the collision if the game object reach the finish
		3. If not reach the finish -> fire the weapon
		
		At least set the game object to the game plan
		:param gameObject: The game object for the game logic
		'''
		if(self.collision.detectEnemy(self.plan, gameObject) == True):
			self.hitByEnemy(gameObject)
		else:
			if(self.collision.detectFinish(self.plan, gameObject) == True):
				self.reachFinish()
			else:
				if(gameObject.hasWeapon == True and gameObject.firedWeapon == True):
					self.fireWeapon(gameObject)
					gameObject.firedWeapon = False
				elif(gameObject.hasWeapon == True and gameObject.firedWeapon == False):
					if(isinstance(gameObject, Player) and self.checkBullets() == False):
						gameObject.weapon.fired = False
				self.addToGamePlan(gameObject)
		
	def addToGamePlan(self, gameObject):
		'''
		Add the game object to the game plan.
		:param gameObject: The game object to add to the game plan
		'''
		self.plan[gameObject.pos] = gameObject
				
	def removeObject(self, gameObject):
		'''
		Remove game object from plan if it not a bullet.
		:param gameObject: The game object to remove.
		'''
		if(not isinstance(self.plan[gameObject.pos], Bullet)):
			self.plan[gameObject.pos] = None

	def setLevel(self, gameObjects):
		'''
		Set the level and save the player life. 
		:param gameObjects: The new level objects.
		'''
		player = None
		for pos in range(0, self.leds):
			if(isinstance(self.plan[pos], Player)):
				player = copy.copy(self.plan[pos])
			self.plan[pos] = None
		for gameObject in gameObjects:
			self.plan[gameObject.pos] = copy.copy(gameObject)
			if(isinstance(self.plan[gameObject.pos], Player) and player != None):
				self.plan[gameObject.pos].life = player.life				
				print self.plan[gameObject.pos].life
				
	def runBulletLogic(self):
		'''
		Run the bullet logic.
		'''
		for pos in range(0, self.leds):
			if(isinstance(self.plan[pos], Bullet)):
				if(self.plan[pos].duration == 0):
					self.plan[pos] = None
				else:
					self.plan[pos].duration -= 1		
		
	def moveObjects(self):
		'''
		Move all game objects. 
		If the game object a Player take the user input else move the game objects as defined in the class. 
		'''
		self.runBulletLogic()
		for gameObject in self.plan:
			if(gameObject != None):
				self.removeObject(gameObject)
				if(isinstance(gameObject, Player)):
					self.controlling.userInput(gameObject)
				else:
					self.controlling.moveObject(gameObject)
				self.runGameLogic(gameObject)

	def nextStep(self):
		'''
		Run the next steps. 
		1. Move all objects. 
		2. Drawing the game plan. 
		'''
		self.moveObjects()
		self.drawing.gamePlan(self.plan)

	def initGamePlan(self):
		'''
		Init the game plan and set the level 0.
		'''
		for _ in range(self.leds):
			self.plan.append(None)
		self.setLevel(self.leveldesign.level[0])
				



