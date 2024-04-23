import numpy as np
import matplotlib.pyplot as plt
import math

mean = 0
gamma = 1
sigma = 2

L=3

N = 1000 #Number of time steps
T = 1 #Total time
dt = T/N #Time step 
t = np.linspace(0,T,N)
dW = np.sqrt(dt)

for k in range(L):

    X = np.zeros(N)

    for i in range (N-1):
        X[i+1] = X[i] + (-gamma * (X[i]-mean))*dt + sigma * dW * np.random.randn()

    plt.plot(t, X, linewidth = 0.5)


plt.xlabel("Time, t")
plt.ylabel("X")
plt.savefig('OU_EM.pdf')
plt.show()