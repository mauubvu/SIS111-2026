def mostrar_menu():
    print("\n-----MENU DE OPERACIONES-----\n(1) Sumar\n(2) Restar\n(3) Multiplicar\n(4) Dividir\n(5) Salir")
 
def pedir_numeros():
    print("Presione ENTER para realizar la operacion")
    numeros = []
    while True:
        entrada = input("Ingresa un número: ")
        if entrada == "":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("Entrada inválida.")
    return numeros

def sumar(nums):
    return sum(nums)

def restar(nums):
    resultado = nums[0]
    for n in nums[1:]:
        resultado -= n
    return resultado

def multiplicar(nums):
    resultado = 1
    for n in nums:
        resultado *= n
    return resultado

def dividir(nums):
    resultado = nums[0]
    for n in nums[1:]:
        if n == 0:
            return "No definida, no se puede dividir entre 0."
        resultado /= n
    return resultado

while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")
    if opcion == "5":
        print("Saliendo del programa...")
        break
    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida.")
        continue
    numeros = pedir_numeros()
    if len(numeros) < 2:
        print("Debes ingresar al menos 2 números.")
        continue
    if opcion == "1": print(f"La suma es: {sumar(numeros)}")
    elif opcion == "2": print(f"La resta es: {restar(numeros)}")
    elif opcion == "3": print(f"La multiplicacion es: {multiplicar(numeros)}")
    elif opcion == "4": print(f"La division es: {dividir(numeros)}")