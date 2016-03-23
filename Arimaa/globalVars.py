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
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from emptyPiece import *
pieces = "rcdhme"
botName = "botThinka"
uiName = "thUIa"
pEn = {}
row = {}
empty = object
blackHolePiece = object
boardSize = 8
blackHoles = [[2,2],[2,5],[5,5],[5,2]]
class globInit:
	once = True
	def __init__(self):
		if globInit.once == True:
			globInit.once = False
			global empty, blackHolePiece
			empty = EmptyPiece()
			blackHolePiece = BlackHolePiece()
			for index, letter in enumerate("abcdefgh"):
				row[letter] = index
			for index, letter in enumerate(pieces):
				pEn[letter] = index
				pEn[index] = letter
globInit()

class Queries:
	def __init__(self):
		self.position = [{},{},{}]
		self.playable = {}
	def updatePosition(self, piece, position):
		self.position[piece.getOwner()][piece] = position
	def getPosition(self, piece):
		return self.position[piece.getOwner()][piece]
	def makePlayable(self):
		self.playable.update(self.position[0])
		self.playable.update(self.position[1])
	def __str__(self):
		return str(self.position)

