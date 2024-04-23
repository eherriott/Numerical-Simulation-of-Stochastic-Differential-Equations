import random
import matplotlib.pyplot as plt
import math
import numpy as np


L = 10
N = 100
end = 1
start = 1/N
t = np.linspace(start, end, N)

Sig=np.zeros([N,N])

for k in range (1,L+1):
    for i in range(N):
        for j in range(N):
            Sig[i][j] = min(t[i],t[j])

    L = np.linalg.cholesky(Sig)
    X = L.dot(np.random.randn(N,1))
    Y = L.dot(np.random.randn(N,1))

    plt.plot(np.append(0,X), np.append(0,Y), linewidth = 0.5)

plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('2D_brownian_motion.pdf')
plt.show()