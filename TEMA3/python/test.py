# ============================================================
#  GESTIÓN DE INVENTARIO - LABORATORIO DE COMPUTACIÓN
#  Autor: Mau Márquez
# ============================================================

# -----------------------------------------------------------
# DATOS INICIALES (materiales de ejemplo para probar)
# -----------------------------------------------------------
materiales = [
    {"codigo": "M001", "nombre": "Teclado",        "categoria": "Periférico", "cantidad": 15, "estado": "Disponible"},
    {"codigo": "M002", "nombre": "Mouse",           "categoria": "Periférico", "cantidad": 2,  "estado": "Disponible"},
    {"codigo": "M003", "nombre": "Monitor 24\"",    "categoria": "Equipo",     "cantidad": 8,  "estado": "Disponible"},
    {"codigo": "M004", "nombre": "Cable HDMI",      "categoria": "Cableado",   "cantidad": 3,  "estado": "Disponible"},
    {"codigo": "M005", "nombre": "Laptop",          "categoria": "Equipo",     "cantidad": 5,  "estado": "Disponible"},
    {"codigo": "M006", "nombre": "Proyector",       "categoria": "Equipo",     "cantidad": 1,  "estado": "Disponible"},
]

LIMITE_BAJA_CANTIDAD = 3

# -----------------------------------------------------------
# FUNCIONES AUXILIARES
# -----------------------------------------------------------

def separador(caracter="─", largo=50):
    print(caracter * largo)

def codigo_existe(materiales, codigo):
    """Retorna True si el código ya está registrado."""
    for m in materiales:
        if m["codigo"] == codigo:
            return True
    return False

# -----------------------------------------------------------
# FUNCIÓN 1 – MENÚ PRINCIPAL
# -----------------------------------------------------------

def mostrar_menu():
    separador("═")
    print("   INVENTARIO - LABORATORIO DE COMPUTACIÓN")
    separador("═")
    print("  1. Registrar material")
    print("  2. Listar materiales")
    print("  3. Buscar material por código")
    print("  4. Actualizar cantidad de un material")
    print("  5. Mostrar materiales con baja cantidad")
    print("  6. Mostrar resumen por categoría")
    print("  7. Salir")
    separador()

# -----------------------------------------------------------
# FUNCIÓN 2 – REGISTRAR MATERIAL
# -----------------------------------------------------------

def registrar_material(materiales):
    print("\n[ REGISTRAR MATERIAL ]")
    separador()

    # Código
    while True:
        codigo = input("Código (ej. M007): ").strip().upper()
        if not codigo:
            print("  ⚠ El código no puede estar vacío.")
        elif codigo_existe(materiales, codigo):
            print(f"  ⚠ El código '{codigo}' ya existe. Usa uno diferente.")
        else:
            break

    # Nombre
    while True:
        nombre = input("Nombre del material: ").strip()
        if nombre:
            break
        print("  ⚠ El nombre no puede estar vacío.")

    # Categoría
    categorias_validas = ["Periférico", "Equipo", "Cableado", "Software", "Otro"]
    print(f"  Categorías disponibles: {', '.join(categorias_validas)}")
    while True:
        categoria = input("Categoría: ").strip().capitalize()
        if categoria in categorias_validas:
            break
        print(f"  ⚠ Categoría inválida. Elige entre: {', '.join(categorias_validas)}")

    # Cantidad
    while True:
        cantidad_str = input("Cantidad: ").strip()
        if cantidad_str.isdigit():
            cantidad = int(cantidad_str)
            break
        print("  ⚠ La cantidad debe ser un número entero ≥ 0.")

    # Estado
    estados_validos = ["Disponible", "En uso", "En reparación", "Dado de baja"]
    print(f"  Estados disponibles: {', '.join(estados_validos)}")
    while True:
        estado = input("Estado: ").strip().capitalize()
        # Aceptar coincidencia parcial simple
        coincidencias = [e for e in estados_validos if e.lower().startswith(estado.lower())]
        if len(coincidencias) == 1:
            estado = coincidencias[0]
            break
        elif estado in estados_validos:
            break
        print(f"  ⚠ Estado inválido. Elige entre: {', '.join(estados_validos)}")

    nuevo = {
        "codigo":    codigo,
        "nombre":    nombre,
        "categoria": categoria,
        "cantidad":  cantidad,
        "estado":    estado,
    }
    materiales.append(nuevo)
    print(f"\n  ✔ Material '{nombre}' registrado exitosamente con código {codigo}.")

# -----------------------------------------------------------
# FUNCIÓN 3 – LISTAR MATERIALES
# -----------------------------------------------------------

