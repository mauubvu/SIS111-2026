def maxmin(a,b,c,mayor=0,menor=0):
    if a>=b and a>=c: mayor = a
    elif b>=a and b>=c: mayor = b
    else: mayor = c
    if a<=b and a<=c: menor = a
    elif b<=a and b<=c: menor = b
    else: menor = c
    return f'Mayor:{mayor} Menor:{menor}'

a=int(input("Introduce el primer numero: "))
b=int(input("Introduce el segundo numero: "))
c=int(input("Introduce el tercer numero: "))
print(maxmin(a,b,c))