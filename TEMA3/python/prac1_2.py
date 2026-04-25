def ingresarDatos():
    n = int(input("\nIngrese el numero de asignaturas: "))
    datos = []
    for i in range(n):
        print(f"\nAsignatura {i+1}")
        asignatura = input("Ingrese el nombre de la asignatura: ")
        porcentaje_examen = float(input("Ingrese el porcentaje de exámenes (ej: 80): ")) / 100
        porcentaje_practicas = 1 - porcentaje_examen
        numero_examenes = int(input("Ingrese el numero de examenes: "))
        examenes = []
        for j in range(numero_examenes):
            nota = float(input(f"Ingrese la nota del examen {j+1}: "))
            examenes.append(nota)
        numero_practicas = int(input("Ingrese el numero de practicas: "))
        practicas = []
        for k in range(numero_practicas):
            nota = float(input(f"Ingrese la nota de la practica {k+1}: "))
            practicas.append(nota)
        datos.append({
            "asignatura": asignatura,
            "examenes": examenes,
            "practicas": practicas,
            "porcentaje_examen": porcentaje_examen,
            "porcentaje_practicas": porcentaje_practicas
        })
    return datos

def calcular():
    datos = ingresarDatos()
    promedios = []
    for dato in datos:
        prom_examenes = sum(dato.get("examenes")) / len(dato.get("examenes"))
        prom_practicas = sum(dato.get("practicas")) / len(dato.get("practicas")) if dato.get("practicas") else 0
        promedio = prom_examenes * dato.get("porcentaje_examen") + prom_practicas * dato.get("porcentaje_practicas")
        promedios.append({
            "asignatura": dato.get("asignatura"),
            "prom_examenes": prom_examenes,
            "prom_practicas": prom_practicas,
            "promedio": promedio
        })
    return promedios

def mostrarPromedios():
    promedios = calcular()
    suma = 0
    print("\n\nPromedio de Notas")
    for p in promedios:
        print(f"\n{p.get('asignatura')}:")
        print(f"Promedio exámenes: {p.get('prom_examenes'):.2f}")
        print(f"Promedio prácticas: {p.get('prom_practicas'):.2f}")
        print(f"Nota final: {p.get('promedio'):.2f}")
        suma += p.get("promedio")
    promedio_general = suma / len(promedios)
    print(f"\nPromedio general: {promedio_general:.2f}")

mostrarPromedios()  