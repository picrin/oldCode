
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







