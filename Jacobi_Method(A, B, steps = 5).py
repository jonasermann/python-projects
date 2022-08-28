def Jacobi_Method(A, B, steps = 5):
    
    X = []
    
    for a in A[0]:
        l = [0]
        X.append(l)
      
    a_list = []
    a = 0
    while a < len(A):
        a_list.append(a)
        a += 1
    
    b_list = []
    b = 0
    while b < len(A[0]):
        b_list.append(b)
        b += 1
    
    while steps > 0:
        for a in a_list:
            y = 0
            for b in b_list:
                if a != b:
                    y += A[a][b]*X[b][0]/A[a][a]
            X[a][0] = 0
            X[a][0] += (B[a][0]/A[a][a]) - y
        steps -= 1
    
    return X