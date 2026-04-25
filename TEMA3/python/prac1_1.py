def ingresarDatos():
    asignaturas=("Programacion","Algebra Lineal","Ing de Sistemas")
    datos = []
    for asignatura in asignaturas:
        print(f"Ingrese la nota de examen de {asignatura}")
        examen = float(input())
        print(f"Ingrese la nota de practica 1  de {asignatura}")
        practica1 = float(input())
        print(f"Ingrese la nota de practica 2 de {asignatura}")
        practica2 = float(input())
        datos.append({"asignatura":asignatura,"examen":examen,
                      "practica1":practica1,"practica2":practica2})
    return datos

def calcular():
    datos = ingresarDatos()
    promedios = []
    for dato in datos:
        promedio_practicas = (dato.get("practica1") + dato.get("practica2")) / 2
        if dato.get("asignatura") == "Programacion":
            promedio = dato.get("examen") * 0.9 + promedio_practicas * 0.1
        elif dato.get("asignatura") == "Algebra Lineal":
            promedio = dato.get("examen") * 0.8 + promedio_practicas * 0.2
        elif dato.get("asignatura") == "Ing de Sistemas":
            promedio = dato.get("examen") * 0.85 + promedio_practicas * 0.15
        promedios.append({
            "asignatura": dato.get("asignatura"),
            "promedio": promedio
        })
    return promedios

def mostrarPromedios():
    promedios = calcular()
    suma = 0
    for p in promedios:
        print(f"{p['asignatura']}: {p['promedio']:.2f}")
        suma += p["promedio"]
    promedio_general = suma / len(promedios)
    print(f"\nPromedio general: {promedio_general:.2f}")

mostrarPromedios()