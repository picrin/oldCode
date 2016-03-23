#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np, string, os, sys

print sys.argv



#sorting of a unicode word, numpy array returned
def sortUTF8(word):
	return string.join(np.sort([utfchar for utfchar in unicode(word,"utf-8")]),"")

#allwords = ["zażółcić","żłzaócić", "ćżłzaóci", "strzepnąć","masło","słoma","myśleć","ślymeć"]

print "otwieranie pliku do odczytu"
polishWords = open(sys.argv[1], 'r')
allwords = polishWords.readlines()
polishWords.close()



print "tworzenie tablicy haszujacej"
przestawiaki = {}
for index, word in enumerate(allwords):
	sortedWord = sortUTF8(word)
	przestawiaki[sortedWord] = przestawiaki.get(sortedWord, [])
	przestawiaki[sortedWord].append(index)



print "tworzenie pliku do zapisu"
grouped = open('./groupedNouns.txt', 'w')
for key in przestawiaki:
	if len(przestawiaki[key])>1:
		grouped.write(string.join([allwords[index] for index in przestawiaki[key]], "\t"))
os.system("gedit ./groupedNouns.txt")

