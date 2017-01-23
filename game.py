from collision import Collision
from leveldesign import Leveldesign
from drawing import Drawing
from controlling import Controlling
from player import Player
import copy

class Game():
	
	def __init__(self, leds):
		self.leds = leds
		self.collision = Collision()
		self.leveldesign = Leveldesign(self.leds)
		self.drawing = Drawing(leds)
		self.controlling = Controlling(leds)
		self.plan = list()
		self.initGamePlan()
		self.level = 0

	def fireWeapon(self, object):
		bullets = object.weapon.getBullets()
		for pos in range(0, object.weapon.size):
			if((object.pos + pos + 1) < self.leds):
				bullets[pos].pos = object.pos + pos + 1
				self.plan[object.pos + pos + 1] = bullets[pos]
			if((object.pos - pos - 1) > 0):
				bullets[pos].pos = object.pos - pos - 1
				self.plan[object.pos - pos - 1] = bullets[pos]

	def lostLife(self, object):
		object.life -= 1
		self.setLevel(self.leveldesign.level[self.level])
		
	def lostGame(self, object):
		self.level = 0
		object.life = object.resetLife
		self.setLevel(self.leveldesign.level[self.level])

	def hitByEnemy(self, object):
		if(isinstance(self.plan[object.pos], Player) and self.plan[object.pos].life < 1):
			self.lostGame(self.plan[object.pos])
		elif(isinstance(object, Player) and object.life < 1):
			self.lostGame(object)
		else:
			if(isinstance(self.plan[object.pos], Player)):
				self.lostLife(self.plan[object.pos])
			elif(isinstance(object, Player)):
				self.lostLife(object)		

	def reachFinish(self, object):
		self.level += 1
		if(self.level >= len(self.leveldesign.level)):
			self.level = 0
		self.setLevel(self.leveldesign.level[self.level])

	def runGameLogic(self, object):
		if(self.collision.detectEnemy(self.plan, object) == True):
			self.hitByEnemy(object)
		else:
			if(self.collision.detectFinish(self.plan, object) == True):
				self.reachFinish(object)
			else:
				if(object.hasWeapon == True and object.firedWeapon == True):
					self.fireWeapon(object)
		self.addToGamePlan(object)
		
	def addToGamePlan(self, object):
		self.plan[object.pos] = object
				
	def removeObject(self, object):
		if(object.hasWeapon == True and object.firedWeapon == True):
			for pos in range(0, object.weapon.size):
				if(object.pos + pos + 1 < self.leds):
					self.plan[object.pos + pos + 1] = None
				if(object.pos - pos - 1 >= 0):
					self.plan[object.pos - pos - 1] = None
			object.firedWeapon = False
		self.plan[object.pos] = None

	def setLevel(self, objects):
		player = None
		for pos in range(self.leds):
			if(isinstance(self.plan[pos], Player)):
				player = copy.copy(self.plan[pos])
			self.plan[pos] = None
		for object in objects:
			self.plan[object.pos] = copy.copy(object)
			if(isinstance(self.plan[object.pos], Player) and player != None):
				self.plan[object.pos].life = player.life
			

	def nextStep(self):
		self.moveObjects()
		self.drawing.gamePlan(self.plan)
		
	def moveObjects(self):
		for object in self.plan:
			if(object != None):
				self.removeObject(object)
				if(isinstance(object, Player)):
					self.controlling.userInput(object)
				else:
					self.controlling.moveObject(object)
				self.runGameLogic(object)

	def initGamePlan(self):
		for pos in range(self.leds):
			self.plan.append(None)
		self.setLevel(self.leveldesign.level[0])
				



