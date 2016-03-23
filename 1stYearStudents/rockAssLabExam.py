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
        

lista = read_from_file("abstract.txt")[::-1]

szpalta = Szpalta(25)

while lista:
    szpalta.put(lista.pop())
print szpalta.getLines()
