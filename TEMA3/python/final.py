estudiantes = []

def mostrar_menu():
    print("-----------------\n")
    print("1.  Registrar estudiante")
    print("2.  Listar estudiantes")
    print("3.  Buscar estudiante por codigo")
    print("4.  Actualizar datos del estudiante")
    print("5.  Agregar materia")
    print("6.  Calcular promedio por materia")
    print("7.  Calcular asistencia por materia")
    print("8.  Mostrar aprobados y reprobados")
    print("9.  Mostrar resumen general")
    print("10. Salir\n")

def codigo_existe(codigo):
    for e in estudiantes:
        if e["codigo"] == codigo:
            return True
    return False

def buscar_estudiante(codigo):
    for e in estudiantes:
        if e["codigo"] == codigo.upper():
            return e
    return None

def seleccionar_materia(e):
    if not e["materias"]:
        print("El estudiante no tiene materias registradas")
        return None
    print(f"\nMaterias de {e['nombre']}:")
    for i, m in enumerate(e["materias"]):
        print(f"  {i+1}. {m['codigo_materia']} - {m['nombre_materia']}")
    while True:
        try:
            indice = int(input("Seleccione el numero de materia: ")) - 1
            if 0 <= indice < len(e["materias"]):
                return e["materias"][indice]
            else:
                print("Numero invalido")
        except:
            print("Ingrese un numero valido")

def ingresar_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100, intente de nuevo")
        except:
            print("Error, ingrese un numero valido")

def ingresar_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor a 0, intente de nuevo")
        except:
            print("Error, ingrese un numero entero")

def ingresar_entero_no_negativo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("El valor debe ser mayor o igual a 0, intente de nuevo")
        except:
            print("Error, ingrese un numero entero")

def calcular_promedio_materia(materia):
    promedio = (materia["nota1"] + materia["nota2"] + materia["examen_final"]) / 3
    return round(promedio, 2)

def calcular_porcentaje_asistencia(asistencia):
    return round((asistencia["clases_asistidas"] / asistencia["total_clases"]) * 100, 2)

def calcular_estado_materia(promedio, porcentaje_asistencia):
    if promedio >= 51 and porcentaje_asistencia >= 75:
        return "Aprobado"
    elif promedio < 51:
        return "Reprobado por nota"
    elif porcentaje_asistencia < 75:
        return "Reprobado por asistencia"
    else:
        return "Reprobado por nota y asistencia"

def calcular_promedio_general(estudiante):
    materias_con_promedio = [m for m in estudiante["materias"] if m["promedio"] is not None]
    if not materias_con_promedio:
        return 0
    total = sum(m["promedio"] for m in materias_con_promedio)
    return round(total / len(materias_con_promedio), 2)

def registrar_estudiante():
    print("-----------------")
    print("\nREGISTRAR ESTUDIANTE\n")
    while True:
        codigo = input("Codigo del estudiante (ej. E001): ").strip().upper()
        if not codigo:
            print("El codigo no puede estar vacio")
        elif codigo_existe(codigo):
            print(f"El codigo {codigo} ya esta registrado")
        else:
            break
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacio")
    while True:
        carrera = input("Carrera: ").strip()
        if carrera:
            break
        print("La carrera no puede estar vacia")
    semestre = ingresar_entero_positivo("Semestre: ")
    estudiante = {
        "codigo": codigo,
        "nombre": nombre,
        "carrera": carrera,
        "semestre": semestre,
        "estado_general": "Activo",
        "materias": []
    }
    estudiantes.append(estudiante)
    print(f"\nEstudiante {nombre} ({codigo}) registrado exitosamente") 

def listar_estudiantes():
    print("-----------------")
    print("\nLISTA DE ESTUDIANTES\n")
    if not estudiantes:
        print("No existen estudiantes registrados")
        return
    print(f"{'Codigo'} {'Nombre'}        {'Carrera'}     {'Semestre'} {'Estado'}\n")
    for e in estudiantes:
        print(f"{e['codigo']} {e['nombre']}     {e['carrera']}   {e['semestre']}    {e['estado_general']}")
    print(f"\nTotal de estudiantes: {len(estudiantes)}")

