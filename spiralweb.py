import numpy as np, matplotlib.pyplot as plt

n = 50
t = np.linspace(0, 20*np.pi, 1000)
r = np.linspace(0, 1, 1000)
x, y = r*np.cos(t), r*np.sin(t)
plt.plot(x, y, 'k')

for i in range(n):
    a = 2*np.pi*i/n
    plt.plot([0, np.cos(a)], [0, np.sin(a)], 'k', lw=0.8)

plt.axis('off')
plt.show()
