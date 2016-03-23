#!/usr/bin/python
# -*- coding:utf-8 -*-
import traceback, pickle, sys
from defaults import *

f = open(sys.argv[1], "r")
lotsOfWords = f.readlines()

f.close()

occurrence = {}
for i in uniAlphabet:
	occurrence[i] = {}
	for j in uniAlphabet:
		occurrence[i][j] = 0
firstOne = {}
for i in uniAlphabet:
	firstOne[i] = 0

for i in lotsOfWords:
	firstOne[uni(i)[:1]] += 1


def wordStatistic(uniWord):
	for char, nextChar in zip(uniWord[:-1], uniWord[1:]):
		occurrence[char][nextChar] += 1

warnings = 0
for word in lotsOfWords:
	try:
		wordStatistic(uni(word[:-1]))
	except KeyError:
		warnings += 1
		print "Warning", warnings, " your dictionary contains some unexpected ", traceback.format_exc()[-15:-1]
pickleTo = open(sys.argv[1]+"_nextOne","w")
pickle.dump(occurrence, pickleTo)
pickleTo.close()

firstOneTo = open(sys.argv[1]+"_firsts","w")
pickle.dump(firstOne, firstOneTo)
firstOneTo.close()
