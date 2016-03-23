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

