#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
	import string

	a = (input('input string:'))
	b = 0
	c = 0
	d = 0
	e = 0
	for i in a:
		if i.isalpha():
			b += 1
		elif i.isspace():
			c += 1
		elif i.isdigit():
			d += 1
		else:
			e += 1
	print ('char=%d,space=%d,digit=%d,others=%d'%(b,c,d,e))

if __name__=='__main__':
	a()