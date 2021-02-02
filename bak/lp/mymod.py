#!/usr/bin/python
def countLines(name):
    """
	# for massive file
    cnt=0
    for line in open(name):
        cnt+=1
    return cnt
    """
    return len(open(name).readlines())

def countChars(name):
    return len(open(name).read())

def test(name):
    countLines(name)
    countChars(name)


