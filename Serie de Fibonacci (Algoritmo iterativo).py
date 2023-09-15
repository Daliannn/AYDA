print('\t\tSerie de Fibonacci')
#Recibimos la posicion del numero que el usuario quiere ver
n=int(input('\nIngrese la posicion del numero que desea ver: '))

#Declaramos una funcion que valla a realizar el procedimiento para calcular el numero
def Fibonacci(n):
    #Creamos un arreglo con espacio de memoria para que pueda imprimir los numeros
    Fibo=[None]*50
    #Ponemos como default los primeros dos numeros de la serie dado que ambos son 1 y es mas sencillo sacarlos para realizar las demas operaciones
    Fibo[0]=1
    Fibo[1]=1
    #Declaramos un for en un rango de 2(posicion incial que vamos a contar) y n+1(el numero que el usuario desea ver +1 debido a la especificacion del rango)
    for i in range (2,n+1):
        #Nos estara sumando los numeros desde los que ya pusimos
        Fibo[i] = Fibo[i-2]+Fibo[i-1]
        #Imprimira el numero de la posicion que el usuario marco
    print('El numero en la posicion de la serie es:', Fibo[n])

#Declaramos la funcion y le asignamos de parametro el numero que el usuario quiere
Fibonacci(n)