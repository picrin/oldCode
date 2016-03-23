import random
import math
def funkcjaRzeczywista(x):
	return math.log(x)

def monteCarlo(funkcjaCalkowana, przedzial, liczbaPowtorzen):
	punkty = [random.uniform(przedzial[0], przedzial[-1]) for i in range(liczbaPowtorzen)]
	punkty.sort()
	punkty = [przedzial[0]] + punkty + [przedzial[-1]]
	prawdziwyPrzedzial = []
	for indeks, wartosc in enumerate(punkty):
		if indeks < len(punkty) - 1:
			prawdziwyPrzedzial += [punkty[indeks+1] - wartosc]
	polaProstokatow = []
	for indeks, szerokoscPrzedzialu in enumerate(prawdziwyPrzedzial):
		poleProstokatu = szerokoscPrzedzialu * funkcjaCalkowana(sum([punkty[indeks+1], punkty[indeks]])/2)
		polaProstokatow += [poleProstokatu]	
	return sum(polaProstokatow)

print monteCarlo(funkcjaRzeczywista, [0, 1], 10000)
print math.e
