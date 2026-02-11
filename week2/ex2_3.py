import sys
import numpy as np

x = [float(a) for a in sys.argv[1:]]
np.save('diag', np.diag(x))