import numpy as np
import matplotlib.pyplot as plt
import math

mu = 0.1
sigma = 0.2

L=1

N = 1000 #Number of time steps
T = 40 #Total time
dt = T/N #Time step 
t = np.linspace(0,T,N)
dW = np.sqrt(dt)

for k in range(L):

    X = np.zeros(N)
    X[0] = 0.1

    for i in range (N-1):
        X[i+1] = X[i] + (mu*X[i]) * dt + (sigma*X[i]) * dW * np.random.randn()

    plt.plot(t, X, linewidth = 0.5)


plt.xlabel("Days")
plt.ylabel("Stock price")
plt.savefig('SP_EM.pdf')
plt.show()