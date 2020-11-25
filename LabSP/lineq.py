from scipy import linalg  # TASK 2
import matplotlib.pyplot as plt
import numpy as np
file = open("lineq/large.txt", 'r')
size = int(file.readline())
file.close()
A1 = np.loadtxt("lineq/large.txt", skiprows=1)
A = A1[:size]
b = A1[size]
x = np.linspace(1, size, size)
plt.bar(x, linalg.solve(A, b), align='center', alpha=0.5)
plt.title('Solutions')
plt.show()
