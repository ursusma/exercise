#! /usr/bin/python
# -*- coding:utf-8 -*-

import math

def pf():
    for i in range(0,10000):
        x = int(math.sqrt(i+100))
        y = int(math.sqrt(i+268))
        if (x*x==i+100) and (y*y==i+268):
            print (i)

if __name__=='__main__':
    pf()