#!/usr/bin/python
#coding=utf8
#编写字典相加的函数
from copy import deepcopy
def addDict(dic1,dic2):
    new_dic={}
    #键重复，这里取前一个字典的键值对
    for k in dic1:
        new_dic[k]=deepcopy(dic1[k])
    for k in dic2:
        if k not in new_dic:
            new_dic[k]=deepcopy(dic2[k])
    return new_dic

if __name__=='__main__':
    a={'a':['dd','gg'],'d':'e','f':{'1':'2'}}
    b={'a':['b','c'],'h':'e','g':{'3':'4'}}
    print addDict(a,b)
