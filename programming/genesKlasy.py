#!/usr/bin/python


class DnaPiece(object): # gene
	def __init__(self, material, gene, exon):
		self.material = material
		self.gene = gene # gene has to implement methods logExon(), logOrder()
		self.exon = exon
	def linkLeft(self, dnaPiece):
		self.left = dnaPiece
		dnaPiece.right = self
	def linkRight(self, dnaPiece):
		self.right = dnaPiece
		dnaPiece.left = self
#double-ended queue only for the outermost, i.e. DNA level. Do not assume goLeft or goRight keep you within Gene. Always check self.gene == desired gene instance.
	def goLeft(self):
		return self.left
	def goRight(self):
		return self.right
	def getGene(self):
		return self.gene
	def getMaterial(self):
		return self.material
#	def decrease(self, by):
#		if self.material < by: #<debug> 
#			raise materialError("decreasing by too much") #</debug>
#		self.material -= by
#		return by
	def setMaterial(self, by):
		materialLeft = self.material - by
		self.material = by
		return materialLeft
	def split(self, leftSide):
		if leftSide == 0 and leftSide == self.getMaterial():
			return self
		if leftSide < 0: #<debug>
			raise ValueError("splitting must use non-negative") #</debug>
		self.gene.logOrder(self)
		if self.exon == True:
			self.gene.logExon(self)
		newDnaPiece = DnaPiece(self.setMaterial(leftSide), self.gene, self.exon)
		newDnaPiece.linkLeft(self)
		newDnaPiece.linkRight(self.goRight())
		return newDnaPiece
	def pop(self):
		self.gene.logOrder(self)
		self.goRight().linkLeft(self.goLeft())
		self.goLeft().linkRight(self.goRight())

class HistogramDrawer():
	def __init__(self, histogram):
		self.histogram = histogram
		self.cummulative = self.prepareCummulative()
	def prepareCummulative(self):
		cummulative = histogram
		for i, v in enumerate(self.histogram[1:]):
			cummulative[i] = cummulative[i-1] + v
		return cummulative
	def randomLength(self):
		threshold = random.randint(0, self.cummulative[-1]-1)
		for i, v in enumerate(self.cummulative):
			if threshold < v:
				return i

class DeadEnd(object):
	def __init__(self):
		self.left = self
		self.right = self
	def goFirst(self):
		self.left
	def goLast(self):
		self.right
	def goLeft(self):
		raise IndexError()
	def goRight(self):
		raise IndexError()
	def getGene():
		return None
		
class DnaIterator(object):
	def __init__(self, dnaPiece):
		self.harbour = dnaPiece
		self.poinAt = dnaPiece
		self.counter = 0
	def move(steps):
		if steps < 0:
			while steps != 0:
				self.pointAt = dnaPiece.goLeft()
				steps += 1
				self.counter += 1
		if steps > 0:
			while steps != 0:
				self.pointAt = dnaPiece.goRight()
				steps -= 1
				self.counter -= 1
	def getDna():
		return self.pointAt
	def position():
		return self.counter
	def reset():
		self.pointAt = self.harbour
		self.counter = 0
		
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
		

class Gene(object, dnaIterable):
	def linkPieces(self, dnaPieces):
		super.linkPieces(dnaPieces)
		self.order = True
	def logOrder(self):
		self.order = False
	def logExon(self):
		return self.damage()
	def order(self):
		self.dnaPiece = []
		index = 0
		while self.getFirstIterator().getDna().getGene() == self:
			self.dnaPiece[index] = self.getFirstIterator().getDna()
	def linkRight(self, dnaPiece):
		dnaPiece.left = self
		self[-1].right = dnaPiece
	def linkLeft(self, dnaPiece):
		dnaPiece.right = self
		self[0].left = dnaPiece
	def __getitem__(self, index):
		if index == 0:
			return self.deadEnd.goFirst()
		elif index == -1:
			return self.deadEnd.goLast()
		else:  
			raise Exception("DnaStrand is not fully iterable, try 0 or -1 or acces through genes")

class DnaStrand(object, dnaIterable):
	def __init__(self, genes):
		super.__init__(genes)
		self.genes = super.dnaPieces
