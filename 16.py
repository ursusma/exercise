#! /usr/bin/python
# -*- coding:utf-8 -*-

def a():
    import datetime

    print(datetime.date.today().strftime('%d/%m/%Y'))

    a = datetime.date(1941,1,5)
    print(a.strftime('%d/%m/%Y'))

    b = a + datetime.timedelta(days=1)
    print (a.strftime('%d/%m/%Y'))

    a = a.replace(year=a.year+1)
    print (a.strftime('%d/%m/%Y'))

if __name__=='__main__':
	a()