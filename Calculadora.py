#Libreria para el tiempo
import time

# Entrada de datos y definicion de variables
a=float(input('\nIngrese su primer número: '))
b=float(input('Ingrese su segundo numero: '))

opc=0
inicio=time.time()
while opc!=5:
    print('''\nCalculadora básica
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    print('\nSeleccione el número de la operacion que desea realizar: ')
    opc=int(input()) #Lee la variable de opc
    if opc==1:
        suma=a+b
        print('\nEl resultado de la suma es:', suma)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('Tiempo tardado en ejecutar la suma: ',tiempo_ejecutado)
    if opc==2:
        resta=a-b
        print('\nEl resultado de la resta es:', resta)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('Tiempo tardado en ejecutar la resta: ',tiempo_ejecutado)
    if opc==3:
        multiplicacion=a*b
        print('\nEl resultado de la multiplicación es:', multiplicacion)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('Tiempo tardado en ejecutar la multiplicación: ',tiempo_ejecutado)
    if opc==4:
        division=a/b
        print('\nEl resultado de la division es:', division)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('Tiempo tardado en ejecutar la división: ',tiempo_ejecutado)
    if opc==5:
        print('\nHa salido del programa')




