def validar_notas(notas):
    total=0
    for n in notas:
        total+=n
    return total

def final():
    while True:
        examen_final=int(input('Ingrese la nota del examen final: '))
        if examen_final>=0 and examen_final<=100:
            return examen_final
        else:
            print('Ingrese un valor entre 0 y 100')

nombre=input('Ingrese el nombre del estudiante: ')
notas=[]
numero_parciales=int(input('Ingrese el numero de parciales: '))
for i in range(numero_parciales):
    while True:
        nota=int(input(f'Ingrese la nota {i+1}: '))
        if nota>=0 and nota<=100:
            notas.append(nota)
            break
        else:
            print('Ingrese un valor entre 0 y 100')
while True:
    porcentaje=int(input(f'Ingrese el porcentaje de los parciales (ej:60): '))
    if porcentaje>=0 and porcentaje<=100:
        porcentaje_examen_final=100-porcentaje
        break
    else:
        print('Ingrese un valor entre 0 y 100')
examen_final=final()
if examen_final==100:
    pass
elif examen_final==0:
    print("Debe dar otro examen final")
    examen_final=final()
    if examen_final==0:
        pass
else:
    if input("Desea dar otro final? (si/no): ")=="si":
        examen_final=final()
promedio_parciales=validar_notas(notas)/numero_parciales
nota_final=(promedio_parciales*porcentaje/100)+(examen_final*porcentaje_examen_final/100)
reporte=''
for x in notas:
    reporte+=str(x)+' '
print(f'\nNombre del estudiante: {nombre}')
print(f'Notas de los parciales: {reporte}')
print(f'Promedio de los parciales: {promedio_parciales:.2f}')
print(f'Nota del examen final: {examen_final}')
print("-----------")
print(f'Porcentajes finales: ({porcentaje}% parciales + {porcentaje_examen_final}% final)')
print(f'Nota final: {nota_final:.2f}')