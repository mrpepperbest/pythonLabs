import sympy  # TASK 3
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

# sympy
y = sympy.Function('y')
x = sympy.Symbol('x')
ode = sympy.Eq(y(x).diff(x), -2*y(x))
sympy.dsolve(ode, y(x))
general_solution = sympy.dsolve(ode, y(x))
value = general_solution.subs([(x, 0), (y(0), sympy.sqrt(2))])
ode_solution = general_solution.subs([(value.rhs, value.lhs)])

x1 = np.linspace(0, 10)
ode_function = sympy.utilities.lambdify((x,), ode_solution.rhs, modules='numpy')
y1 = ode_function(x1)

print("Sympy solution:", ode_solution.rhs)
# numpy


def dydx(y_, x_):
    return -2*y_


y0 = 2**(1/2)
x2 = np.linspace(0, 10)
y2 = odeint(dydx, y0, x1)

# plots
fig, axs = plt.subplots(2)
axs[0].set_title("Solutions")
axs[0].grid()
axs[0].plot(x1, y1, '-', label='sympy', color='red')
axs[0].plot(x2, y2, '--', label='scipy', color='black')
axs[0].legend(loc='upper right')

for i in range(y1.size):
    y1[i] -= y2[i]

axs[1].set_title("Difference")
axs[1].grid()
axs[1].plot(x1, y1, color="black")

plt.show()




