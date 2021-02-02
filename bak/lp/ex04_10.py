#!/usr/bin/python
#coding=utf8
#3种求平方根方法的性能评估
from timeit import timeit
print 'benchmark for sqrt from math module: ',timeit(stmt='sqrt(193454303931)',setup='from math import sqrt')
print 'benchmark for sqrt from **: ',timeit('193454303931**.5')
print 'benchmark for sqrt from pow: ',timeit('pow(193454303931,.5)')

def dict_for():
    d={}
    for k in range(1000):
        d[k]=k**2
    return d
print 'benchmark for dict from for: ',timeit(dict_for)
print 'benchmark for dict from comprehension: ',timeit('{x:x**2 for x in range(1000)}')