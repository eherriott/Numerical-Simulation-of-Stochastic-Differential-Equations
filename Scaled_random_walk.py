import random
import matplotlib.pyplot as plt
import math
import numpy as np

L = 3
N = 10


for k in range (1,L+1):
    up = 1/math.sqrt(N)
    down = -1/math.sqrt(N)

    time = np.arange(N+1)
    scaled_random_walk = list()
    xs = list()
    scaled_random_walk.append(0)
    value = 0
    xs.append(time[0])
    rang = 2*N +1

    for j in range (1,N+1):
        xs.append(time[j]/N)
        xs.append(time[j]/N)

    i = 1
    
    while i < rang: 
        scaled_random_walk.append(value)       
        prob = random.random()
        movement  = down if prob < 0.5 else up
        value = scaled_random_walk[i] + movement       
        scaled_random_walk.append(value)
        i = i +2

    y = scaled_random_walk
    plt.plot(xs, y, linewidth = 0.5)
    N = N*10

plt.xlabel("Time")
plt.ylabel("Position")
plt.savefig('Scaled_random_walk.pdf')
plt.show()
