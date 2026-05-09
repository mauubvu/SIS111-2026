def ingresarDatos():
    datos = []
    for i in range(int(input("Ingrese la cantidad de productos a comprar: "))):
        print(f"\nProducto número {i+1}")
        while True:
            etiqueta=int(input("Ingrese su etiqueta: "))
            if etiqueta>=1 and etiqueta<=1000:
                break
            else:
                print("La etiqueta tiene que ser un numero entre 1 y 1000")
        precio = float(input("Ingrese su precio: "))
        if '666' in str(etiqueta):
            precio=precio*0.2    
        datos.append({
            "etiqueta": etiqueta,
            "precio": precio,
        })
    return datos

def mostrarResumen(datos):
    print("\n\nResumen de Compra")
    total=0
    for d in datos:
        total+=d["precio"]
    print(f"Se deberan pagar {total:.2f}")

def main():
    print("\n\n--- Empresa Bonos ---")
    datos=ingresarDatos()
    mostrarResumen(datos)

main()