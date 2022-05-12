"""hash function"""
def hash_value(offm, T, P, m, d, q):
    p, t = 0, 0 
    for i in range(0, m):
        p  = (d*p + ord(P[i])) % q
        print(T[i+offm])
        t  = (d*t + ord(T[i+offm]))  % q 
    return p, t

"""robin karp algorithm"""
def robin_karp(T, P, d, q):
    n  = len(T)
    m  = len(P)
    h  = d**(m-1) % q
    p = 0
    t = 0
    for s in range(0, n - m + 1):
        if p == t:
            if P[0:m] == T[s:s+m]:
                print(f" '{P}' trouvé en position : {s}")
                return True
    return False
        
txt     = "hello everyone"
pattern = "everyone"
print(robin_karp(txt, pattern, 2, 13))