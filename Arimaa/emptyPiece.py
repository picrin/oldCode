from abstractPiece import *
from pieceError import *
class EmptyPiece(AbstractPiece):
	singleton = True
	def __init__(self):
		if EmptyPiece.singleton == True:
			EmptyPiece.singleton = False
		else:
			raise PieceError("there can be only one EmptyPiece")
	def getStrength(self):
		return -1 # used by implementation
	def getOwner(self):
		return 2 # to distinguish from white 0 and black 1
	def isEmpty():
		return True
	def __str__(self):
		return " "		
	def __repr__(self):
		return " "
	def __int__(self):
		return -1


class BlackHolePiece(AbstractPiece):
	singleton = True
	def __init__(self):
		if BlackHolePiece.singleton == True:
			BlackHolePiece.singleton = False
		else:
			raise PieceError("there can be only one BlackHolePiece")
	def getStrength(self):
		return -2
	def getOwner(self):
		return 2 # to distinguish from white 0 and black 1
	def __str__(self):
		return "X"
	def __repr__(self):
		return "X"
	def __int__(self):
		return -2

