import numpy as np  # TASK 3
from matplotlib import pyplot as plt
import matplotlib.animation as anm

f0 = np.genfromtxt("process/start.txt", delimiter="\n")
x = np.linspace(0, f0.size, f0.size, endpoint=True)
u = [f0]

A1 = (np.eye(x.size-1)*(-1))
A2 = np.zeros((x.size, x.size))
A2[1:x.size, :x.size-1] = A1
A = np.eye(x.size)
A[0, x.size-1] = -1
A = A+A2

for _ in range(255):
    u.append(u[_-1]-(0.5*A @ u[_-1]))


fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [])


def init():
    line.set_data(x, u[0])
    return line,


def animate(i):
    y = u[i+1]
    line.set_data(x, u[i])
    return line,

plt.xlim(0, 50)
plt.ylim(0, 10)
animate(1)


anim = anm.FuncAnimation(fig, animate, init_func=init, frames=255, interval=5, blit=True)

anim.save('process/process.gif')
