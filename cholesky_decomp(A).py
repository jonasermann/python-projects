import math 

def cholesky_decomp(A):
    
    a = 0
    a_list =[]
    while a < len(A):
        a_list.append(a)
        a += 1
    
    b = 0
    b_list =[]
    while b < len(A[0]):
        b_list.append(b)
        b += 1           
    
    L = []
    for a in a_list:
        l = []
        for b in b_list:
            l.append(0)
        L.append(l)
    
    for a in a_list:
        for b in b_list:
            
            if a - b == 1:
               
                L[a][b] += A[a][b] / L[a-1][b]
                
            elif a - b == 0:
                
                if a != 0:
                    
                    L[a][b] += math.sqrt(A[a][b] - (L[a][b-1]**2))
                    
                else: 
                    
                    L[a][b] += math.sqrt(A[a][b])
                
    return L