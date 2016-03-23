import sys, os, tokenize

def countIfs(filename):
	tokens = tokenize.generate_tokens(open(filename).readline)
	return len([token for token in tokens if token[0] == 1 and token[1] == 'if'])

message = "Pass a path to a directory containing some .py files. E.g. countifs.py path/to/directory"

#fail because of empty argument list
try:
	directory = sys.argv[1]
except IndexError:
	print "No arguments passed. Will exit now.", message
	exit(1)

#fail because of non-existing directory
try:
	filenames = [filename for filename in os.listdir(directory) if filename[-3:] == ".py"]
except IOError:
	print direcotry, "is not a directory. Will exit now.", message
	exit(1)

#fail because of no python files
if not filenames:
	print directory, "does not contain any .py files. Will exit now.", message
	exit(1)

howManyIfs = [countIfs(filename) for filename in filenames]

countedFiles = zip(howManyIfs, filenames)

countedFiles.sort()

for aTuple in countedFiles[::-1]:
	print aTuple[1], "contains", aTuple[0], "ifs"
exit(0)
