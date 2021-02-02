from mymod3 import *
import mymod3,sys

if __name__=="__main__":
    print 'test from import'
    test(sys.argv[1])
    print 'test import'
    mymod3.test(sys.argv[1])
