import numpy as np
import matplotlib.pyplot as plt
import math

sigma = 1

L=5

N = 1000 #Number of time steps
T = 1 #Total time
dt = T/N #Time step 
t = np.linspace(0,T,N)
dW = np.sqrt(dt)

for k in range(L):

    B = np.zeros(N)

    for i in range (N-1):
        B[i+1] = B[i] + (-(1/(1-t[i]))*B[i])*dt + sigma * dW * np.random.randn()

    plt.plot(t, B, linewidth = 0.5)


plt.xlabel("Time, t")
plt.ylabel("B(t)")
plt.savefig('Bb_EM.pdf')
plt.show()