#!/usr/bin/python
def adder(**kwargs):
    return reduce((lambda x,y: x+y),kwargs.values())
print adder(a='p',b='lu',c='to')
print adder(d=['p'])
print adder(e=0.19,f=5.57,g=0.34)
