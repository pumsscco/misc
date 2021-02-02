L=[2**x for x in range(7)]
X = 5
y=2**X
if y in L:
	print 'at index ',L.index(y)
else:
	print X, 'not found'
