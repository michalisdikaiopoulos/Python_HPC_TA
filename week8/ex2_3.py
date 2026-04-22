import sys
import numpy as np
import matplotlib.pyplot as plt

fname = sys.argv[1]
step = int(sys.argv[2])

a = np.memmap(fname, dtype='int32', mode='r', shape=(1000, 1000))
a_ds = a[::step, ::step]
plt.imsave('mandelbrot_ds.png', a_ds, cmap='hot')