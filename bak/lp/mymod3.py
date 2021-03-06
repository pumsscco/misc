#!/usr/bin/python
#third edition, add self test
import sys
def countLines(fileobj):
    """
	# for massive file
    cnt=0
    for line in fileobj:
        cnt+=1
    return cnt
    """
    return len(fileobj.readlines())

def countChars(fileobj):
    return len(fileobj.read())

def test(name):
    fileobj=open(name)
    print 'Lines of file %s: %d ' % (name,countLines(fileobj))
    fileobj.seek(0)
    print 'Characters of file %s: %d ' % (name,countChars(fileobj))

if __name__=="__main__":
    test(sys.argv[1])
