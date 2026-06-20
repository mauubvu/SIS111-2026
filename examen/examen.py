reservas = []

def mostrar_menu():
    print("\n===== SISTEMA RESERVAS =====")
    print("1. Registrar reserva")
    print("2. Listar reservas")
    print("3. Buscar reserva por código")
    print("4. Agregar servicio adicional")
    print("5. Calcular total de una reserva")
    print("6. Mostrar reservas activas")
    print("7. Mostrar resumen general")
    print("8. Salir")


def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))

            if valor >= 0:
                return valor
            else:
                print("Error: el número no puede ser 0 o negativo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


def buscar_reserva(reservas, codigo):
    for reserva in reservas:
        if reserva["codigo"] == codigo:
            return reserva

    return None


def registrar_reserva(reservas):
    print("\n--- Registrar reserva ---")

    codigo = input("Ingrese el código de la reserva: ").upper()

    if buscar_reserva(reservas, codigo) is not None:
        print("Error: ya existe un reserva con ese código.")
        return

    nombre_huesped = input("Ingrese el nombre de el huesped: ")
    ci = input("Ingrese el CI del huesped: ")
    noches=leer_entero("Ingrese el numero de noches: ")
    tipo=input("Ingrese el tipo de habitacion (Personal / Doble): ")
    precio_noche=leer_entero("Ingrese el numero de noches: ")
    reserva = {
        "codigo": codigo,
        "huesped": {
            "nombre": nombre_huesped,
            "ci": ci
        },
        "habitacion":{
            "tipo":tipo,
            "precio_noche":precio_noche,
        },
        "noches": noches,
        "servicios": {
        "desayuno": "No",
        "lavanderia":"No",
        "garaje":"No"
        },
        "subtotal":0,
        "descuento":0,
        "total":0,
        "estado":"Activa"
    }

    reservas.append(reserva)

    print("Reserva registrada correctamente.")


def listar_reservas(reservas):
    print("\n--- Lista de reservas ---")

    if len(reservas) == 0:
        print("No existen reservas registrados.")
        return
    for reserva in reservas:
        print("-----------------------------")
        print("Código:", reserva["codigo"])
        print("huesped:", reserva["huesped"]["nombre"])
        print("ci:", reserva["huesped"]["ci"])


def buscar_reserva_por_codigo(reservas):
    print("\n--- Buscar reserva ---")

    codigo = input("Ingrese el código del reserva: ").upper()

    reserva = buscar_reserva(reservas, codigo)

    if reserva is None:
        print("No se encontró un reserva con ese código.")
    else:
        print("Reserva encontrada:")
        print("Código:", reserva["codigo"])
        print("huesped:", reserva["huesped"]["nombre"])
        print("ci:", reserva["huesped"]["ci"])

def agregar_servicio(reservas):
    print("\n--- Agregar servicio adicional ---")

    codigo = input("Ingrese el código del reserva: ").upper()

    reserva = buscar_reserva(reservas, codigo)
    if reserva is None:
        print("No se encontró un reserva con ese código.")
        return
    print("Ingrese el servicio que desea (ej: 1): ")
    print("1. Desayuno")
    print("2. Lavanderia")
    print("3. Garaje")
    serv=leer_entero("Servicio: ")
    if serv==0:
        return
    if serv==1:
        desayuno="Si"
    if serv==2:
        lavanderia="Si"
    if serv==3:
        garaje="Si"
    reserva["servicios"] = {
        "desayuno": desayuno,
        "lavanderia":lavanderia,
        "garaje":garaje
    }

    print("Servicio añadido para la reserva: ",codigo)

def calcular_costo_servicios(reserva):
    total_serv=0
    if reserva["servicios"]["desayuno"]=="Si":
        total_serv+=60
    if reserva["servicios"]["lavanderia"]=="Si":
        total_serv+=30
    if reserva["servicios"]["garaje"]=="Si":
        total_serv+=20
    return total_serv

def calcular_descuento(subtotal):
    if subtotal>=1000:
        print("Descuento del 10%")
        return subtotal-(subtotal*0.1)
    elif subtotal>=500:
        print("Descuento del 5%")
        return subtotal-(subtotal*0.05)
    else:
        print("No tiene descuento")
        return subtotal
def calcular_habitacion(reserva):
    return reserva["habitacion"]["precio_noche"]*reserva["noches"]

def calcular_subtotal(reserva,suma_habit,suma_serv):
    reserva["subtotal"]=suma_habit+suma_serv
    return reserva["subtotal"]

def calcular_total(reservas):
    print("\n--- Calcular total de reserva ---")

    codigo = input("Ingrese el código del reserva: ").upper()

    reserva = buscar_reserva(reservas, codigo)
    if reserva is None:
        print("No se encontró un reserva con ese código.")
        return
    suma_serv=calcular_costo_servicios(reserva)
    suma_habit=calcular_habitacion(reserva)
    subtotal=calcular_subtotal(reserva,suma_habit,suma_serv)
    total=calcular_descuento(subtotal)
    print("El total de la reserva es ",total)
    reserva[total]=total

def ver_reservas_activas(reservas):
    print("\n--- Historial de reservas activas ---")
    if len(reservas) == 0:
        print("No existen reservas registradas.")
        return
    cont=0
    resumen = {}
    for reserva in reservas:
        if reserva["estado"]=="Activa":
            cont+=1
    for reserva in reservas:
        print("-----------------------------")
        print("Código:", reserva["codigo"])
        print("huesped:", reserva["huesped"]["nombre"])
        print("ci:", reserva["huesped"]["ci"])




def main():
    opcion = ""

    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_reserva(reservas)

        elif opcion == "2":
            listar_reservas(reservas)

        elif opcion == "3":
            buscar_reserva_por_codigo(reservas)

        elif opcion == "4":
            agregar_servicio(reservas)

        elif opcion == "5":
            calcular_costo_habitacion(reservas)

        elif opcion == "6":
            ver_reservas_activas(reservas)

        elif opcion == "8":
            print("Saliendo del sistema...")

        else:
            print("Opción inválida. Intente nuevamente.")

main()