#! /usr/bin/python
# -*- coding:utf-8 -*-

def p():
    i=[]
    f=2
    i[0]=0
    i[1]=1
    for s in range(10000):
        i[f] = i[f-1] + i [f-2]
        f = f+1
    print (i)

if __name__=='__main__':
    p()