import math 

prod = math.prod

def binomial_coefficient(n, k):
    
    a = prod(i for i in range(1, n+1))
    b = prod(i for i in range(1, k+1))
    c = prod(i for i in range(1, n-k+1))
    
    return int(a / (b * c))

def binomial_expansion(p):
    
    l = []
    
    for i in range(p):
        
        s = ""
        if binomial_coefficient(p, i) != 1:
            s += str(binomial_coefficient(p, i))
        s += "a"
        s += str(p)
        l.append(s)
    
    return l

def formulas(p):
    
    L = []
    
    for i in range(p+1):
        
        if not binomial_expansion(i) == []:
        
            L.append(binomial_expansion(i))
    
    return L

def simplification(p):
    
    L = []
    
    for i in range(len(formulas(p))):
        l = []
        for j in range(i, len(formulas(p))):
            l.append(formulas(p)[j][i])
        L.append(l)
    return L

def calculator(p):
    
    s = ""
    
    for i in simplification(p)[::-1]:
        
        s += "("
        for j in i:
            s += j
            if i.index(j) != len(i)-1:
                s += "+"
        
        s += ")"
        if simplification(p)[::-1].index(i) != len(simplification(p)) - 1:
            s += " + "
    
    return s

print(calculator(8))
