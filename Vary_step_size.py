import random
import matplotlib.pyplot as plt
import numpy as np

L = 20
N = 100
time = np.arange(N+1)

rang = 2*N + 1
s = 1

xs = list()
xs.append(time[0])

for j in range (1,N+1):
    xs.append(time[j])
    xs.append(time[j])

for k in range (1,L+1):
    i = 1
    random_walk = list()
    random_walk.append(0)
    value = 0

    while i < rang:
        random_walk.append(value)
        prob = random.random()
        movement  = -s if prob < 0.5 else s
        value = random_walk[i] + movement
        random_walk.append(value)
        i = i+2

    y = random_walk
    plt.plot(xs, y, linewidth = 0.5)
    s = s+1

plt.xlabel("Time")
plt.ylabel("Position")
plt.savefig('Vary_step_size.pdf')
plt.show()