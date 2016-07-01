#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
	a = int(input('please set frequency:'))
	k = int(input('please set number:'))
	s = 0
	e = k
	for i in range(0,a):
		s = s + k
		e = e * 10
		k = e + k
	print(s)

if __name__=='__main__':
	a()