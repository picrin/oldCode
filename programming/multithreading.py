#!/usr/bin/python
import thread
import time
def computeHard():
	u = range(2**24)
	thread.exit()

try:
	thread.start_new(computeHard,())
	time.sleep(2)
except SystemExit:
		print "tusia"



