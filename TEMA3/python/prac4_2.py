def primo(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def suma(n):
    lista=[]
    total=0
    i=2
    while i <= n:
        if primo(i):
            total+=i
            lista.append(i)
        i+=1
    return lista,total

def main():
    n=int(input("Ingrese el limite: "))
    lista,total=suma(n)
    print(f'Numeros primos: {lista}')
    print(f'Suma: {total}')

main()