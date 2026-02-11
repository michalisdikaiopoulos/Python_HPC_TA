import sys
import numpy as np

def magnitude(x):
    return np.sqrt(np.sum(x*x))

if __name__ == "__main__":
    x = np.array([float(a) for a in sys.argv[1:]])
    print(magnitude(x))