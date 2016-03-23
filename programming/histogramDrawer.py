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

