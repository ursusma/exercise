#! /usr/bin/python
# -*- coding:utf-8 -*-

def s():
    try:
        l = []
        for i in range (0,3):
            a = int (input('please set your number:'))
            l.append(a)
        l.sort()
        print (l)
    except:
        print('your set number error')
        s()

if __name__=='__main__':
    s()