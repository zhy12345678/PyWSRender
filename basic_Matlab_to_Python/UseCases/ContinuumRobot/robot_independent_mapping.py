import numpy as np


def robot_independent_mapping(kappa, phi, ell, ptsperseg):
    numseg = len(kappa)
    if len(kappa) != len(phi) or len(kappa) != len(ell):
        raise ValueError("Dimension mismatch.")

    if numseg > 1 and isinstance(ptsperseg, int):
        ptsperseg = [ptsperseg] * numseg

    g = np.zeros((np.sum(ptsperseg), 16))
    T_base = np.eye(4)

    for i in range(numseg):
        T = np.zeros((ptsperseg[i], 16))
        c_p = np.cos(phi[i])
        s_p = np.sin(phi[i])

        for j in range(ptsperseg[i]):
            c_ks = np.cos(kappa[i] * j * (ell[i] / ptsperseg[i]))
            s_ks = np.sin(kappa[i] * j * (ell[i] / ptsperseg[i]))

            if kappa[i] != 0:
                T_temp = [c_p * c_p * (c_ks - 1) + 1, s_p * c_p * (c_ks - 1), -c_p * s_ks, 0,
                          s_p * c_p * (c_ks - 1), c_p * c_p * (1 - c_ks) + c_ks, -s_p * s_ks, 0,
                          c_p * s_ks, s_p * s_ks, c_ks, 0,
                          (c_p * (1 - c_ks)) / kappa[i], (s_p * (1 - c_ks)) / kappa[i], s_ks / kappa[i], 1]
            else:
                T_temp = [c_p * c_p * (c_ks - 1) + 1, s_p * c_p * (c_ks - 1), -c_p * s_ks, 0,
                          s_p * c_p * (c_ks - 1), c_p * c_p * (1 - c_ks) + c_ks, -s_p * s_ks, 0,
                          c_p * s_ks, s_p * s_ks, c_ks, 0,
                          0, 0, j * (ell[i] / ptsperseg[i]), 1]

            T[j, :] = np.reshape(np.dot(T_base, np.reshape(T_temp, (4, 4))), (1, 16))

        if i == 0:
            g[:ptsperseg[i], :] = T
        else:
            g[np.sum(ptsperseg[:i]):np.sum(ptsperseg[:i]) + ptsperseg[i], :] = T

        T_base = np.reshape(T[ptsperseg[i] - 1, :], (4, 4))

    return g


# Example usage
# kappa = np.array([1 / 40e-3, 1 / 10e-3])
# phi = np.array([0, np.pi])
# ell = np.array([25e-3, 20e-3])
# ptsperseg = np.array([10])
# g = robot_independent_mapping(kappa, phi, ell, ptsperseg)
# print(g)
