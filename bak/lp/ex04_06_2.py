#!/usr/bin/python
#coding=utf8
#编写字典或列表相加的函数
from copy import deepcopy
def addDorL(arg1,arg2):
    if type(arg1)==type(arg2)==dict:
        new_dic={}
        for k in arg1:
            new_dic[k]=deepcopy(arg1[k])
        for k in arg2:
            if k not in new_dic:
                new_dic[k]=deepcopy(arg2[k])
        return new_dic
    elif type(arg1)==type(arg2)==list:
        return arg1+arg2

if __name__=='__main__':
    a={'a':['b','c'],'d':'e','f':{'1':'2'}}
    b={'a':['b','c'],'h':'e','g':{'3':'4'}}
    c=['a',{'f':'g'},'i','j']
    d=[1,2,34,5,6]
    print addDorL(a,b)
    print addDorL(c,d)