#!/usr/bin/python
def adder(*pargs):
    return reduce((lambda x,y: x+y),pargs)
    """
    res = pargs[0]
    for arg in pargs[1:]:
        res+=arg
    return res
    """
print adder('p','lu','to')
print adder(['p'])
print adder(0.19,5.57,0.34)
