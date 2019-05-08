# 蒙特卡洛算法
import numpy as np


def bsm_mcs_valuation(strike):
    S0 = 100.
    T = 1.0
    r = 0.05
    vola = 0.2
    M = 50
    I = 20000
    dt = T/M
    rand = np.random.standard_normal((M+1,I))
    S = np.zeros((M+1,I))
    S[0] = S0
    for t in range(1,M+1):
        S[t] = S[t-1] * np.exp((r-0.5*vola**2)*dt + vola*np.sqrt(dt)*rand[t])
    value = (np.exp(-r * T)*np.sum(np.maximum(S[-1]-strike,0))/I)
    return value



