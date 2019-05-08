import math
import multiprocessing as mp
import numpy as np
def simulate_geometric_brownian_motion(p):
    M,I = p
    S0 = 100.
    T = 1.0
    r = 0.05
    sigma = 0.2
    dt = T / M
    paths = np.zeros((M+1,I))
    paths[0] = S0
    for t in range(1,M+1):
        paths[t] = paths[t-1] * np.exp((r-0.5*sigma**2)*dt + sigma*math.sqrt(dt)*np.random.standard_normal(I))
    return paths

paths = simulate_geometric_brownian_motion((5,2))
print(paths)