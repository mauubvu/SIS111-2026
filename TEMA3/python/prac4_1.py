def suma(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total

def digitos(n):
    if n<=0:
        return False
    count=0
    while n>0:
        count+=1
        n//=10
    return count>3

def main():
    while True:
        a=int(input("Introduzca el primer numero: "))
        if digitos(a):
            break
        else:
            print("Numero invalido")
    while True:
        b=int(input("Introduzca el segundo numero: "))
        if digitos(b):
            break
        else:
            print("Numero invalido")
    suma_a, suma_b = suma(a), suma(b)
    print("Son amigos" if (suma_a==suma_b) else "No son amigos")
main()