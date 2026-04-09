from random import randint

def rand(n,r=[]):
    for i in range(n):
        r.append(randint(1,100))
    return r

def find(x,n,nx=0):
    randNum=rand(n)
    for i in randNum:
        if i==x: nx+=1
    return f'La lista de numeros es {randNum}\nEl numero {x} sale {nx} veces'

n=int(input('Introduzca el limite: '))
x=int(input('Introduzca el numero a encontrar: '))
print(find(x,n))