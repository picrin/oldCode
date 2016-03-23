#!/usr/bin/python
# *-* coding:utf-8 *-*
import pickle, sys, copy, defaults
f = open(sys.argv[1], "r")

occurrence = pickle.load(f)

partialFlatten = {}

frequency = {}

frequencyOverall = 0

for firstLetter in occurrence:
	cumulative = 0
	for secondLetter in uniAlphabet:
		occurred = occurrence[firstLetter][secondLetter]
		cumulative = cumulative + occurred
		partialFlatten.setdefault(firstLetter,[]).append([cumulative,secondLetter])
	frequency[firstLetter] = cumulative

for freq in frequency:
	frequencyOverall += frequency[freq]

print partialFlatten
print
print frequency
print
print frequencyOverall



reverse = copy.copy(occurrence)

