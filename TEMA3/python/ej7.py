def ingresarDatos():
    datos = []
    for i in range(3):
        print(f"\nCompra numero {i+1}")
        while True:
            codigo = int(input("(1) TV\n(2) Refrigerador\n(3) Lavadora\nIngrese el código: "))
            if codigo in [1, 2, 3]:
                break
            else:
                print("Código inválido, intente nuevamente.")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        datos.append({
            "codigo": codigo,
            "cantidad": cantidad,
            "precio": precio,
        })
    return datos

def calcular():
    datos = ingresarDatos()
    index = {
        1: {"nombre": "televisores", "cantidad": 0, "total": 0},
        2: {"nombre": "refrigeradores", "cantidad": 0, "total": 0},
        3: {"nombre": "lavadoras", "cantidad": 0, "total": 0}
    }
    for dato in datos:
        codigo = dato.get("codigo")
        cantidad = dato.get("cantidad")
        precio = dato.get("precio")
        index[codigo]["cantidad"] += cantidad
        index[codigo]["total"] += cantidad * precio
    return index

def mostrarResumen():
    datos = calcular()
    print("\n\nResumen de Compras")
    for d in datos:
        print(f"Se compraron {datos[d].get('cantidad')} {datos[d].get('nombre')}, a un total de {datos[d].get('total'):.2f}")

print("\n\n--- CyberStore ---")
mostrarResumen()