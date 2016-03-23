class AbstractPiece:
	def __init__(self):
		raise PieceError("AbstractPiece is an abstract class")
	def getOwner(self):
		raise PieceError("there is no owner to this piece")

