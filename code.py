
#4-braids for n=3, 5, 7 , .. . 99.

import numpy as np
import math

 The variables are represented as elements of the string
 x[0] = w_1
 x[1] = w_2
 x[2] = u_1
 x[3] = u_2

Define Sec(x) function
def sec(x):
    return 1/math.cos(x)

Define the function f
def f(x,n):
    return np.array([x[3]**2 -x[0] +x[1],
                     x[2]*x[3] + x[2] + x[3] +1 +x[0] - x[1]*x[2] -x[1],
                     x[2]*x[3] +x[2] + x[3] +1 +2*x[0],
                     x[3] + 1 -2*x[1],
                     x[0] - 0.25 * (sec(math.pi / n))**2 * x[2]**2])

Define the Jacobian of f
def J(x,n):
    return np.array([[-1, 1, 0, 2*x[3]],
                     [1, -x[2] - 1, x[3] - x[1] + 1, x[2] + 1],
                     [2, 0, x[3] + 1, x[2] + 1],
                     [0, -2, 0, 1],
                     [1, 0, -0.25 * (sec(math.pi / n))**2 * 2*x[2], 0]])

Initial guess for x
x0 = np.array([0.5 + 0.5*1j]*4, dtype=np.complex128)

Iterate until convergence
for n in range(3,99,2):  # iterate over n from 3 to 99 with steps 2.
    while True:
        # Compute the QR decomposition of J(x)
        Q, R = np.linalg.qr(J(x0,n))

        # Compute the solution to the linear system J(x) * dx = -f(x)
        dx = np.linalg.solve(R, np.dot(Q.conj().T, -f(x0,n)))

        # Update
        x1 = x0 + dx

        # Check for convergence
        if np.linalg.norm(x1 - x0) < 1e-6:
            break

        x0 = x1

        print(np.round(x1,10))