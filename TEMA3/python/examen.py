def validar_notas(notas):
    total=0
    for n in notas:
        total+=n
    return total

def validar_assist(assist):
    if assist>=75:
        return True
    else:
        return False

nombre=input('Ingrese el nombre del estudiante: ')
notas=[]
for i in range(3):
    while True:
        nota=int(input(f'Ingrese la nota {i+1}: '))
        if nota>=0 and nota<=100:
            notas.append(nota)
            break
        else:
            print('Ingrese un valor entre 0 y 100')
while True:
    assist=int(input(f'Ingrese el porcentaje de asistencia: '))
    if assist>=0 and assist<=100:
        break
    else:
        print('Ingrese un valor entre 0 y 100')

promedio=validar_notas(notas)/3
reporte=''
for x in notas:
    reporte+=str(x)+' '
print(f'Nombre del estudiante: {nombre}')
print(f'Las notas son: {reporte}y su promedio es {promedio}')
print(f'El porcentaje de asistencia es {assist}%')
if promedio>=51 and validar_assist(assist):
    print('Aprobado')
elif promedio<=51 and validar_assist(assist):
    print("Reprobado por notas")
elif promedio>=51 and not validar_assist(assist):
    print("Reprobado por asistencia")
else:
    print("Reprobado por notas y asistencia")