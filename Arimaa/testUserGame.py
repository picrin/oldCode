from userGame import *
class TestUserGame(UserGame):
	def __init__(self):
		self.board = Board()
		self.board.setup(self.generatePieces(0), self.generatePieces(1))
	def testExtendedBoard(self):
		for row in self.board.extendedBoard:
			for field in row:
				print field.getPiece(),
			print
	def swapTesting(self):
		while True:
			toDecode = raw_input("command: ")
			if toDecode == "test":
				self.testAllSurrounding()
			else:
				self.board.swap(self.decode(toDecode))
				print self.board
	def testAllSurrounding(self):
		print self.board.query.playable
		for piece in self.board.query.playable:
			position = self.board.query.getPosition(piece)
			indirectSurrounding = [[-1,1],[1,-1],[1,1],[-1,-1]]
			surrounding = [[position[0] + i, position[1] + j] for i,j in indirectSurrounding]
			if self.board.getField(position).checkSupport([self.board.getExtendedField(i) for i in surrounding]) == False:
				print "Piece:", self.board.getField(position).getPiece(), position
#set of pieces with surrounding
#set of frozen pieces

