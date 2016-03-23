from piece import *
from globalVars import *
from field import *
import warnings
#[white{strengths:positions},black{strengths:positions}]
#[{0:[],1:[]...},{0:[],...}]
class Board:
	def __init__(self):
		self.round = 0
		self.query = Queries()
		self.board = [[Field() for j in range(boardSize)] for i in range(boardSize)]
		self.extendedBoard = self.extend()
		for i in blackHoles: #black holes:
			self.getField(i).blackHolise()
		self.history = []
	def extend(self):
		newList = []
		newList.append([Field()] + self.board[0] + [Field()])
		for row in self.board:
			newRow = [row[0]] + row + [row[boardSize - 1]]
			newList.append(newRow )
		newList.append([Field()] + self.board[boardSize - 1] + [Field()])
		return newList		
	def setup(self, whitePieces, blackPieces):
		for rowNumber, row in enumerate(whitePieces):
			for columnNumber, piece in enumerate(row):
				self.query.updatePosition(piece, [rowNumber, columnNumber])
				self.board[rowNumber][columnNumber].setPiece(piece)
		for rowNumber, row in enumerate(blackPieces):
			for columnNumber, piece in enumerate(row):
				self.query.updatePosition(piece, [rowNumber, columnNumber])
				self.board[boardSize - 1 - rowNumber][columnNumber].setPiece(piece)
		self.query.makePlayable()
	def getExtendedField(self, coordinates):
		return self.extendedBoard[coordinates[0] + 1][coordinates[1] + 1]
	def getField(self, coordinates):
		return self.board[coordinates[0]][coordinates[1]]
	def roundUp(self):
		self.round += 1
		for piece in self.query.position:
			position = self.query.getPosition(piece)			
			field = self.getField(position)
			piece = field.getPiece()
			field.historify()
			piece.historify(piece)
	def movePiece(colour, position):
		pass
	def setField(self, coordinates, piece):
		field = self.getField(coordinates)
		self.query.updatePosition(piece, coordinates)
		field.setPiece(piece)
	def swap(self, coordinatesPair):
		fieldA = self.getField(coordinatesPair[0])
		fieldB = self.getField(coordinatesPair[1])
		swapField = fieldA.getPiece()
		self.setField(coordinatesPair[0],fieldB.getPiece())
		self.setField(coordinatesPair[1],swapField)
	def firstRoundSwap(self, coordinates, colour):
		if self.round >= 1:
			warnings.warn("are you sure that swapping elements after 1st round is ok?")
		fieldA = self.getField(coordinates[0])
		fieldB = self.getField(coordinates[1])
		if fieldA.getPiece().getOwner() != colour or fieldB.getPiece().getOwner() != colour:
			raise PieceError("your own pieces, no empty fields, be reasonable")
		self.swap(coordinates)
	def blackOrder(self, rowIndex):
		return rowIndex
	def whiteOrder(self, rowIndex):
		return boardSize - rowIndex - 1
	def blackWhiteString(self, board, orderMethod):
		empty = ""
		for rowIndex, rows in enumerate(board):
			empty += str(orderMethod(rowIndex))+" "
			for element in rows:
				empty += str(element.getPiece())
				empty += " "
			empty += "\n"
		empty += " "
		for i in "abcdefgh":
			empty += " " + str(i)
		return empty
	def __str__(self):
		if self.round%2 == 0:
			return self.blackWhiteString(self.board[::-1], self.whiteOrder)
		else:
			return self.blackWhiteString(self.board, self.blackOrder)
