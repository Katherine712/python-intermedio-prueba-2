#Ejercicio 3

from functools import reduce


def suma(a,b):
    return a+b
def multiplicacion(a,b):
    return a*b
def resta (a,b):
    return a-b
def division (a,b):
    return a/b
def exponente(a,b):
    return a**b
def raiz(a,b):
    return a**(1/b)
def Calculadora(lista):

    print('Suma: {}'.format(reduce(suma,lista)))
    print('Resta: {}'.format(reduce(resta,lista)))
    print('Multiplicación: {}'.format(reduce(multiplicacion, lista)))
    print('División: {}'.format(reduce(division, lista)))
    print('Exponente: {}'.format(reduce(exponente, lista)))
    print('Raiz cuadrada: {}'.format(reduce(raiz, lista)))




lista=input('Ingrese los numeros separados por un espacio: ').strip()
datos=[]
for elementos in lista.split(' '):
    datos.append(int(elementos))
Calculadora(datos)

print()
