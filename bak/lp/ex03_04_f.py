L=map(lambda x: 2 ** x, range(7))
X = 5
y=2**X
if y in L:
	print 'at index ',L.index(y)
else:
	print X, 'not found'
