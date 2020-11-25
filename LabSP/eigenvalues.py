from sympy import *  # TASK 1
x, l, m, p = symbols('x λ μ ρ')
M = zeros(9, 9)
M[3, 0] = -(l+2*m)
M[6, 0] = -l
M[8, 0] = -l
M[4, 1] = -m
M[5, 2] = -m
M[0, 3] = -1/p
M[1, 4] = -1/p
M[2, 5] = -1/p

for i in range(len(M.eigenvals())):
    print("eiginval: ", list(M.eigenvals().keys())[i], ", algebraic multiplicity: ", list(M.eigenvals().values())[i])


