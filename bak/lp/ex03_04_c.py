L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if 2 ** X in L:
	print 'at index ',L.index(2**X)
else:
	print X, 'not found'
