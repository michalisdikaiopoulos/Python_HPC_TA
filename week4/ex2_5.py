import sys
import numpy as np
import time

@profile
def distance_matrix(p1, p2):
    p1 = np.radians(p1)
    p2 = np.radians(p2)

    D = np.empty((len(p1), len(p2)))
    for i in range(len(p1)):
        dsin2 = np.sin(0.5 * (p1[i] - p2)) ** 2
        cosprod = np.cos(p1[i, 0]) * np.cos(p2[:, 0])
        a = dsin2[:, 0] + cosprod * dsin2[:, 1]
        row = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        D[i, :] = row

    D *= 6371  # Earth radius in km
    return D


def load_points(fname):
    data = np.loadtxt(fname, delimiter=',', skiprows=1, usecols=(1, 2))
    return data


def distance_stats(D):
    # Extract upper triangular part to avoid duplicate entries
    assert D.shape[0] == D.shape[1], 'D must be square'
    idx = np.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        'mean': float(distances.mean()),
        'std': float(distances.std()),
        'max': float(distances.max()),
        'min': float(distances.min()),
    }


fname = sys.argv[1]
points = load_points(fname)
D = distance_matrix(points, points)
stats = distance_stats(D)
print(stats)


# Results
# Total time: 0.0329796 s
# File: points.py
# Function: distance_matrix at line 20
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     20                                           @profile
#     21                                           def distance_matrix(p1, p2):
#     22         1         15.0     15.0      0.0      p1 = np.radians(p1)
#     23         1          4.5      4.5      0.0      p2 = np.radians(p2)
#     24
#     25         1          9.6      9.6      0.0      D = np.empty(...
#     26       500        168.3      0.3      0.5      for i in range(len(p1)):
#     27       499      17275.1     34.6     52.4          dsin2 = ...
#     28       499       6913.0     13.9     21.0          cosprod = ...
#     29       499       1790.0      3.6      5.4          a = ...
#     30       499       4762.1      9.5     14.4          row = np.arctan2(...
#     31       499       1841.4      3.7      5.6          D[i, :] = row
#     32
#     33         1        199.7    199.7      0.6      D *= 6371  # Earth ...
#     34         1          0.8      0.8      0.0      return D