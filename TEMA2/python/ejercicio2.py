from random import randint

def rand(n):
    odd,even = [],[]
    for i in range(n):
        num = randint(1, 100)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd, even

def listAdd(odd, even):
    oddAdd, evenAdd = 0,0
    for num in odd:
        oddAdd += num
    for num in even:
        evenAdd += num
    return oddAdd, evenAdd

n = int(input('Introduzca el limite: '))
odd, even = rand(n)
oddAdd, evenAdd = listAdd(odd, even)
print(f'La lista de pares es {even} y su suma es {evenAdd}')
print(f'La lista de impares es {odd} y su suma es {oddAdd}')