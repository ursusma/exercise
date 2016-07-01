#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
	a = 1
	e = 3
	for i in range(0,4):
		for e in range(0,e):
			print(' ',end='')
		for a in range(0,a):
			print('*',end='')
		a = a + 2
		e = e - 1
		print(a,e)
		break
	a = a - 2
	e += 1
	for b in range(0,3):
		for e in range(0,e):
			print(' ',end='')
		for a in range(0,a):
			print('*')
		a = a - 2
		e += 1

if __name__=='__main__':
	a()