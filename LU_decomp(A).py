def LU_decomp(A):
    
    '''Takes a matrix and converts it into two LU matrices'''
    
    U = A
    
    a = 0
    a_list = []
    while a < len(A):
        a_list.append(a)
        a += 1
        
    b = 0
    b_list = []
    while b < len(A[0]):
        b_list.append(b)
        b += 1
        
    c = 1
    c_list = []
    while c < len(A):
        c_list.append(c)
        c += 1
        
    L = []
    for a in a_list:
        l = []
        for b in b_list:
            if a == b:
                l.append(1)
            else: l.append(0)
        L.append(l)
    
    for a in a_list:
        for c in c_list:
            if a+c < len(U):
                d = U[a+c][a] / U[a][a]
                L[a+c][a] += d
                for b in b_list:
                    U[a+c][b] -= d*U[a][b]
    
    return L, U