def buscar_estudiante_menu():
    print("-----------------")
    print("\nBUSCAR ESTUDIANTE\n")
    codigo = input("Ingrese el codigo del estudiante: ").upper()
    e = buscar_estudiante(codigo)
    if not e:
        print("No se encontro ningun estudiante con ese codigo")
        return
    print("\nEstudiante encontrado:")
    print(f"  Codigo        : {e['codigo']}")
    print(f"  Nombre        : {e['nombre']}")
    print(f"  Carrera       : {e['carrera']}")
    print(f"  Semestre      : {e['semestre']}")
    print(f"  Estado        : {e['estado_general']}")
    print(f"  Materias reg. : {len(e['materias'])}")
    if e["materias"]:
        print(f"  Prom. general : {calcular_promedio_general(e)}")
        print("\n  Detalle de materias:")
        for m in e["materias"]:
            asist = m["asistencia"]
            print(f"    [{m['codigo_materia']}] {m['nombre_materia']}")
            print(f"      Notas: {m['nota1']} / {m['nota2']} / {m['examen_final']}  |  Promedio: {m['promedio']}")
            print(f"      Asistencia: {asist['clases_asistidas']}/{asist['total_clases']} ({asist['porcentaje']}%)  |  Estado: {m['estado']}")

def actualizar_estudiante():
    print("-----------------")
    print("\nACTUALIZAR DATOS DEL ESTUDIANTE\n")
    codigo = input("Codigo del estudiante: ").upper()
    e = buscar_estudiante(codigo)
    if not e:
        print("No se encontro el estudiante")
        return
    print(f"\nEstudiante: {e['nombre']}")
    print("Que desea actualizar?")
    print("  1. Nombre")
    print("  2. Carrera")
    print("  3. Semestre")
    print("  4. Estado general (Activo/Inactivo)")
    opcion = input("Opcion: ")
    if opcion == "1":
        while True:
            nuevo = input("Nuevo nombre: ").strip()
            if nuevo:
                break
            print("El nombre no puede estar vacio")
        e["nombre"] = nuevo
        print("Nombre actualizado")
    elif opcion == "2":
        while True:
            nuevo = input("Nueva carrera: ").strip()
            if nuevo:
                break
            print("La carrera no puede estar vacia")
        e["carrera"] = nuevo
        print("Carrera actualizada")
    elif opcion == "3":
        e["semestre"] = ingresar_entero_positivo("Nuevo semestre: ")
        print("Semestre actualizado")
    elif opcion == "4":
        estado = input("Nuevo estado (Activo/Inactivo): ").strip().capitalize()
        if estado in ("Activo", "Inactivo"):
            e["estado_general"] = estado
            print("Estado actualizado")
        else:
            print("Estado invalido, debe ser Activo o Inactivo")
    else:
        print("Opcion invalida")

def agregar_materia():
    print("-----------------")
    print("\nAGREGAR MATERIA\n")
    codigo_est = input("Codigo del estudiante: ").upper()
    e = buscar_estudiante(codigo_est)
    if not e:
        print("No se encontro el estudiante")
        return
    if e["estado_general"] != "Activo":
        print("El estudiante se encuentra inactivo")
        return
    while True:
        codigo_mat = input("Codigo de la materia (ej. SIS111): ").upper()
        if not codigo_mat:
            print("El codigo no puede estar vacio")
            continue
        ya_existe = any(m["codigo_materia"] == codigo_mat for m in e["materias"])
        if ya_existe:
            print(f"La materia {codigo_mat} ya esta registrada para este estudiante")
        else:
            break
    while True:
        nombre_mat = input("Nombre de la materia: ").strip()
        if nombre_mat:
            break
        print("El nombre no puede estar vacio")
    materia = {
        "codigo_materia": codigo_mat,
        "nombre_materia": nombre_mat,
        "nota1": None,
        "nota2": None,
        "examen_final": None,
        "promedio": None,
        "estado": "Sin notas",
        "asistencia": {
            "clases_asistidas": 0,
            "total_clases": 0,
            "porcentaje": 0.0
        }
    }
    e["materias"].append(materia)
    print(f"\nMateria {nombre_mat} ({codigo_mat}) agregada exitosamente a {e['nombre']}")

def calcular_promedio_menu():
    print("-----------------")
    print("\nCALCULAR PROMEDIO POR MATERIA\n")
    codigo_est = input("Codigo del estudiante: ").upper()
    e = buscar_estudiante(codigo_est)
    if not e:
        print("No se encontro el estudiante")
        return
    if e["estado_general"] != "Activo":
        print("El estudiante se encuentra inactivo")
        return
    m = seleccionar_materia(e)
    if not m:
        return
    print(f"\nIngresando notas para: {m['nombre_materia']}")
    m["nota1"] = ingresar_nota("Nota 1 (0-100): ")
    m["nota2"] = ingresar_nota("Nota 2 (0-100): ")
    m["examen_final"] = ingresar_nota("Examen final (0-100): ")
    m["promedio"] = calcular_promedio_materia(m)
    asist = m["asistencia"]
    porcentaje = asist["porcentaje"] if asist["total_clases"] > 0 else 0
    m["estado"] = calcular_estado_materia(m["promedio"], porcentaje)
    print(f"\nPromedio calculado: {m['promedio']}")
    print(f"Estado de la materia: {m['estado']}")

