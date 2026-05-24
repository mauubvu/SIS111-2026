def primo(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def generar(cantidad):
    primos=[]
    num=2
    while len(primos)<cantidad:
        if primo(num):
            primos.append(num)
        num+=1
    return primos

def indice(k):
    PERM=[0,3,2,4,1]
    k-=1
    grupo=k//5
    pos_grupo=k%5
    return grupo*5+PERM[pos_grupo]

def indice_max(ns):
    max=0
    for n in ns:
        idx=indice(n)
        if idx>max:
            max=idx
    return max

ns=[]
for t in range(int(input())):
    ns.append(int(input()))
primos=generar(indice_max(ns)+1)
for k in ns:
    print(primos[indice(k)])