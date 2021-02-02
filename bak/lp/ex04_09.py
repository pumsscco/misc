#!/usr/bin/python
#coding=utf8
#4种求新列表的方法
l=[2,4,9,16,25]
sqrt_for=[]
for i in l:
    sqrt_for.append(i**.5)
print 'sqrt list by for: ',sqrt_for
sqrt_map=map((lambda x : x**.5),l)
print 'sqrt list by map: ',sqrt_map
sqrt_lcomp=[i**.5 for i in l]
print 'sqrt list by list comprehension: ',sqrt_lcomp
sqrt_ge=list(i**.5 for i in l)
print 'sqrt list by generator expression: ',sqrt_ge