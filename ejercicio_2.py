#Ejercicio 2

lista = int(input("Ingrese la cantidad de numeros \n"))
cont = 0
for i in range(2, lista + 1):
    primos = True
    for j in range(2,i):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(' ',i, end='')
        cont += 1
print('\nHay %u números primos.' % cont )
