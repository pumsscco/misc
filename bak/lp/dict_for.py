#!/usr/bin/python

def dict_for():
	d={}
	for k in range(1000):
		d[k]=k**2
	return d
print dict_for()

print {x:x**2 for x in range(1000)}




