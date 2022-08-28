def matrix_mult(A, B):
    
    if type(A[0]) == list:
        if type(B[0] == list):

            a = 0
            a_list = []
            while a < len(A):
                a_list.append(a)
                a += 1
            
            b = 0
            b_list = []
            while b < len(B):
                b_list.append(b)
                b += 1
            
            c = 0
            c_list = []
            while c < len(A):
                c_list.append(c)
                c += 1
            
            C = [] 
            for a in a_list:    
                l = []    
                for c in c_list:        
                    s = 0    
                    for b in b_list:    
                        s += A[a][b] * B[b][c]    
                    l.append(s)    
                C.append(l)
            
            return C
        
    else:

        a = 0
        a_list = []
        while a < len(A):
            a_list.append(a)
            a += 1
            
        if len(a_list) == len(B):
                
            C = [] 
            s = 0
            for a in a_list:      
                s += A[a] * B[a][0]      
            C.append(s)  
            
        return C

#def matrix_mult(A, B): (gammal version)
    
    '''Takes two matrices and multiplies the with each other'''
    
    if len(A[0]) != len(B):
        
        print("Matrices cannot be multiplied with each other")
    
    else:
        
        a = 0
        a_list = []
        while a < len(A):
            a_list.append(a)
            a += 1
            
        b = 0
        b_list = []
        while b < len(B):
            b_list.append(b)
            b += 1
            
        c = 0
        c_list = []
        while c < len(A):
            c_list.append(c)
            c += 1
            
        C = [] 
        for a in a_list:    
            l = []    
            for c in c_list:        
                s = 0    
                for b in b_list:    
                    s += A[a][b] * B[b][c]    
                l.append(s)    
            C.append(l)    
            
        return C
                        