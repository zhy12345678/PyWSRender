import numpy as np
import sympy as sp


def manipulability_gradient(J, q):
    # Compute manipulability
    w = sp.sqrt(sp.det(J * J.T))

    # Differentiate w with respect to joint variables
    gradient = [sp.diff(w, qi) for qi in q]

    return gradient


# Define joint variables
q1, q2, q3 = sp.symbols('q1 q2 q3')

# Define a symbolic Jacobian as an example
J = sp.Matrix([[q1 + q2, q2 + q3, q3],
               [q1 - q2, q2 - q3, q3],
               [q1 * q2, q2 * q3, q3]])

gradient = manipulability_gradient(J, [q1, q2, q3])

print(gradient)
