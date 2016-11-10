import numpy as np
from scipy.sparse import lil_matrix

def mul(a, b):
	n = a.shape[0]
	c = lil_matrix((n, n))
	aRowEmpty = [not row for row in a.rows]
	bRowEmpty = [not row for row in b.rows]

	for i in range(n):
		for j in range(n):
			if not (aRowEmpty[i] or bRowEmpty[j]):
				c[i, j] = a.getrow(i).multiply(b.getrow(j))[0,0]
	return c

def lil_multiply():
	sm = lil_matrix((300, 300))
	sm[0, 0] = 3
	sm[0, 2] = 1
	
	'''
	print sm
	print sm.transpose()
	print sm.getrow(0).todense()
	print sm.shape
	print sm.getrow(0)
	'''
	print mul(sm, sm.transpose())

if __name__ == '__main__':
	lil_multiply()
