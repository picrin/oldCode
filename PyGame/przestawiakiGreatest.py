#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np, string, os, sys, math, itertools

if sys.argv[1] == "help" or sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "-h" or sys.argv[1] == "--h":
	print "============================PRZESTAWIAKI============================\nThe use is: ./przestawiaki.py <name of a text file with huge list of words in a given language>"
	quit()

def uni(string):
	return unicode(string, "utf-8")

#sorting of a unicode word, numpy array returned
def sortUTF8(word):
	return string.join(np.sort([utfchar for utfchar in uni(word)]),"")

def closestDistance(indexedLetter, word):
	distance = sys.maxint	
	for index, letter in enumerate(word):
		#print index, letter
		if letter == indexedLetter[1]:
			tempDistance = abs(indexedLetter[0] - index)
			if(tempDistance < distance):
				distance = tempDistance
	return distance

#assume the same letters
def dissimilarity(wordPair):
	suma = 0	
	for indexedLetter in enumerate(wordPair[0]):
		suma += closestDistance(indexedLetter, wordPair[1])
	return suma

def listDissimilarity(lista):
	highest = 0
	for wordPair in list(itertools.combinations(lista, 2)):
		localDissimilarity = dissimilarity(wordPair)
		if highest < localDissimilarity:
			highest = localDissimilarity
	return highest

print "otwieranie pliku do odczytu"
polishWords = open(sys.argv[1], 'r')
allwords = polishWords.readlines()
polishWords.close()

print "tworzenie tablicy haszującej"
przestawiaki = {}
for index, word in enumerate(allwords):
	sortedWord = sortUTF8(word)
	przestawiaki[sortedWord] = przestawiaki.get(sortedWord, [])
	przestawiaki[sortedWord].append(index)

print "usuwanie nieinteresujących elementów"
for key, item in przestawiaki.items():
	if len(item)==1:
		del przestawiaki[key]

print "ocena elementów"
for key in przestawiaki:
	przestawiaki[key] = [len(przestawiaki[key]),przestawiaki[key]]

print "sortowanie chyba timsortem"
posortowane = [przestawiaki[keys] for keys in przestawiaki]
posortowane.sort()

print "zapisywanie do pliku"
groupedName = sys.argv[1]+"_przestawiakiGreatest.txt"
grouped = open(groupedName, 'w')

for indeces in posortowane:
	grouped.write(string.join([allwords[index] for index in indeces[1]], "\t"))

grouped.close()
os.system("gedit "+groupedName)

