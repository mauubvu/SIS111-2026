pacientes = []

def mostrar_menu():
    print("\n===== SISTEMA VETERINARIO =====")
    print("1. Registrar paciente")
    print("2. Listar pacientes")
    print("3. Buscar paciente por código")
    print("4. Agregar consulta al historial")
    print("5. Ver historial de consultas")
    print("6. Contar pacientes por especie")
    print("7. Salir")


def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))

            if valor >= 0:
                return valor
            else:
                print("Error: el número no puede ser negativo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


def buscar_paciente(pacientes, codigo):
    for paciente in pacientes:
        if paciente["codigo"] == codigo:
            return paciente

    return None


def registrar_paciente(pacientes):
    print("\n--- Registrar paciente ---")

    codigo = input("Ingrese el código del paciente: ").upper()

    if buscar_paciente(pacientes, codigo) is not None:
        print("Error: ya existe un paciente con ese código.")
        return

    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie: ").capitalize()
    edad = leer_entero("Ingrese la edad de la mascota: ")

    nombre_dueno = input("Ingrese el nombre del dueño: ")
    telefono_dueno = input("Ingrese el teléfono del dueño: ")

    paciente = {
        "codigo": codigo,
        "mascota": {
            "nombre": nombre_mascota,
            "especie": especie,
            "edad": edad
        },
        "dueno": {
            "nombre": nombre_dueno,
            "telefono": telefono_dueno
        },
        "historial_consultas": {}
    }

    pacientes.append(paciente)

    print("Paciente registrado correctamente.")


def listar_pacientes(pacientes):
    print("\n--- Lista de pacientes ---")

    if len(pacientes) == 0:
        print("No existen pacientes registrados.")
        return

    for paciente in pacientes:
        print("-----------------------------")
        print("Código:", paciente["codigo"])
        print("Mascota:", paciente["mascota"]["nombre"])
        print("Especie:", paciente["mascota"]["especie"])
        print("Edad:", paciente["mascota"]["edad"])
        print("Dueño:", paciente["dueno"]["nombre"])
        print("Teléfono:", paciente["dueno"]["telefono"])


def buscar_paciente_por_codigo(pacientes):
    print("\n--- Buscar paciente ---")

    codigo = input("Ingrese el código del paciente: ").upper()

    paciente = buscar_paciente(pacientes, codigo)

    if paciente is None:
        print("No se encontró un paciente con ese código.")
    else:
        print("Paciente encontrado:")
        print("Código:", paciente["codigo"])
        print("Mascota:", paciente["mascota"]["nombre"])
        print("Especie:", paciente["mascota"]["especie"])
        print("Edad:", paciente["mascota"]["edad"])
        print("Dueño:", paciente["dueno"]["nombre"])
        print("Teléfono:", paciente["dueno"]["telefono"])


def agregar_consulta(pacientes):
    print("\n--- Agregar consulta al historial ---")

    codigo = input("Ingrese el código del paciente: ").upper()

    paciente = buscar_paciente(pacientes, codigo)

    if paciente is None:
        print("No se encontró un paciente con ese código.")
        return

    numero_consulta = len(paciente["historial_consultas"]) + 1
    codigo_consulta = "C" + str(numero_consulta).zfill(3)

    fecha = input("Ingrese la fecha de consulta: ")
    motivo = input("Ingrese el motivo de consulta: ")
    diagnostico = input("Ingrese el diagnóstico: ")
    tratamiento = input("Ingrese el tratamiento: ")

    paciente["historial_consultas"][codigo_consulta] = {
        "fecha": fecha,
        "motivo": motivo,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento
    }

    print("Consulta registrada correctamente con código:", codigo_consulta)


def ver_historial_consultas(pacientes):
    print("\n--- Historial de consultas ---")

    codigo = input("Ingrese el código del paciente: ").upper()

    paciente = buscar_paciente(pacientes, codigo)

    if paciente is None:
        print("No se encontró un paciente con ese código.")
        return

    historial = paciente["historial_consultas"]

    if len(historial) == 0:
        print("El paciente no tiene consultas registradas.")
        return

    print("Historial de:", paciente["mascota"]["nombre"])

    for codigo_consulta, consulta in historial.items():
        print("-----------------------------")
        print("Código consulta:", codigo_consulta)
        print("Fecha:", consulta["fecha"])
        print("Motivo:", consulta["motivo"])
        print("Diagnóstico:", consulta["diagnostico"])
        print("Tratamiento:", consulta["tratamiento"])


def contar_pacientes_por_especie(pacientes):
    print("\n--- Contar pacientes por especie ---")

    if len(pacientes) == 0:
        print("No existen pacientes registrados.")
        return

    resumen = {}

    for paciente in pacientes:
        especie = paciente["mascota"]["especie"]

        if especie in resumen:
            resumen[especie] += 1
        else:
            resumen[especie] = 1

    print("Resumen por especie:")

    for especie, cantidad in resumen.items():
        if cantidad == 1:
            print(especie + ":", cantidad, "paciente")
        else:
            print(especie + ":", cantidad, "pacientes")


def main():
    opcion = ""

    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_paciente(pacientes)

        elif opcion == "2":
            listar_pacientes(pacientes)

        elif opcion == "3":
            buscar_paciente_por_codigo(pacientes)

        elif opcion == "4":
            agregar_consulta(pacientes)

        elif opcion == "5":
            ver_historial_consultas(pacientes)

        elif opcion == "6":
            contar_pacientes_por_especie(pacientes)

        elif opcion == "7":
            print("Saliendo del sistema...")

        else:
            print("Opción inválida. Intente nuevamente.")

main()