structuredDatabase = {"IM":{},"BS":{},"BA":{},"CR":{},"FS":{}}
def loading():
	#reset database
	global structuredDatabase
	structuredDatabase = {"IM":{},"BS":{},"BA":{},"CR":{},"FS":{}}
	path = raw_input("Give the file path: ")
	try:
		fileToLoad = open(path, "r")
	except IOError:
		print "No such file.",
		loading()
	lines = fileToLoad.readlines()
	fileToLoad.close()
	rawDatabase = []
	semiStructuredDatabase = {"IM":[],"BS":[],"BA":[],"CR":[],"FS":[]}
	for i in lines:
		rawDatabase.append(i[:-1].split(":"))
	for i in rawDatabase:
		semiStructuredDatabase[i[0]] += [i[1:]]
	for dic in semiStructuredDatabase:
		for lista in semiStructuredDatabase[dic]:
			structuredDatabase[dic].setdefault(lista[1],[])
			structuredDatabase[dic][lista[1]].append([lista[2],lista[3],lista[0]])
			structuredDatabase[dic][lista[1]].sort()
	print structuredDatabase
	raw_input("Loaded OK, press enter to go back to menu.")
def saving():
	lines = ""
	for event in structuredDatabase:
		for age in structuredDatabase[event]:
			for record in structuredDatabase[event][age]:
				lines += str(event)+":"
				lines += str(record[2])+":"
				lines += str(age)+":"
				lines += str(record[0])+":"
				lines += str(record[1])
				lines += "\n"
	path = raw_input("give the file path: ")
	plik = open(path, "w")
	plik.write(lines)
def printing():
	for event in structuredDatabase:
		for age in structuredDatabase[event]:
			print "Time\tEvent\tGender\tAge\tName"		
			for record in structuredDatabase[event][age]:
				print str(record[0])+"\t"+str(event)+"\t"+str(record[2])+"\t"+str(age)+"\t"+str(record[1])
	raw_input("Press enter to go back to menu.")
def checking():
	entry = raw_input("Give the new entry, in the format event:sex:age:time:name surname and press enter. Example: IM:F:6:58.2:Kirsty Laing: ")
	lines = entry.split(":")
	try:
		structuredDatabase[lines[0]]
	except KeyError, IndexError:
		print "Possible events dissiplines are: Individual Medley (IM) Breast stroke (BS) Backstroke (BA) Crawl (CR) and Freestyle (FS). Remember to use the right format, i.e. <CR:M:21:15.4:Adam Kurkiewicz>. Please try again. "
		checking()
	structuredDatabase[lines[0]].setdefault(lines[2],[])	
	recordList = structuredDatabase[lines[0]][lines[2]]
	for record in recordList:
		if record[1] == lines[4]:
			if record[0] > lines[3]:
				record[0] = lines[3]
				print "Better time "+str(lines[3])+" recorded for "+str(lines[4])+". "
			else:
				print "This is not the personal best. Current best time is " + str(record[0]) + ". "
			recordList.sort()
			raw_input("Done, press enter to go back to menu. ")
			return
	recordList.append([lines[3],lines[4],lines[1]])
	recordList.sort()
	raw_input("New entry recorded, press enter to go back to menu. ")
	return
def quitting():
	raise SystemExit
functions = {"l":loading, "s":saving, "p":printing, "c":checking, "q":quitting}
def functionChoice():
	function = raw_input("Enter your choice: ")
	try:
		functions[function]()
	except KeyError:
		print "I didn't understand, check your spelling or try other option."
		functionChoice()
def main():
	for i in ["Choose from the following options:",
"l:\tload results from a file",
"s:\tsave results to a file",
"p:\tprint results",
"c:\tcheck and add a new personal best",
"q:\tquit"]:
		print i
	functionChoice()
	main()
main()
