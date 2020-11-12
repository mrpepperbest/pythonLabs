import matplotlib.pyplot as plt  # TASK 2
import numpy as np
f = open("evolution/frames.txt")
frames = []
N = int(sum(1 for i in f))
f.seek(0)
for _ in range(int(N/2)):
    x = [float(x) for x in f.readline().split()]
    y = [float(y) for y in f.readline().split()]
    frames.append(np.array([x, y]))
frames = np.array(frames)
fig, axs = plt.subplots(3, 2, figsize=(15, 12))
for _ in range(0, 3):
    axs[_, 0].plot(frames[_, 0], frames[_, 1])
    axs[_, 0].title.set_text("Frame "+str(_))
    axs[_, 0].grid()

    axs[_, 1].plot(frames[_+3, 0], frames[_+3, 1])
    axs[_, 1].title.set_text("Frame "+str(_+3))
    axs[_, 1].grid()

plt.setp(axs, xlim=(0, 17), ylim=(-10, 12))
plt.savefig("evolution/res.png")
plt.show()
