#!/usr/bin/python
# *-* coding:utf-8 *-*
import pickle, sys, copy, random
from defaults import *


firstOnes = open(sys.argv[1], "r")
firstChars = pickle.load(firstOnes)
firstOnes.close()

nextOnes = open(sys.argv[2], "r")
occurrence = pickle.load(nextOnes)
nextOnes.close()

wordsToProcess = open(sys.argv[3], "r")
wordsToProcess = wordsToProcess.readlines()

partialFlatten = {}
frequency = {}
for firstLetter in occurrence:
	cumulative = 0
	for secondLetter in uniAlphabet:
		occurred = occurrence[firstLetter][secondLetter]
		cumulative = cumulative + occurred
		partialFlatten.setdefault(firstLetter,[]).append([cumulative,secondLetter])
	frequency[firstLetter] = cumulative

#frequencyOverall = 0
#for freq in frequency:
#	frequencyOverall += frequency[freq]

def generateNext(a):
	cumulativeThreshold = random.randint(0,frequency[a])
	for i in partialFlatten[a]:
		if cumulativeThreshold <= i[0]:
			return i[1]
flatFirsts = []
cumulative = 0
for i in uniAlphabet:
	cumulative += firstChars[i]
	flatFirsts.append([cumulative, i])

def generateFirst():
	cumulativeThreshold = random.randint(0,flatFirsts[-1][0])
	for i in flatFirsts:
		if cumulativeThreshold <= i[0]:
			return i[1]

kwadrat = []
def generateFirstRow(myLetter, length):
	kwadrat.append([])
	myLetterPlace = random.randint(0, length-1)
	for i in range(length):
		if i == myLetterPlace:
			kwadrat[-1].append(myLetter)
			print myLetter,
		else:
			letter = generateFirst()
			kwadrat[-1].append(letter)
			print letter,
	print
	return myLetterPlace

def nextPlace(placeBefore, length):
	if placeBefore == 0:
		newLetterPlace = random.randint(0,1)
	elif placeBefore == length-1:
		newLetterPlace = random.randint(length-2,length-1)
	else:
		newLetterPlace = random.randint(placeBefore-1,placeBefore+1)
	return newLetterPlace

def generateNextRow(placeBefore, nextLetter, length):
	kwadrat.append([])
	newLetterPlace = nextPlace(placeBefore,length)
	for i in range(length):
		if i == newLetterPlace:
			#historia.append([placeBefore, i])			
			kwadrat[-1].append(nextLetter)
			print nextLetter,
		else:
			oldLetterFromPlace = nextPlace(i,length) #as previousPlace
			#historia.append([oldLetterFromPlace, i])
			newLetterLetter = generateNext(kwadrat[-2][oldLetterFromPlace])
			kwadrat[-1].append(newLetterLetter)
			print newLetterLetter,
	print
	return newLetterPlace

def generateKwadrat(word, width):
	kwadrat = []
	place = generateFirstRow(word[0], width)
	for letter in word[1:]:
		place = generateNextRow(place, letter, width)
	return kwadrat

def generateSentence(sentence):
	for letter in sentence.split()[0]:
		print letter
	length = 2
	print
	for word in sentence.split()[1:]:
		generateKwadrat(word, length)
		length += 1
		print

for line in wordsToProcess:
	splitLine = line.split()
	generateKwadrat(uni(splitLine[0]), int(splitLine[1]))
	print
