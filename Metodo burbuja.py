def BubbleSort(array):
    #Dara el recorrido de las comparaciones
    for i in range (0,longitud):
        #Hara las comparaciones de los números
        for j in range (0,longitud-1):
            #Hacemos las comparaciones
            if array[j]>array[j+1]:
                #Guardamos el valor de la posicion j+1
                AUX=array[j]
                #Cambiamos de lugar el numero en la poisicion j
                array[j]=array[j+1]
                #Guardamos el siguiente valor que cambiaremos
                array[j+1]=AUX

print('\n\tMetodo de ordenamiento Bubble Sort')
#Solicitar al usuario la cantidad de números que desea ingresar
n=int(input('\n¿Cuantos números desea que contenga el arreglo?: '))
#Inicializamos un arreglo vacio que contendra los numeros
N=[0]*n
#Calculamos la longitud del arreglo
longitud=len(N)
# Utilizamos un ciclo for para pedir al usuario que ingrese los números y almacenarlos en el arreglo
for i in range(n):
    #La f en el enunciado sirve para que nos permita usar la i como numero al imprimir
    num=int(input(f'Ingrese el número en la posicion {i}: '))
    N[i]=num

print('\nArreglo antes de ser ordenado:')
print(N)

#Mandamos llamaar la funcion y le asignamos como parametro el arreglo
BubbleSort(N)
print('\nArreglo después de ser ordenado:')
print(N)