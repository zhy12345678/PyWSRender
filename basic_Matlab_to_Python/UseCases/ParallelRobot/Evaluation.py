'''
这里边就是提到的进行local evaluation 的计算，里面有论文里提到的indics 这种引用方法可以进行借鉴
'''
import numpy as np

def local_evaluation(Index, N_DoF, Y, m, M, R):
    Results = 0
    U, S, V = np.linalg.svd(Y)
    #here the U and VshangjiaoT are orthogonal matrics and S is a diagonal matrix containing the singular values of J.
    # Y_transpose = np.transpose(Y)
    # Y_transpose=Y*Y_transpose
    pinv_Y = np.linalg.pinv(Y @ Y.T)
    trace_pinv_Y = np.trace(pinv_Y)
    hmmi = np.sqrt(1 / trace_pinv_Y)
    SS=S
    #SS = np.diag(S)
    J = Y[:3, :]

    J_transpose = np.transpose(J)
    J_J_transpose = np.dot(J, J_transpose)
    det_J_J_transpose = np.linalg.det(J_J_transpose)
    Sum_Singular = np.sqrt(det_J_J_transpose)

    Y = np.array(Y)  # Replace with your matrix Y
    M = np.array(M)  # Replace with your matrix M
    H = np.dot(Y, M)



    if Index == 'Manipulability':
        Results = Sum_Singular * R
    elif Index == 'Inverse Condition Number':
        Results = np.min(SS) / np.max(SS) * R
    elif Index == 'Minimum Singular Value':
        Results = np.min(SS) * R
    elif Index == 'Order-Independent Manipulability':
        Results = Sum_Singular ** (1 / N_DoF)
    elif Index == 'Harmonic Mean Manipulability Index':
        Results = hmmi * R
    elif Index == 'Isotropic Index':
        Results = (Sum_Singular ** (1 / N_DoF)) / np.mean(SS) * R
    elif Index == 'Condition number':
        Results = np.max(SS) / np.min(SS) * R
    elif Index == 'Max Singular':
        Results = np.max(SS) * R


    return Results
