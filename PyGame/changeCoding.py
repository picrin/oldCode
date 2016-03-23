#!/usr/bin/python
# -*- coding: utf-8 -*-
f = open('./slowa.txt')
f2 = open('./polishWordsUTF8.txt', 'w')

allwords = f.readlines()
for i in allwords:
	f2.write(i.decode("iso-8859-2").encode("utf-8"))


f.close()
f2.close()
