import numpy as np
from scipy import sparse
import json
import sys
import os
curdir = os.path.dirname(os.path.realpath(__file__))
from sklearn.preprocessing import normalize

def save_sparse_matrix(filename,x):
    x_coo=x.tocoo()
    row=x_coo.row
    col=x_coo.col
    data=x_coo.data
    shape=x_coo.shape
    np.savez(filename,row=row,col=col,data=data,shape=shape)

def load_sparse_matrix(filename):
    y=np.load(filename)
    z=sparse.coo_matrix((y['data'],(y['row'],y['col'])),shape=y['shape'])
    return z

def save_sparse():
    sm = sparse.csc_matrix(np.arange(10).reshape(2,5))
    save_sparse_matrix('sm.mpy', sm)

def transform_jsonMatrix_to_sparseFile(filename):
    cooc = json.loads(sys.stdin.read().strip('\n'))
    n = max([int(user) for user in cooc])+1
    cm = sparse.lil_matrix((n, n))
    for user in cooc:
        meetCount = sum(cooc[user].values())
        for meet in sorted([int(meet) for meet in cooc[user]]):
            meet = str(meet)
            cm[user, meet] = cooc[user][meet]/meetCount

    save_sparse_matrix(filename, cm)

def normalize_matrix():
    x = [[1,2,3], [4,5,6]]
    print(normalize(x, norm='l1', axis=0))

if __name__ == '__main__':
    pass
    normalize_matrix()
    #import networkx as nx
    #G = nx.from_scipy_sparse_matrix(load_sparse_matrix('{}/../data/10000_cm.npz'.format(curdir)))

    #transform_jsonMatrix_to_sparseFile('{}/../data/input_matrix'.format(curdir))