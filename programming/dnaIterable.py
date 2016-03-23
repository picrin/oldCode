		
class dnaIterable(object):
	# dnaPieces must implement linkLeft, linkRight
	def __init__(self, dnaPieces):
		self.deadEnd = deadEnd()
		self.dnaPieces = self.linkPieces(dnaPieces)
		self.firstIterator = DnaIterator(self[0])
		self.lastIterator = DnaIterator(self[-1])
	def linkPieces(self, dnaPieces):
		dnaPieces[0].linkLeft(self.deadEnd)
		dnaPieces[-1].linkRight(self.deadEnd)
		for index, piece in enumerate(dnaPieces[1:-1]):
			piece.linkLeft(dnaPieces[index-1])
			piece.linkRight(dnaPieces[index+1])
		return dnaPieces
	def getFirstIterator():
		return self.firstIterator
	def getLastIterator():
		return self.lastIterator
	def getDeadEnd():
		return self.deadEnd
	def __getitem__(self, index):
		if index == 0:
			return self.deadEnd.goFirst()
		elif index == -1:
			return self.deadEnd.goLast()
		else:  
			raise Exception("DnaIterable otherwise then 0 or -1 is iterable through iterators. Try instance.getFirstIterator()")

