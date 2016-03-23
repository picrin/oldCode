import string
import os
# read text from file
def read_from_file(a_file):
    the_file = open(a_file,"r")
    the_file = the_file.read()
    listWords = the_file.split("\n")
    return [word for line in listWords for word in line.split(" ") ]
#print read_from_file("abstract.txt")


def get_new_name(filename, align, width):
    name = filename + "-" + "aligned" + "_" + align + "-" + width + ".txt"
    return name

def just(stringa,command,width):
    print stringa, "*"*9
    if command == "left":
        stringa = string.ljust(stringa,width)
    if command == "right":
        stringa = string.rjust(stringa,width)
    if command == "center":
        stringa = string.center(stringa,width)
    if command == "justified":
        listOFstringa = stringa.split(" ")
        i = width - len(stringa)
        freeSpace = len(listOFstringa) - 1
        deleno = i/freeSpace
        i = i - (deleno*freeSpace)
        for word in listOFstringa:
            if word!=listOFstringa[-1] and word!=" ":
                index = listOFstringa.index(word)
                listOFstringa = listOFstringa[0:index+1] + [" "] + listOFstringa[index+1:]
        for word in listOFstringa:
            if word!=listOFstringa[-1] and word!=" ":
                index = listOFstringa.index(word)
                listOFstringa = listOFstringa[0:index+1] + [" "]*deleno + listOFstringa[index+1:]
                if i!=0:
                    listOFstringa = listOFstringa[0:index+1] + [" "] + listOFstringa[index+1:]
                    i = i - 1       
        stringa = "".join(listOFstringa)
    return stringa

def justify(listWords,width):
#    print listWords
    myString = ""
    a = ""
    for word in listWords:
       # print "len a + len words before:", len(word) + len(a)
        if len(word) + len(a) + 1<=width:
            a = a + " " + word
           # print "a1: ", a, "len a: ", len(a), "len word:", len(word)
        if len(word) + len(a)>width:
            a = just(a,"right",25)
            myString = myString + a + "\n"
         #   print "a2:", a
            a = ""
          #  print "a3: ", a
            if word not in myString:
            #    print "word not in the string"
                a = a + " " + word
    return myString
print justify(read_from_file("abstract.txt"),25)









        

        
  
