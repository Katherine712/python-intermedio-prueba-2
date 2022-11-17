#Ejercicio 1
a=[4,5,6,7,4,3]
b=[5,6,4,3,3,3]
c=[6,6,5,4,3,3]



def promedio_estudiante(a,b,c):
    return list(map(lambda x,y,z : round((x+y+z )/ 3,2) , a,b,c))

materias=['Historia','Lenguaje','Matemáticas','Física','Química','Biología']

def imprimir_notas(a,b,c,materias):
    promedios=promedio_estudiante(a,b,c)
    for i in range(len(materias)):
        print('{}: {}'.format(materias[i],promedios[i]))

notas=[]

for i in range(3):
    print(f'Estudiante {i+1}')
    notas_estudiante=[]
    for j in range(6):
        ingreso=float(input(f'Ingrese la nota para {materias[j]}: '))
        notas_estudiante.append(ingreso)
    notas.append(notas_estudiante)

    print("Promedio de notas por materia: ")

imprimir_notas(notas[0],notas[1],notas[2],materias)
