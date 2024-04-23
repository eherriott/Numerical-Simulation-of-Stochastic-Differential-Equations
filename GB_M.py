import numpy as np
import matplotlib.pyplot as plt
import math

a = 1

L=10

N = 1000 #Number of time steps
T = 16 #Total time
dt = T/N #Time step 
t = np.linspace(0,T,N)
dW = np.sqrt(dt)

for k in range(L):

    X = np.zeros(N)
    X[0] = 1

    for i in range (N-1):
        X[i+1] = X[i] + (a*X[i]) * dW * np.random.randn() +\
        0.5*(a**2)*X[i]*((dW * np.random.randn())**2 - dt)

    plt.plot(t, X, linewidth = 0.5)


plt.xlabel("Time, t")
plt.ylabel("X")
plt.savefig('GB_M.pdf')
plt.show()