def listar_materiales(materiales):
    print("\n[ LISTADO DE MATERIALES ]")
    separador()

    if not materiales:
        print("  No hay materiales registrados.")
        return

    # Encabezado de tabla
    print(f"  {'Código':<8} {'Nombre':<22} {'Categoría':<12} {'Cant':>5}  {'Estado'}")
    separador()

    for m in materiales:
        alerta = " ⚠" if m["cantidad"] <= LIMITE_BAJA_CANTIDAD else ""
        print(f"  {m['codigo']:<8} {m['nombre']:<22} {m['categoria']:<12} {m['cantidad']:>5}  {m['estado']}{alerta}")

    separador()
    print(f"  Total de materiales registrados: {len(materiales)}")

# -----------------------------------------------------------
# FUNCIÓN 4 – BUSCAR MATERIAL POR CÓDIGO
# -----------------------------------------------------------

def buscar_material(materiales, codigo):
    """Retorna el material si lo encuentra, None si no."""
    codigo = codigo.strip().upper()
    for m in materiales:
        if m["codigo"] == codigo:
            return m
    return None

def buscar_material_menu(materiales):
    print("\n[ BUSCAR MATERIAL ]")
    separador()
    codigo = input("Ingresa el código del material: ").strip()
    resultado = buscar_material(materiales, codigo)

    if resultado:
        print(f"\n  ✔ Material encontrado:")
        separador()
        for clave, valor in resultado.items():
            print(f"    {clave.capitalize():<12}: {valor}")
    else:
        print(f"  ✘ No se encontró ningún material con código '{codigo.upper()}'.")

# -----------------------------------------------------------
# FUNCIÓN 5 – ACTUALIZAR CANTIDAD
# -----------------------------------------------------------

def actualizar_cantidad(materiales):
    print("\n[ ACTUALIZAR CANTIDAD ]")
    separador()
    codigo = input("Código del material a actualizar: ").strip()
    material = buscar_material(materiales, codigo)

    if not material:
        print(f"  ✘ No se encontró el código '{codigo.upper()}'.")
        return

    print(f"  Material: {material['nombre']}  |  Cantidad actual: {material['cantidad']}")

    while True:
        nueva_str = input("Nueva cantidad: ").strip()
        if nueva_str.isdigit():
            nueva = int(nueva_str)
            break
        print("  ⚠ Ingresa un número entero ≥ 0.")

    material["cantidad"] = nueva
    print(f"  ✔ Cantidad actualizada a {nueva} para '{material['nombre']}'.")

# -----------------------------------------------------------
# FUNCIÓN 6 – MATERIALES CON BAJA CANTIDAD
# -----------------------------------------------------------

def mostrar_baja_cantidad(materiales):
    print(f"\n[ MATERIALES CON BAJA CANTIDAD (≤ {LIMITE_BAJA_CANTIDAD}) ]")
    separador()

    bajos = [m for m in materiales if m["cantidad"] <= LIMITE_BAJA_CANTIDAD]

    if not bajos:
        print("  ✔ No hay materiales con baja cantidad.")
        return

    for m in bajos:
        print(f"  {m['codigo']} - {m['nombre']} - Cantidad: {m['cantidad']}")

    print(f"\n  Total en alerta: {len(bajos)} material(es).")

# -----------------------------------------------------------
# FUNCIÓN 7 – RESUMEN POR CATEGORÍA
# -----------------------------------------------------------

def resumen_por_categoria(materiales):
    print("\n[ RESUMEN POR CATEGORÍA ]")
    separador()

    if not materiales:
        print("  No hay materiales registrados.")
        return

    conteo = {}
    for m in materiales:
        cat = m["categoria"]
        if cat in conteo:
            conteo[cat] += 1
        else:
            conteo[cat] = 1

    for categoria, total in sorted(conteo.items()):
        unidad = "material" if total == 1 else "materiales"
        print(f"  {categoria:<15}: {total} {unidad}")

    separador()
    print(f"  Categorías distintas: {len(conteo)}")

# -----------------------------------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------------------------------

def main():
    print("\n  Bienvenido al sistema de inventario de laboratorio.\n")

    while True:
        mostrar_menu()
        opcion = input("  Elige una opción (1-7): ").strip()

        if opcion == "1":
            registrar_material(materiales)

        elif opcion == "2":
            listar_materiales(materiales)

        elif opcion == "3":
            buscar_material_menu(materiales)

        elif opcion == "4":
            actualizar_cantidad(materiales)

        elif opcion == "5":
            mostrar_baja_cantidad(materiales)

        elif opcion == "6":
            resumen_por_categoria(materiales)

        elif opcion == "7":
            print("\n  Saliendo del sistema... ¡Hasta luego!\n")
            break

        else:
            print("\n  ⚠ Opción inválida. Ingresa un número del 1 al 7.")

        input("\n  [Presiona Enter para continuar...]")

# -----------------------------------------------------------
if __name__ == "__main__":
    main()