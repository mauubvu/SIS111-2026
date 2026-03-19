def despejar(x):
    z=(15+(2*x/3))/(x**2+2)
    return f"El valor de z es: {z}"

print("Despejar Z")
print("*******************")

x=float(input("Introduzca el valor de x: "))
print(despejar(x))