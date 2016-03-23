from abstractPiece import *
from globalVars import *
class Piece(AbstractPiece):
	def __init__(self, strength, owner):
		self.owner = owner
		self.history = []
		try:
			self.strength = int(strength)
		except ValueError:
			self.strength = int(pEn[strength])
	def getStrength(self):
		return self.strength
	def setStrength(self, strength):
		warnings.warn("changing the piece strength, are you sure?")
		self.strength = self.strength = strength
	def getOwner(self):
		return self.owner
	def historify(self, position):
		self.history.append(position)
	def __str__(self):
		if self.getOwner() == 0:
			return pEn[self.strength].upper()
		if self.getOwner() == 1:
			return pEn[self.strength]
		else:
			return "Dupa Jasia"
	def __repr__(self):
		return pEn[self.strength] + str(self.owner)
	def __int__(self):
		return self.strength


