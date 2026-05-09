def ingresarDatos():
    datos = []
    for i in range(int(input("Ingrese el numero de trabajadores de la empresa: "))):
        print(f"\nTrabajador número {i+1}")
        while True:
            try:
                ci=int(input("Ingrese su CI: "))
                if type(ci)==int:
                    break
            except ValueError:
                print("Error, ingrese un CI valido")
        while True:
            sueldo = float(input("Ingrese su sueldo: "))
            if sueldo > 5000:
                break
            else:
                print("El sueldo debe ser mayor a 5000, intente nuevamente.")
        bono_loc=sueldo*0.14
        bono_ali=sueldo*0.09
        print(f'\nBono de locomocion: {bono_loc:.2f}Bs.')
        print(f'Bono de alimentacion: {bono_ali:.2f}Bs.')
        datos.append({
            "ci": ci,
            "sueldo": sueldo,
            "bono_locomocion": bono_loc,
            "bono_alimentacion": bono_ali
        })
    return datos

def mostrarResumen(datos):
    print("\n\nResumen de Bonos")
    total_bono_ali=0
    total_bono_loc=0
    for d in datos:
        total_bono_loc+=d["bono_locomocion"]
        total_bono_ali+=d["bono_alimentacion"]
    print(f"Se gasto un total de {total_bono_loc:.2f}Bs. por concepto de locomocion")
    print(f"Se gasto un total de {total_bono_ali:.2f}Bs. en conceptos de alimentacion")


def main():
    print("\n\n--- Empresa Bonos ---")
    datos=ingresarDatos()
    mostrarResumen(datos)

main()