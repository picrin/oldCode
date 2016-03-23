#!/usr/bin/python
import random
import math

domainHisto = [0, 7, 11, 13, 15, 12, 11, 8, 5, 2]
exonHisto = [0, 0, 0, 0, 0, 0, 1, 1, 3, 5, 7, 14, 32, 75, 198, 214, 225, 315, +

intronHisto = exonHisto
translocation = exonHisto

def gaussianHisto(width=100, avg=600, repetitions = 10**6):
	distro = []
	for i in xrange(repetitions):
		randomLength = abs(int(math.floor(random.gauss(avg,width))))
		if randomLength >= len(distro):
			distro += [0]*(randomLength - len(distro) + 1)
		distro[randomLength] += 1
	return distro
	
#print gaussianHisto()

class RandHisto(object):
	def __init__(self, histo):
		self.histo = histo
		self.number = None
		#make cummulative
		cumm = [0]*len(self.histo)
		sum = 0
		for i, v in enumerate(self.histo):
			sum += v
			cumm[i] = sum
			self.cumm = cumm
	def getRandom(self):
		#get random from distribution
		threshold = random.randint(0, self.cumm[-1]-1)
		for i, v in enumerate(self.cumm):
			if threshold < v:
				return i

#tusia = RandHisto(exonHisto)
#print [tusia.getRandom() for i in range(10000)]

class DNA(object):
	def __init__(self, numberOfProteins, domainHisto, exonHisto, intronHisto):
		self.strand = self.makeStrand(numberOfProteins, domainHisto, exonHisto, intronHisto)
		self.summedGenes = [sum(i) for i in self.strand]
		self.DNAlength = sum(self.summedGenes)
	#	print self.strand
	#	print self.summedGenes
	#	print self.DNAlength
	def _restrictSummedGenes(self, sizeOfRestriction):
		reversedSummedGenes = self.summedGenes[::-1]		
		toBeCut = sizeOfRestriction
		for  index, reversed_gene in enumerate(reversedSummedGenes):
			if toBeCut < reversed_gene:
				reversedSummedGenes[index] -= toBeCut
				break
			else:
				toBeCut -= reversed_gene
				reversedSummedGenes[index] = 0
		return reversedSummedGenes[::-1]		
	def makeStrand(self, numberOfProteins, domainHisto, exonHisto, intronHisto):
		randDomainHisto = RandHisto(domainHisto)
		randExonHisto = RandHisto(exonHisto)
		randIntronHisto = RandHisto(intronHisto)
		strand = []
		for i in range(numberOfProteins):
			protein = []
			noDomains = randDomainHisto.getRandom()
			for i in range(noDomains):	
				protein += [randExonHisto.getRandom()]
				protein += [randIntronHisto.getRandom()]
			strand += [protein]
		return strand
	def geneSplit(self, geneNumber, domainNumber, exactPoint, length, upperCutInherited = []):
		try:
			chosenGeneStrand = self.strand[geneNumber]
		except IndexError:
			exit("o ja pierdole")
		chosenDomainLength = self.strand[geneNumber][domainNumber]
		lower = chosenGeneStrand[:domainNumber] + [exactPoint]
		upper = [chosenDomainLength - exactPoint] + chosenGeneStrand[domainNumber + 1:]
#		if domainNumber%2 == False:
#			upper = [0] + upper
#			lower = lower + [0]
		sumUpper = sum(upper)
		if length <= sumUpper:
			index = 0
			upperCut = upperCutInherited
			upperLeft = []
			lengthDown = length
			while lengthDown > upper[index] and index < len(upper):
				lengthDown -= upper[index]
				upperCut += [upper[index]]
				index += 1
			upperCut += [lengthDown]
			while index < len(upper):
				upperLeft += [upper[index]]
				index += 1
			upperLeft[0] -= lengthDown
			return lower, upperCut, upperLeft
#		self.strand[geneNumber] = lower
		else:
			call = self.geneSplit(geneNumber + 1, 0, 0, length - sumUpper, upper)
			
			return lower, call[1], call[2]
		
	def chromosomalDeletion(self):
		randHistoDeletion = RandHisto(translocation)
		deletionLength = randHistoDeletion.getRandom()
#		print deletionLength
		restrictedSummed = self._restrictSummedGenes(deletionLength)
		randHistoSummedGenes = RandHisto(restrictedSummed)
		chosenGene = randHistoSummedGenes.getRandom()
		randHistoChosenGene = RandHisto(self.strand[chosenGene])
		chosenDomain = randHistoChosenGene.getRandom()
#		print restrictedSummed
#		print self.summedGenes
#		print self.strand
		chosenGeneStrand = self.strand[chosenGene]
		chosenDomainLength = self.strand[chosenGene][chosenDomain]
		exactPoint = random.randint(0, chosenDomainLength - 1)
		result = self.geneSplit(chosenGene, chosenDomain, exactPoint, 500)
		print sum(result[1])
#		print chosenDomain, chosenDomainLength
		print "strand: ", self.strand
		print "[a], [b], exactPoint", chosenGene, chosenDomain, exactPoint
		print chosenGeneStrand, chosenDomainLength
		print "result!", result
#		print "suma1nd", sum(result[1]) 
		print self.strand[chosenGene]
		self.strand[chosenGene]
		print chosenGene, chosenDomain, chosenDomainLength
		
dupa = DNA(10, domainHisto, exonHisto, intronHisto)
dupa.chromosomalDeletion()

