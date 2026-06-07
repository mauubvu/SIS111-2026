def mostrar_menu():
    print("-----------------\n")
    print("1. Registrar material")
    print("2. Listar material")
    print("3. Buscar material por codigo")
    print("4. Actualizar cantidad de material")
    print("5. Mostrar materiales con baja cantidad")
    print("6. Mostrar resumen por categoria")
    print("7. Salir\n")

def codigo_existe(materiales,codigo):
    for m in materiales:
        if m["codigo"]==codigo:
            return True
    return False

def registrar_material(materiales):
    print("-----------------")
    print("\nREGISTRAR MATERIAL\n")
    while True:
        codigo=input("Codigo (ej. M001): ").upper()
        if codigo_existe(materiales,codigo):
            print(f'El codigo {codigo} ya esta registrado')
        else:
            break
    nombre=input("Nombre del material: ")
    categoria=input("Categoria: ").upper()
    while True:
        try:
            cantidad=int(input("Cantidad: "))
            if cantidad>=0:
                break
            else:
                print("La cantidad debe ser mayor o igual a 0, intente de nuevo")
        except:
            print("Error, ingrese un numero entero")
    estado="Disponible" if cantidad !=0 else "Agotado"
    material={
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "estado": estado,
    }
    materiales.append(material)
    print(f'\nMaterial {nombre} ({codigo}) registrado exitosamante')

def listar_materiales(materiales):
    print("-----------------")
    print("\nLISTA DE MATERIALES\n")
    if not materiales:
        print("No existen materiales registrados")
        return
    print(f'{'Codigo'} {'Nombre'} {'Categoria'} {'Cantidad'} {'Estado'}\n')
    for m in materiales:
        print(f'{m["codigo"]} {m["nombre"]} {m["categoria"]} {m["cantidad"]} {m["estado"]}{" Bajo" if m["cantidad"]<=3 else ""}\n')

def buscar_material(materiales,codigo):
    for m in materiales:
        if m["codigo"]==codigo.upper():
            return m
    return None

def buscar_material_menu(materiales):
    print("-----------------")
    print("\nBUSCAR MATERIAL\n")
    codigo=input("Ingrese el codigo del material: ").upper()
    resultado=buscar_material(materiales,codigo)
    if resultado:
        print(f'Material encontrado:')
        for clave,valor in resultado.items():
            print(f' {clave}: {valor}')
    else:
        print("No se encontro ningun material")

def actualizar_cantidad(materiales):
    print("-----------------")
    print("\nACTUALIZAR CANTIDAD\n")
    codigo=input("Codigo del material: ").upper()
    material=buscar_material(materiales,codigo)
    if not material:
        print("No se econtro el material")
        return
    print(f'Material: {material["nombre"]}, Cantidad actual: {material["cantidad"]}')
    while True:
        nueva_cantidad=int(input("Cantidad: "))
        try:
            if nueva_cantidad>=0:
                break
            else:
                print("La cantidad debe ser mayor o igual a 0, intente de nuevo")
        except:
            print("Error, ingrese un numero entero")
    material["cantidad"]=nueva_cantidad
    material["estado"]="Disponible" if int(material["cantidad"]) !=0 else "Agotado"

def baja_cantidad_menu(materiales):
    print("-----------------")
    print("\nMATERIALES CON BAJA CANTIDAD (<= 3)\n")
    bajos=[m for m in materiales if m["cantidad"]<=3]
    if not bajos:
        print("No existen materiales con baja cantidad")
        return
    for m in bajos:
        print(f'{m["codigo"]} - {m["nombre"]} - {m["cantidad"]}')
    print(f'Total de materiales bajos: {len(bajos)}')

def resumen_categoria(materiales):
    print("-----------------")
    print("\nRESUMEN POR CATEGORIA\n")
    if not materiales:
        print("No existen materiales registrados")
        return
    conteo={}
    for m in materiales:
        cat=m["categoria"]
        if cat in conteo:
            conteo[cat]+=1
        else:
            conteo[cat]=1
    for categoria,total in sorted(conteo.items()):
        unidad="material" if total==1 else "materiales"
        print(f' {categoria}: {total} {unidad}')
    print(f'Existen {len(conteo)} categorias')

materiales=[]
def main():
    print("\n SISTEMA DE INVENTARIO")
    while True:
        mostrar_menu()
        opcion=input("Elija una opcion (1-7): ")
        if opcion=='1':
            registrar_material(materiales)
        elif opcion=='2':
            listar_materiales(materiales)
        elif opcion=='3':
            buscar_material_menu(materiales)
        elif opcion=='4':
            actualizar_cantidad(materiales)
        elif opcion=='5':
            baja_cantidad_menu(materiales)
        elif opcion=='6':
            resumen_categoria(materiales)
        elif opcion=='7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida")

main()