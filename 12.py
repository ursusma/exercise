#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
    for i in range(101,200):
        s = 0
        for k in range(2,i):
            if i % k == 0:
                s = s + 1
        if s == 2 or s < 2:
            print (i)

if __name__=='__main__':
    a()