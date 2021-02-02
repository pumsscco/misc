L=[]
for i in range(7): L.append(2**i)
X = 5
y=2**X
if y in L:
	print 'at index ',L.index(y)
else:
	print X, 'not found'
