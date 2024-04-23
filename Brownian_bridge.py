import random
import matplotlib.pyplot as plt
import math
import numpy as np


L = 5
N = 1000
end = 1
start = 1/N
t = np.linspace(start, end, N)
time = np.append(0,t)

B = np.zeros(N+1)

Sig=np.zeros([N,N])

for k in range (1,L+1):
    for i in range(N):
        for j in range(N):
            Sig[i][j] = min(t[i],t[j])

    L = np.linalg.cholesky(Sig)
    W = L.dot(np.random.randn(N,1))

    for l in range (1,N):
        B[l] = W[l] - (time[l]*W[-1])
    

    plt.plot(time, B, linewidth = 0.5)



plt.xlabel("t")
plt.ylabel("B(t)")
plt.savefig('Brownian_bridge.pdf')
plt.show()