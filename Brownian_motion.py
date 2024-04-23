import random
import matplotlib.pyplot as plt
import math
import numpy as np


L = 30
N = 100
end = 1
start = 1/N
t = np.linspace(start, end, N)
time = np.append(0,t)

Sig=np.zeros([N,N])

for k in range (1,L+1):
    for i in range(N):
        for j in range(N):
            Sig[i][j] = min(t[i],t[j])

    L = np.linalg.cholesky(Sig)
    X = L.dot(np.random.randn(N,1))

    plt.plot(time, np.append(0,X), linewidth = 0.5)

plust = [math.sqrt(i) for i in time]
minust = [-math.sqrt(i) for i in time]

plt.plot(time, plust,linewidth = 0.5, color = "black", linestyle = "dashed")
plt.plot(time, minust,linewidth = 0.5, color = "black", linestyle = "dashed")

plt.xlabel("t")
plt.ylabel("W(t)")
plt.savefig('Brownian_motion.pdf')
plt.show()