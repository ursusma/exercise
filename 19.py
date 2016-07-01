#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
	a = int(input('please set number:'))
	s = []
	e = 0
	d = 0
	for i in range(1,a):
		if a % i == 0:
			s.append(i)
			e = e + 1
	for b in range(0,e):
		d = d + s[b]
	if a == d:
		print (a)
		print (s)
	else:
		print ('this not')

if __name__=='__main__':
	a()