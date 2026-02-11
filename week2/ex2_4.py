import sys
import numpy as np

fname = sys.argv[1]
array = np.load(fname)
np.save('cols.npy', array.mean(axis=0))
np.save('rows.npy', array.mean(axis=1))