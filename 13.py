#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
    for i in range(123,1000):
        a = int(i / 100)
        b = int(i / 10 % 10)
        c = i % 10
        if a * a * a + b * b * b + c * c * c == i:
            print(i)

if __name__=='__main__':
    a()