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

