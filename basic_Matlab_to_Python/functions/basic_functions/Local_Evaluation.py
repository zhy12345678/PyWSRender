'''
这里边就是提到的进行local evaluation 的计算，里面有论文里提到的indics 这种引用方法可以进行借鉴
'''
import numpy as np



def local_evaluation(Index, N_DoF, Y, m, M, R):
    Results = 0
    print(Y)
    U, S, V = np.linalg.svd(Y)
    #here the U and VshangjiaoT are orthogonal matrics and S is a diagonal matrix containing the singular values of J.
    # Y_transpose = np.transpose(Y)
    # Y_transpose=Y*Y_transpose
    #pinv_Y = np.linalg.pinv(Y @ Y.T)
    trace_pinv_Y = np.trace(np.linalg.pinv(Y @ Y.T))
    hmmi = np.sqrt(1 / trace_pinv_Y)
    SS=S
    #SS = np.diag(S)
    J = Y[:3, :]

    #J_transpose = np.transpose(J)
    #J_J_transpose = np.dot(J, np.transpose(J))
    det_J_J_transpose = np.linalg.det(np.dot(J, np.transpose(J)))
    Sum_Singular = np.sqrt(det_J_J_transpose)

    Y = np.array(Y)  # Replace with your matrix Y
    M = np.array(M)  # Replace with your matrix M
    H = np.dot(Y, M)

    U, DS, V = np.linalg.svd(H)
    Dynamic_SS=DS
    #Dynamic_SS = np.diag(DS)
    Dynamic_Sum_Singular = np.sqrt(np.linalg.det(H @ H.T))
    Dynamic_hmmi = np.sqrt(1 / np.trace(np.linalg.pinv(H @ H.T)))

    if Index == 'Manipulability': ##可操作性  Sum_Singular    P
        Results = Sum_Singular * R
    elif Index == 'Inverse Condition Number': #逆条件数 SS
        Results = np.min(SS) / np.max(SS) * R
    elif Index == 'Minimum Singular Value': ##最小奇异值 SS
        Results = np.min(SS) * R
    elif Index == 'Order-Independent Manipulability': #Order-Independent可操纵性 Sum_Singular P
        Results = Sum_Singular ** (1 / N_DoF)
    elif Index == 'Harmonic Mean Manipulability Index': #调和平均操纵指数 hmmi
        Results = hmmi * R
    elif Index == 'Isotropic Index': #各向同性指数  Sum_Singular SS P
        Results = (Sum_Singular ** (1 / N_DoF)) / np.mean(SS) * R
    elif Index == 'Condition number':#条件数 SS
        Results = np.max(SS) / np.min(SS) * R
    elif Index == 'Max Singular': #马克斯奇异 SS
        Results = np.max(SS) * R
    elif Index == 'Dynamic Manipulability': #Dynamic_Sum_Singular
        Results = m * R
        Results = Dynamic_Sum_Singular * R
    elif Index == 'Dynamic Inverse Condition Number': #Dynamic_SS
        Results = np.min(Dynamic_SS) / np.max(Dynamic_SS) * R
    elif Index == 'Dynamic Minimum Singular Value':#Dynamic_SS
        Results = np.min(Dynamic_SS) * R
    elif Index == 'Dynamic Order-Independent Manipulability':#Dynamic_Sum_Singular
        Results = Dynamic_Sum_Singular ** (1 / N_DoF)
    elif Index == 'Dynamic Harmonic Mean Manipulability Index': #Dynamic_hmmi
        Results = Dynamic_hmmi * R
    elif Index == 'Dynamic Isotropic Index':#Dynamic_Sum_Singular， Dynamic_SS
        Results = (Dynamic_Sum_Singular ** (1 / N_DoF)) / np.mean(Dynamic_SS) * R
    elif Index == 'Dynamic Condition Number':#Dynamic_SS
        Results = np.max(Dynamic_SS) / np.min(Dynamic_SS) * R
    elif Index == 'Dynamic Max Singular':#Dynamic_SS
        Results = np.max(Dynamic_SS) * R

    return Results
