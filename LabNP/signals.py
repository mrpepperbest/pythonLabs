import numpy as np  # TASK 2
import matplotlib.pyplot as plt
print("Insert test name (01-03):")
f = np.genfromtxt("signals/signal"+input()+".dat", delimiter="\n")
nf = np.copy(f)
x = np.linspace(0, f.size, f.size)
begin = nf[0:9]
for _ in range(1, 9):
    begin[_] = sum(f[0:_+1])/(_+1)
for i in range(f.size-9):
    nf[9+i] = np.sum(f[i:(10+i)]/10)
fig, axs = plt.subplots(2)
axs[0].set_title("Raw signal")
axs[0].grid()
axs[0].plot(x, f, color="black")

axs[1].set_title("Filterd signal")
axs[1].grid()
axs[1].plot(x, f, color="grey")
axs[1].plot(x, nf, color="black")

plt.show()


