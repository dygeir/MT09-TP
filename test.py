import numpy as np

def choleski(A):
    # A compléter ...
    B = np.zeros(A.shape)
    for j in range(A.shape[1]):
        for i in range(j,A.shape[0]):
            if i==j:
                B[i][j]=A[i][j]
                for k in range(0,j):
                    B[i][j]-=B[i][k]*B[i][k]
                B[i][j]=np.sqrt(B[i][j])
            else:
                B[i][j]=A[i][j]
                for k in range(0,i):
                    B[i][j]-=B[i][k]*B[j][k]
                B[i][j]/=B[j][j]
    # fini
    return B

A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
B=choleski(A)
print(B@B.T)