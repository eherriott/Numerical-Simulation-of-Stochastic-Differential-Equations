import numpy as np
import matplotlib.pyplot as plt
import math

a = 6

L = 1

N = 1000 #Number of time steps
T = 1 #Total time
dt = T/N #Time step 
t = np.linspace(0,T,N)

time = np.linspace(1/N, T, N)
tnew = np.append(0,time)
tnew = tnew[:-1]

dW = np.sqrt(dt)

X = np.zeros(N)
X[0] = 1
Sig = np.zeros([N,N])

for k in range (1,L+1):
    for i in range(N):
        for j in range(N):
            Sig[i][j] = min(time[i],time[j])

    L = np.linalg.cholesky(Sig)
    W = L.dot(np.random.randn(N,1))

    for l in range(1,N):
        X[l] = X[0]*np.exp(a*W[l] - ((a**2)/2)*tnew[l])

    plt.plot(tnew, X, linewidth = 0.5, color = 'blue')


Xm = np.zeros(N)
Xm[0] = 1

for i in range (N-1):
    Xm[i+1] = Xm[i] + (a*Xm[i]) * dW * np.random.randn() +\
    0.5*(a**2)*Xm[i]*((dW * np.random.randn())**2 - dt)

plt.plot(t, Xm, linewidth = 0.5, color = 'red')

Xem = np.zeros(N)
Xem[0] = 1

for i in range (N-1):
    Xem[i+1] = Xem[i] + (a*Xem[i]) * dW * np.random.randn()

plt.plot(t, Xem, linewidth = 0.5, color = 'green')


plt.xlabel("Time, t")
plt.ylabel("X")
plt.savefig('GB_comp.pdf')
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
plt.savefig('GB_diff.pdf')
plt.show()