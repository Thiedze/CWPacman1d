from object import Object
from weapon import Weapon

class Player(Object):

	def __init__(self):
		Object.__init__(self)
		self.pos = 1
		self.direction = 1
		self.color = [255,0,0]
		self.hasWeapon = True
		self.weapon = Weapon()


