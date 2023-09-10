import numpy as np

def manipulability_measure(J):
    singular_values = np.linalg.svd(J, compute_uv=False)
    return np.prod(singular_values) ** (1 / len(singular_values))

def evaluate_multiple_jacobians(jacobians):
    """
    Compute the manipulability measure for a list of Jacobian matrices.
    :param jacobians: List of Jacobian matrices
    :return: List of manipulability measures
    """
    return [manipulability_measure(J) for J in jacobians]

# Example usage
J1 = np.array([[1, 0, 0],
               [0, 2, 0],
               [0, 0, 0.5]])

J2 = np.array([[0.5, 0.1, 0],
               [0, 1.5, 0.2],
               [0, 0, 1]])

J3 = np.array([[1.2, 0.1, 0.2],
               [0, 1.7, 0],
               [0.2, 0, 0.8]])

jacobians = [J1, J2, J3]
measures = evaluate_multiple_jacobians(jacobians)

print(measures)
