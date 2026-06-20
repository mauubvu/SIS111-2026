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

        suma_serv=calcular_costo_servicios(reserva)
    reserva["subtotal"]=reserva["habitacion"]["precio_noche"]*reserva["noches"]+suma_serv
    subtotal=reserva["subtotal"]
    calcular_descuento(subtotal)