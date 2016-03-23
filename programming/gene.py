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

