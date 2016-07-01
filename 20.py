#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
	a = 100.0
	s = 0.0
	for i in range(0,10):
		s = s + a
		a = a * 0.5
	print (s,a)

if __name__=='__main__':
	a()
