from random import randint

def rand(n,odd="",even=""):
    for i in range(n):
        r=randint(1,100)
        if r%2==0:
            even+=f'{r} '
        else:
            odd+=f'{r} '
    return f'Pares: {even} \nImpares: {odd}'

n=int(input('Introduzca el limite: '))
print(rand(n))