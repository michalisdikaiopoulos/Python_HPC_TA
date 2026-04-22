import sys
from time import perf_counter as time
import numpy as np

def index_to_point(i, imsize, limits):
    c = np.unravel_index(i, imsize)
    # Subtract 1 from imsize[*] to match linspace
    stepw = (limits[1] - limits[0]) / (imsize[0] - 1)
    steph = (limits[3] - limits[2]) / (imsize[1] - 1)
    c = limits[0] + c[0] * stepw + 1j * (limits[2] + c[1] * steph)
    return c

def mandelbrot_escape_time(i, imsize, limits):
    c = index_to_point(i, imsize, limits)
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2:
            return i
    return 100

if __name__ == "__main__":
    width = int(sys.argv[1])
    height = width
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    fname = sys.argv[1] if len(sys.argv) > 1 else 'mandelbrot.raw'

    # Make sure the file is created and has the correct size
    f = np.memmap(fname, dtype='int32', mode='w+', shape=(width * height,))

    t = time()
    for i in range(width * height):
        f[i] = mandelbrot_escape_time(
            i,
            (width, height),
            (xmin, xmax, ymin, ymax),
        )
    print(time() - t)