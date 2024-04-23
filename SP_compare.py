import numpy as np
import matplotlib.pyplot as plt
import math

mu = 0.1
sigma = 0.2


N = 1000 #Number of time steps
T = 40 #Total time
dt = T/N #Time step 
t = np.linspace(0,T,N)

time = np.linspace(1/N, T, N)
tnew = np.append(0,time)
tnew = tnew[:-1]

dW = np.sqrt(dt)

X = np.zeros(N)
X[0] = 0.1
Sig = np.zeros([N,N])


for i in range(N):
    for j in range(N):
        Sig[i][j] = min(time[i],time[j])

L = np.linalg.cholesky(Sig)
W = L.dot(np.random.randn(N,1))

for l in range(1,N):
    X[l] = X[0]*np.exp((mu - (sigma**2/2))*tnew[l]+ sigma*W[l])

plt.plot(tnew, X, linewidth = 0.5, color = 'blue')


Xm = np.zeros(N)
Xm[0] = 0.1

for i in range (N-1):
    Xm[i+1] = Xm[i] + (mu*Xm[i]) * dt + (sigma*Xm[i]) * dW * np.random.randn() +\
        0.5*(sigma**2)*Xm[i]*((dW * np.random.randn())**2 - dt)

plt.plot(t, Xm, linewidth = 0.5, color = 'red')

Xem = np.zeros(N)
Xem[0] = 1

for i in range (N-1):
    Xem[i+1] = Xem[i] + (mu*Xem[i]) * dt + (sigma*Xem[i]) * dW * np.random.randn()

plt.plot(t, Xem, linewidth = 0.5, color = 'green')


plt.xlabel("Time, t")
plt.ylabel("X")
plt.savefig('SP_comp.pdf')
plt.show()

ndiff = np.zeros(N)
for i in range(N):
    ndiff[i] = Xm[i] - Xem[i]

plt.plot(t, ndiff, linewidth = 0.5, color = 'blue') 

emdiff = np.zeros(N)
for i in range(N):
    emdiff[i] = X[i] - Xem[i]

plt.plot(t, emdiff, linewidth = 0.5, color = 'green') 

mdiff = np.zeros(N)
for i in range(N):
    mdiff[i] = X[i] - Xm[i]

plt.plot(t, mdiff, linewidth = 0.5, color = 'red')

plt.xlabel("Time, t")
plt.ylabel("X")
plt.savefig('SP_diff.pdf')
plt.show()