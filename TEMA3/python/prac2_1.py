def ingresarDatos():
    datos = []
    n = int(input("Ingrese la cantidad de trabajadoras: "))
    for i in range(n):
        print(f"\nTrabajadora número {i+1}")
        while True:
            estado = int(input("(1) Soltera\n(2) Casada\n(3) En pareja\nIngrese el código: "))
            if estado in [1, 2, 3]:
                break
            else:
                print("Código inválido, intente nuevamente.")
        hijos = int(input("Ingrese la cantidad de hijos: "))
        datos.append({
            "estado": estado,
            "hijos": hijos
        })
    return datos

def calcular():
    datos = ingresarDatos()
    index = {
        1: {"estado": "solteras", "trabajadoras": 0, "hijos": 0},
        2: {"estado": "casadas", "trabajadoras": 0, "hijos": 0},
        3: {"estado": "en pareja", "trabajadoras": 0, "hijos": 0}
    }
    total_bono = 0
    for dato in datos:
        estado = dato.get("estado")
        hijos = dato.get("hijos")
        index[estado]["trabajadoras"] += 1
        index[estado]["hijos"] += hijos
        total_bono += hijos * 2000
    return index, total_bono

def mostrarResumen():
    datos, bono = calcular()    
    print("\n\nResumen de Bonos")
    for d in datos:
        print(f"Hay {datos[d].get('trabajadoras')} trabajadoras {datos[d].get('estado')}, con {datos[d].get('hijos')} hijos")    
    print(f"\nEl total del bono entregado por la empresa es de: {bono} Bs")

print("\n\n--- Empresa Bonos ---")
mostrarResumen()