import random
import matplotlib.pyplot as plt
import numpy as np

N = 10

random_walk = list()
time = np.arange(N+1)
xs = list()
random_walk.append(0)
value = 0
xs.append(time[0])
rang = 2*N +1

for j in range (1,N+1):
    xs.append(time[j])
    xs.append(time[j])

i=1

while i < rang:
    random_walk.append(value)
    prob = random.random()
    movement  = -1 if prob < 0.5 else 1
    value = random_walk[i] + movement
    random_walk.append(value)
    i = i+2



plt.plot(xs, random_walk)
plt.xlabel("Time")
plt.ylabel("Position")
plt.savefig('Random_walk.pdf')
plt.show()