def calcular_asistencia_menu():
    print("-----------------")
    print("\nCALCULAR ASISTENCIA POR MATERIA\n")
    codigo_est = input("Codigo del estudiante: ").upper()
    e = buscar_estudiante(codigo_est)
    if not e:
        print("No se encontro el estudiante")
        return
    if e["estado_general"] != "Activo":
        print("El estudiante se encuentra inactivo")
        return
    m = seleccionar_materia(e)
    if not m:
        return
    print(f"\nRegistrando asistencia para: {m['nombre_materia']}")
    total = ingresar_entero_positivo("Total de clases: ")
    while True:
        asistidas = ingresar_entero_no_negativo("Clases asistidas: ")
        if asistidas <= total:
            break
        print(f"Las clases asistidas no pueden superar el total ({total})")
    m["asistencia"]["total_clases"] = total
    m["asistencia"]["clases_asistidas"] = asistidas
    m["asistencia"]["porcentaje"] = calcular_porcentaje_asistencia(m["asistencia"])
    if m["promedio"] is not None:
        m["estado"] = calcular_estado_materia(m["promedio"], m["asistencia"]["porcentaje"])
    print(f"\nAsistencia registrada: {asistidas}/{total} ({m['asistencia']['porcentaje']}%)")
    print(f"Estado de la materia: {m['estado']}")

def mostrar_aprobados_reprobados():
    print("-----------------")
    print("\nAPROBADOS Y REPROBADOS\n")
    if not estudiantes:
        print("No existen estudiantes registrados")
        return
    for e in estudiantes:
        if not e["materias"]:
            continue
        aprobadas = [m for m in e["materias"] if m["estado"] == "Aprobado"]
        reprobadas = [m for m in e["materias"] if "Reprobado" in m["estado"]]
        print(f"Estudiante: {e['nombre']} ({e['codigo']})")
        print(f"  Aprobadas  ({len(aprobadas)}): {', '.join(m['nombre_materia'] for m in aprobadas) if aprobadas else 'Ninguna'}")
        print(f"  Reprobadas ({len(reprobadas)}): {', '.join(m['nombre_materia'] for m in reprobadas) if reprobadas else 'Ninguna'}")
        print(f"  Promedio general: {calcular_promedio_general(e)}\n")

def resumen_general():
    print("-----------------")
    print("\nRESUMEN GENERAL DEL SISTEMA\n")
    if not estudiantes:
        print("No existen estudiantes registrados")
        return
    total_estudiantes = len(estudiantes)
    activos = sum(1 for e in estudiantes if e["estado_general"] == "Activo")
    inactivos = total_estudiantes - activos
    total_aprobadas = 0
    total_reprobadas = 0
    total_sin_notas = 0
    promedios_validos = []
    for e in estudiantes:
        for m in e["materias"]:
            if m["estado"] == "Aprobado":
                total_aprobadas += 1
            elif "Reprobado" in m["estado"]:
                total_reprobadas += 1
            else:
                total_sin_notas += 1
        pg = calcular_promedio_general(e)
        if pg > 0:
            promedios_validos.append(pg)
    promedio_sistema = round(sum(promedios_validos) / len(promedios_validos), 2) if promedios_validos else 0
    print(f"  Total de estudiantes  : {total_estudiantes}")
    print(f"  Activos               : {activos}")
    print(f"  Inactivos             : {inactivos}")
    print(f"  Materias aprobadas    : {total_aprobadas}")
    print(f"  Materias reprobadas   : {total_reprobadas}")
    print(f"  Materias sin notas    : {total_sin_notas}")
    print(f"  Promedio general UCB  : {promedio_sistema}")

def main():
    print("\n SISTEMA DE CONTROL ACADEMICO")
    while True:
        mostrar_menu()
        opcion = input("Elija una opcion (1-10): ")
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            buscar_estudiante_menu()
        elif opcion == "4":
            actualizar_estudiante()
        elif opcion == "5":
            agregar_materia()
        elif opcion == "6":
            calcular_promedio_menu()
        elif opcion == "7":
            calcular_asistencia_menu()
        elif opcion == "8":
            mostrar_aprobados_reprobados()
        elif opcion == "9":
            resumen_general()
        elif opcion == "10":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida")

main()