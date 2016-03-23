# *-* coding:utf-8 *-*

def uni(string):
	return unicode(string, "utf-8")
alphabet = ["a","ą","b","c","ć","d","e","ę","f","g","h","i","j","k","l","ł","m","n","ń","o","ó","p","r","s","ś","t","q","u","v","w","x","y","z","ź","ż"]
uniAlphabet = [uni(i) for i in alphabet]
