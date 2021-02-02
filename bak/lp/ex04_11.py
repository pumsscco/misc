#!/usr/bin/python
#coding=utf8
#倒计时递归
def countdown(x):
    if type(x)!=int or x<0:
        return 'arg must positive integer!!!'
    if x==0:
        return 'stop'
    else:
        return '%i %s' %(x,countdown(x-1))

if __name__=='__main__':
    print countdown(5)
    print countdown(7)
    print countdown(99)
    print countdown(111)
    print countdown(-111)
    print countdown('66777')

    print 'generator expression for count down: \n', ' '.join(str(x) for x in range(77,0,-1))+' stop'