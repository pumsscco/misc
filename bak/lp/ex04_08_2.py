#!/usr/bin/python
#coding=utf8
#找素数
from math import sqrt,floor
def prime(y):
    try:
        x=int(sqrt(y))
        if x<1:
            return 'error: prime must greater than 1'
    except Exception as e:
        return 'error: %s' % str(e)
    for i in range(2,int(x+1)):
        if y % x == 0: 
            if type(y)==float:
                return '%s has factor %.1f' % (y,x)
            else:
                return '%s has factor %i' % (y,x)
    else:
        return '%s is prime' % y

if __name__=='__main__':
    print prime(13)
    print prime(13.0)
    print prime(15)
    print prime(15.0)
