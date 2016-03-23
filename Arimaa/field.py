from globalVars import *
from pieceError import *
class Field:
	def __init__(self):
		self.movable = True
		self.support = True
		self.piece = empty
		self.history = []
	def getPiece(self):
		return self.piece
	def setPiece(self, piece):
		self.piece = piece
	def blackHolise(self):
		self.piece = blackHolePiece
	def checkMobility(self, surrounding):
		#sc strength and colour		
		self.movable = True
		mySC = [self.getPiece().getStrength(), self.getPiece().getOwner()]
		surroundingSC = [[i.getPiece().getStrength(), i.getPiece.getOwner()] for i in surrounding]
		for sC in surroundingSC:
			if mySC[0] < sC[0] and mySC[1] != sC[1]:
				self.movable = False
				break
		return self.movable
	def checkSupport(self, surrounding):
		self.support = False
		myColour = self.getPiece().getOwner()
		for colour in [i.getPiece().getOwner() for i in surrounding]:
			if myColour == colour:
				self.support = True
				break
		return self.support
	def historify(self):
		self.history.append(self.getPiece())
