#! /usr/bin/python
# -*- coding:utf-8 -*-

def day():
    try:
        y = int(input('please set years:'))
        m = int(input('please set month:'))
        d = int(input('please set day:'))
        p = [31,28,31,30,31,30,31,31,30,31,30,31]
        r = [31,29,31,30,31,30,31,31,30,31,30,31]
        i = 0
        day = 0
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            for i in range(0,m-1):
                day = day + p[i]
            day = day + d
            print ('输入的是今年的第%d天'%day)
        else:
            for i in range(0,m-1):
                day = day + r[i]
            day = day + d
            print ('输入的是今年的第%d天'%day)
    except:
        print('your set data error')
        day()

if __name__ == '__main__':
    day()