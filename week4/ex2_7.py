import sys
import numpy as np
import time

@profile
def distance_matrix(p1, p2):
    p1 = np.radians(p1)
    p2 = np.radians(p2)

    dsin2 = np.sin(0.5 * (p1[:, None, :] - p2[None, :, :])) ** 2
    cosprod = np.cos(p1[:, None, 0]) * np.cos(p2[None, :, 0])
    D = 2 * np.arcsin(np.sqrt(dsin2[:, :, 0] + cosprod * dsin2[:, :, 1]))
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

# python -m kernprof -l -v week4/ex2_7.py /dtu/projects/02613_2025/data/locations/locations_1000.csv
