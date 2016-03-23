#!/usr/bin/python
#*-* coding:utf-8 *-*
import copy as cp

licence = """
This program is an Arimaa UI and a simple bot, development version.
Copyright (C) 2012 by Adam Kurkiewicz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import warnings
pieces = "rcdhme"
botName = "thinkBot"
pEn = {}
row = {}

for index, letter in enumerate("abcdefgh"):
	row[letter] = index

for index, letter in enumerate(pieces):
	pEn[letter] = index
	pEn[index] = letter

boardSize = 8

class AbstractPiece:
	def __init__(self):
		raise PieceError("AbstractPiece is an abstract class")
	def getOwner(self):
		raise PieceError("there is no owner to this piece")


class PieceError(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return str(self.message)

class EmptyPiece(AbstractPiece):
	singleton = True
	def __init__(self):
		if EmptyPiece.singleton == True:
			EmptyPiece.singleton = False
		else:
			raise PieceError("there can be only one EmptyPiece")
	def getStrength(self):
		return -1 # used by implementation
	def isEmpty():
		return True
	def __str__(self):
		return " "		
	def __repr__(self):
		return " "
	def __int__(self):
		return -1

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
	def remeberPosition(self, position):
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

empty = EmptyPiece()

class Field:
	def __init__(self):
		self.piece = empty
		self.history = []
		self.isblackHole = False
	def getPiece(self):
		return self.piece
	def setPiece(self, piece):
		self.piece = piece
	def updateHistory(piece):
		pass		
		
class Board:
	def __init__(self):
		self.round = 0
		self.byStrength = [{},{}]
		self.board = [[Field() for i in range(boardSize)] for i in range(boardSize)]
		self.history = []
	def setup(self, whitePieces, blackPieces):
		for rowNumber, row in enumerate(whitePieces):
			for columnNumber, piece in enumerate(row):
				dicKey = piece.getStrength()
				self.byStrength[piece.getOwner()].setdefault(dicKey, [])
				self.byStrength[piece.getOwner()][dicKey].append([rowNumber, columnNumber])
				self.board[rowNumber][columnNumber].setPiece(piece)
		for rowNumber, row in enumerate(blackPieces):
			for columnNumber, piece in enumerate(row):
				inverseRow = boardSize - rowNumber - 1
				dicKey = piece.getStrength()
				self.byStrength[piece.getOwner()].setdefault(dicKey, [])
				self.byStrength[piece.getOwner()][dicKey].append([inverseRow, columnNumber])
				self.board[inverseRow][columnNumber].setPiece(piece)
	def getField(self, coordinates):
		return self.board[coordinates[1]][coordinates[0]]
	def roundUp(self):
		self.round += 1
		for colour in byStrength:
			for fieldWithPiece in colour:
				fieldWithPiece.getPiece().historify()
	def firstRoundSwap(self, coordinates, colour):
		if self.round != 0:
			warnings.warn("are you sure that swapping elements after 0th round is ok?")
		fieldA = self.getField(coordinates[0])
		fieldB = self.getField(coordinates[1])

		if fieldA.getPiece().getOwner() != colour or fieldB.getPiece().getOwner() != colour:
			raise PieceError("your own pieces, no empty fields, be reasonable")
		swapField = fieldA.getPiece()
		fieldA.setPiece(fieldB.getPiece())
		fieldB.setPiece(swapField)
	def strBlack(self):
		empty = "\n"
		for rowIndex, rows in enumerate(self.board):
			empty += str(rowIndex)+" "
			for element in rows:
				empty += str(element.getPiece())
				empty += " "
			empty += "\n"
		empty += " "
		for i in "abcdefgh":
			empty += " " + str(i)
		return empty
	def strWhite(self):
		empty = "\n"
		for rowIndex, rows in enumerate(self.board[::-1]):
			empty += str(boardSize - rowIndex - 1)+" "
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
			return self.strWhite()
		else:
			return self.strBlack()

class UserInputError(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return str(self.message)


class UserGame:
	def __init__(self):
		self.board = Board()
	def generatePieces(self, owner):
		pieces = [[Piece("r", owner) for i in range(boardSize)],[Piece(pieceName, owner) for pieceName in "cdhmehdc"]]
		return pieces
	def decode(self, letterNumber):
		toDecode = str(letterNumber).split()
		coordinates = [[k for k in i] for i in toDecode]
		for i in coordinates:
			i[0] = row[i[0]]
			i[1] = int(i[1])
		return coordinates
		#raise UserInputError("litera-cyfra-spacja-litera-cyfra")
			
	def uIFirstRound(self):
		# [0 mianownik kto co, 1 dopełniacz kogo czego, 2 celownik komu czemu, 3 biernik kogo co, 4 narzędnik z kim z czym, 5 miejscownik o kim o czym, 6 wołacz o]
		playerColour = [[["biały", "białego", "białemu", "białego", "białym", "białym", "biały"],["białe", "białych", "białym", "białe", "białymi", "białych", "białe"]],[["czarny", "czarnego", "czarnemu", "czarnego", "czarnym", "czarnym", "czarny"],["czarne", "czarnych", "czarnym", "czarne", "czarnymi", "czarnych", "czarne"]]]
		playerColourEnglish = ["white", "black"] 
		example = ["a0 e1","a7 e6"]
		for colour, text in enumerate(playerColour):
			firstRoundInfo = "Witaj w Arimaa UI by picrin. Rozgrywasz " + text[1][4] + ". Pierwsza faza rozgrywki. Możesz zamienić dowolne dwie figury " + text[0][1] + " koloru. Oddzielając spacją wpisz dwukrotnie literę kolumny i numer rzędu, np. " + example[colour] + ". Aby zakończyć rozstawianie wpisz x. Możesz w dowolnym momencie wyświetlić pomococ wpisując h. Żeby zapoznać się ze szczegółami licencji wciśnij l. Good Loch!\n"
			print firstRoundInfo
			print self.board
			command = raw_input(botName+": ")
			while command != "x":
				if command == "l":
					print licence
				else:
					try:
						toSwap = self.decode(command)
						self.board.firstRoundSwap(toSwap, colour)
						print self.board
					except Exception as exc:
						print str(exc)
				command = raw_input(botName+": ")
		
			
	def play(self):
		self.board.setup(self.generatePieces(0),self.generatePieces(1))
		self.uIFirstRound()
casualFame = UserGame()
casualFame.play()
