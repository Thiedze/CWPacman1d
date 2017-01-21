from collision import Collision
from leveldesign import Leveldesign
from drawing import Drawing
from controlling import Controlling
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

	def setObject(self, object):
		if(self.collision.detect(self.plan, object.pos) == False):
			if(object.pos >= self.leds - 1):
				self.level += 1
				if(self.level >= len(self.leveldesign.level)):
					self.level = 0
				self.setLevel(self.leveldesign.level[self.level])
			else :
				self.plan[object.pos] = object
				if(object.hasWeapon == True and object.firedWeapon == True):
					bullets = object.weapon.getBullets()
					for pos in range(0, object.weapon.size):
						if((object.pos + pos + 1) < self.leds):
							bullets[pos].pos = object.pos + pos + 1
							self.plan[object.pos + pos + 1] = bullets[pos]
						if((object.pos - pos - 1) > 0):
							bullets[pos].pos = object.pos - pos - 1
							self.plan[object.pos - pos - 1] = bullets[pos]
		else:
			self.level = 0
			self.setLevel(self.leveldesign.level[self.level])

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
		for pos in range(self.leds):
			self.plan[pos] = None
		for object in objects:
			self.plan[object.pos] = copy.copy(object)

	def nextStep(self):
		self.moveObjects()
		self.drawing.gamePlan(self.plan)
		
	def moveObjects(self):
		for object in self.plan:
			if(object != None):
				self.removeObject(object)
				self.controlling.userInput(object)
				self.setObject(object)

	def initGamePlan(self):
		for pos in range(self.leds):
			self.plan.append(None)
		self.setLevel(self.leveldesign.level[0])
				



