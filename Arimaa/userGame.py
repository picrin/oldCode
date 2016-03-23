#*-* coding:utf-8 *-*
from board import *
from userInputError import *
from globalVars import *
class UserGame:
	def __init__(self):
		self.board = Board()
		self.board.setup(self.generatePieces(0),self.generatePieces(1))
	def generatePieces(self, owner):
		pieces = [[Piece("r", owner) for i in range(boardSize)],[Piece(pieceName, owner) for pieceName in "cdhmehdc"]]
		return pieces
	def decode(self, letterNumber):
		toDecode = str(letterNumber).split()
		coordinates = [[k for k in i] for i in toDecode]
		for i in coordinates:
			swap = i[1]			
			i[1] = row[i[0]]
			i[0] = int(swap)
		return coordinates
		#raise UserInputError("litera-cyfra-spacja-litera-cyfra")	
	def uIFirstRound(self):
		# [0 mianownik kto co, 1 dopełniacz kogo czego, 2 celownik komu czemu, 3 biernik kogo co, 4 narzędnik z kim z czym, 5 miejscownik o kim o czym, 6 wołacz o]
		playerColour = [[["biały", "białego", "białemu", "białego", "białym", "białym", "biały"],["białe", "białych", "białym", "białe", "białymi", "białych", "białe"]],[["czarny", "czarnego", "czarnemu", "czarnego", "czarnym", "czarnym", "czarny"],["czarne", "czarnych", "czarnym", "czarne", "czarnymi", "czarnych", "czarne"]]]
		playerColourEnglish = ["white", "black"] 
		example = ["a0 e1","a7 e6"]
		for colour, text in enumerate(playerColour):
			firstRoundInfo = "Witaj w " + uiName + ", UI do gry Arimaa. Rozgrywasz " + text[1][4] + ". Pierwsza faza rozgrywki. Możesz zamienić dowolne dwie figury " + text[0][1] + " koloru. Oddzielając spacją wpisz dwukrotnie literę kolumny i numer rzędu, np. " + example[colour] + ". Aby zakończyć rozstawianie wpisz x. Możesz w dowolnym momencie wyświetlić pomococ wpisując h. Żeby zapoznać się ze szczegółami licencji wciśnij l. Good Loch!\n"
			print firstRoundInfo
			print self.board
			command = raw_input(uiName+": ")
			while command != "x":
				if command == "l":
					print licence
				if command == "h":
					print firstRoundInfo
				else:
					try:
						toSwap = self.decode(command)
						self.board.firstRoundSwap(toSwap, colour)
						print self.board
					except Exception as exc:
						raise exc
						print "Invalid input. Try something like " + example[colour] + "."
				command = raw_input(uiName+": ")
			self.board.roundUp()
	def play(self):
		self.uIFirstRound()
