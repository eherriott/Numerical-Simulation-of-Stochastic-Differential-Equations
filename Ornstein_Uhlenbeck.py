import random
import matplotlib.pyplot as plt
import math
import numpy as np

L = 15
N = 1000
gamma = 1
sigma = 2
t = np.linspace(0,10,N)


Sig = np.zeros([N,N])

for k in range (1,L+1):
    for i in range(N):
        for j in range(N):
            Sig[i][j] = (sigma**2/(2*gamma))*np.exp(-gamma*np.abs(t[i]-t[j]))

    L = np.linalg.cholesky(Sig)
    X = L.dot(np.random.randn(N,1))

    plt.plot(t, X, linewidth = 0.5)

sd = sigma/(math.sqrt(2*gamma))
plt.axhline(y = sd, linewidth = 0.5, color = "black", linestyle = "dashed")
plt.axhline(y = -sd, linewidth = 0.5, color = "black", linestyle = "dashed")

plt.xlabel("Time, t")
plt.ylabel("X")
plt.xticks(range(0,11))
plt.savefig('Ornstein_Uhlenbeck.pdf')
plt.show()