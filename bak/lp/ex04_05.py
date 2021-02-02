#!/usr/bin/python
#coding=utf8
#完整拷贝，也就是要模拟copy模块的deepcopy的功能，这里偷一下懒，直接用系统的解决方案，否则要考虑太多细节
from copy import deepcopy
def copyDict(dic):
    new_dic={}
    for k in dic:
        new_dic[k]=deepcopy(dic[k])
        #如果不考虑嵌套，则以下亦可实现顶层复制
        #new_dic[k]=dic[k]
    return new_dic
    #如果要考虑最复杂的情况，最好直接用deepcopy代劳
    # return deepcopy(dic)

if __name__=='__main__':
    a={'a':['b','c'],'d':'e','f':{'1':'2'}}
    b=copyDict(a)
    print a
    print b
    print b is a