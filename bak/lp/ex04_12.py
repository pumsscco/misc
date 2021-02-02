#!/usr/bin/python
#coding=utf8
#写4个计算阶乘的函数，然后调用timeit来计时(（为简单起见，不考虑参数有效性检验，参数必须是大于等于0的正整数）
from timeit import timeit
def fact1(N=11):
    if N<=1:
        return 1
    else:
        return N*fact1(N-1)
def fact2(N=11):
    if N<=1:
        return 1
    else:
        return reduce((lambda x,y:x*y),range(1,N+1))
def fact3(N=11):
    if N<=1:
        return 1
    else:
        l=range(1,N+1)
        m=l[1]
        for i in l[1:]:
            m*=i
        return m
def fact4(N=11):
    from math import factorial
    return factorial(N)
print 'fact1: ',timeit(fact1)
print 'fact2: ',timeit(fact2)
print 'fact3: ',timeit(fact3)
print 'fact4: ',timeit(fact4)