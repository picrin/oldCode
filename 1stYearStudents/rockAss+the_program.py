import string
import gui.py
def read_from_file(a_file):
    the_file = open(a_file,"r")
    the_file = the_file.read()
    list_words = the_file.split("\n")
    return [word for line in list_words for word in line.split(" ")]

class Szpalta:
    def __init__(self, width):
        self.width = width
        self.current_line = []
        self.lines = []
        self.counter = 0
        self.word_counter = 0
    def put(self, word):
        word_len = len(word) + 1
        new_counter = self.counter + word_len
        if new_counter > self.width + 1:
            self.lines.append(self.current_line)
            self.current_line.append(self.counter - 1)
            self.current_line = []
            self.current_line.append(word)
            self.counter = word_len
        else:
            self.counter = new_counter
            self.current_line.append(word)
    def getLines(self):
        self.lines.append(self.current_line)
        return self.lines
        
width = input("width:")
command = raw_input("left, right, centered or justified??!")
lista = read_from_file("abstract.txt")[::-1]
szpalta = Szpalta(width)
while lista:
    szpalta.put(lista.pop())
result = szpalta.getLines()

def just(nested_list,command,width):
    A = ""
    for sublist in nested_list:
        sublist = sublist[0:-1]
        stringa = " ".join(sublist)
        if command == "left":
            stringa = string.ljust(stringa,width)
        if command == "right":
            stringa = string.rjust(stringa,width)
        if command == "center":
            stringa = string.center(stringa,width)
        if command == "justified":
            listOFstringa = sublist
            i = width - len(stringa)
            freeSpace = len(listOFstringa) - 1
            if freeSpace!=0:
                deleno = i/freeSpace
                i = i - (deleno*freeSpace)
                for word in listOFstringa:
                    if word!=listOFstringa[-1] and word!=" ":
                        index = listOFstringa.index(word)
                        listOFstringa = listOFstringa[0:index+1] + [" "] + listOFstringa[index+1:]
                        listOFstringa = listOFstringa[0:index+1] + [" "]*deleno + listOFstringa[index+1:]
                        if i!=0:
                            listOFstringa = listOFstringa[0:index+1] + [" "] + listOFstringa[index+1:]
                            i = i - 1       
            stringa = "".join(listOFstringa)
        A = A + stringa + "\n"
    return A

def get_new_name(filename, align, width,result):
    name = filename + "-" + "aligned" + "_" + align + "-" + str(width) + ".txt"
    file_with_data = open(name,"w")
    file_with_data.write(result)
    file_with_data.close()
get_new_name("Iva", command, width,just(result,command,width))

