#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
	a = int (input('please set number:'))
	d = a
	s = 0
	b = []
	for i in range(2,a+1):
		while a != i:
		    if a % i == 0:
		    	b.append(i)
		    	a = a/i
		    	s = s + 1
		    else:
		    	break
	print('%d='%d,end='')
	for e in range(0,s):
		print('%d*'%b[e],end='')
	print('%d'%a)

if __name__=='__main__':
	a()