#Definimos una funcion que hara que el arreglo se ordene
def Burbuja(N, n):
    #Establecemos el caso base de que si la longitud del arreglo es uno, ya estara ordenado
    if n==1:
        #Regresamos el valor de el arreglo
        return N

    #Definimos una funcion auxiliar que hara todas las comparaciones a la vez que valla recorriendo todo el arreglo
    def burbuja(N, i, n):
        #usamos la variable i para verificar la posicion del arreglo en que esta
        #Si la posicion en la que se encuentra actualemente el algoritmo es igual a la longitud, quiere decir que estamos en la ultima posicion del arreglo
        #Por lo tanto no hay mas elementos que comprar y el codigo se detiene
        if i==n:
            #Se devuelve el arreglo sin hacer cambios
            return N

        #Aqui comparamos si el primer numero del arreglo es mayor que el que el siguiente
        if N[i]>N[i+1]:
            #Si la condicion anterior se cumple, creamos una variable auxiliar, donde guardamos el numero que es mayor
            AUX=N[i]
            #Ahora en la posicion donde estaba el numero anterior, lo cambiamos por el que es mas pequeño
            N[i]=N[i+1]
            #Y por ultimo el que guardamos en la variable euxiliar, lo ponemos en la posicion que comparamos al inicio
            N[i+1]=AUX
        
        #Llamamos a la funcion para hacer lo mismo con el numero en la siguiente posicion
        burbuja(N, i+1, n)

    #Llamamos a la funcion de nuevo para comparar todos los elementos
    burbuja(N, 0, n-1)

    #Regresamos el valor del arreglo ordenado, excepto la posicion del numero del caso base
    return Burbuja(N, n-1)

#Se define el arreglo a ordenar
N=[3,5,7,6,2]
#Creamos una variable que tendra el tamaño del arreglo
n=len(N)
#Imprimimos el arreglo sin ordenar
print("El arreglo original es:", N)
#Creamos una variable que contendra el resultado de la funcion
Ordenado=Burbuja(N,n)
#Imprimimos el arreglo ordenado que nos dio la funcion 
print("El areglo ordenado es:", Ordenado)