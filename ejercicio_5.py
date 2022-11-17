#Ejercicio 5
def mayusculas(*args):
    for elementos in args:
        print(elementos.upper())

colores=[]

cond=True

print('Ingrese la palabra \'salir\' para dejar de ingresar colores')
while cond:
    color=input('Ingrese su color favorito: ')
    if color.lower()=='salir':
        print('Fin del programa')
        cond=False
    else:
        colores.append(color)

mayusculas(*colores)
print()
