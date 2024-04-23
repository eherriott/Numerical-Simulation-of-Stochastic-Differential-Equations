import random
import matplotlib.pyplot as plt
import math
import numpy as np

L = 1
N = 1000
end = 16
start = 1/N
t = np.linspace(start, end, N)
time = np.append(0,t)
time = time[:-1]
a = 1


X = np.zeros(N)
X[0] = 1
Sig = np.zeros([N,N])

for k in range (1,L+1):
    for i in range(N):
        for j in range(N):
            Sig[i][j] = min(t[i],t[j])

    L = np.linalg.cholesky(Sig)
    W = L.dot(np.random.randn(N,1))

    #plt.plot(time, W, linewidth = 0.5)


    for l in range(1,N):
        X[l] = X[0]*np.exp(a*W[l] - ((a**2)/2)*time[l])
    

    plt.plot(time, X, linewidth = 0.5)


plt.xlabel("Time, t")
plt.ylabel("X")
plt.savefig('Geometric_brownian_motion.pdf')
plt.show()