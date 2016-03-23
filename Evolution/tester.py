import numpy

def solutionPruning(twoSolutions): #return smallest positive or None
	"""
	@dev-only -- return least real positive from a sequence of two complex numbers (or one).
	"""
	try:
		if twoSolutions[0].imag == 0:
			if twoSolutions[0].real > 0:
				if twoSolutions[0] < twoSolutions[1]:
					return twoSolutions[0].real
				else:
					return twoSolutions[1].real
			elif twoSolutions[1].real > 0:
				if twoSolutions[1] < twoSolutions[0]:
					return twoSolutions[1].real
				else:
					return twoSolutions[0].real
		else:
			return None
	except IndexError:
		print "Unusual stuff going on with solution pruning. Leading coefficient == 0?"
		return twoSolutions[0].real

interesting = numpy.real_if_close(numpy.roots([0.1, -40, 3]))
print interesting
print solutionPruning(interesting)

