import sys
import os
curdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append('{}/../lib'.format(curdir))

from lib import transform_jsonMatrix_to_sparseFile

if __name__ == '__main__':
    filename = sys.argv[1]
    transform_jsonMatrix_to_sparseFile('{}/../data/{}'.format(curdir, filename))