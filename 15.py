#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
    s = int(input('please set number:'))
    if s >= 90:
        print('A')
    elif s >= 60:
        print('B')
    else:
        print('C')

if __name__=='__main__':
    a()