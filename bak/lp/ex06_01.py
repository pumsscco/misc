#!/usr/bin/python
import copy
class Adder:
    def __init__(self,data):
        if type(data)==list or type(data)==dict:
            self.data=data
        else:
            raise TypeError("init data type error,must be list or dict")
    def __add__(self,y):
        return self.add(y)
    def add(self,y):
        print "Not Implemented"

class ListAdder(Adder):
    def add(self,y):
        if type(self.data)==list==type(y):
            return self.data+y
        else:
            raise TypeError("arg type error,must give two list!")

class DictAdder(Adder):
    def add(self,y):
        if type(self.data)==dict==type(y):
            z=copy.deepcopy(self.data)
            z.update(y)
            return z
        else:
            raise TypeError("arg type error,must give two dict!")


