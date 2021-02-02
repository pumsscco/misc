#!/usr/bin/env python
from glob import glob
import re
names=locals()
for y in ('2017','2018'):
    for m in range(12):
        names['fp'+y+'-'+'%02d'%(m+1)]=open('mongodb.log.'+y+'-'+'%02d'%(m+1),'w')
for f in glob('../mongodb.txt*'):
    for line in open(f):
        for y in ('2017','2018'):
            for m in range(12):
                pattern='^'+y+'-'+'%02d'%(m+1)
                if re.search(pattern,line):
                    names['fp'+y+'-'+'%02d'%(m+1)].write(line)

