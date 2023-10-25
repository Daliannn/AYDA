#Libreria para el tiempo
import time
#Libreria para poner datos aleatorios
import random
#Libreria para crear la grafica
import matplotlib.pyplot as plt

#Funcion que genera el tamaño de el arreglo
def Tam():
    #Genera el tamaño aleatoriamente
    t=random.randrange(5,15)
    return t

#Funcion que genera el arreglo
def GenA(n):
    #Llena el arreglo aleatoriamente
    A=[random.randrange(1,20) for i in range(n)]
    return A

#Funcion que genera una lista donde se guardan los 100 arreglos  
def Arreglos():
    #Genera la lista vacia
    a=[]
    #Hace que nos genere tantos arreglos como queramos
    for i in range(100):
        #Va agregando a la lista cada arreglo generado
        a.append(GenA(Tam()))
    return a
    
def Media(x):
    #Usa sum, nos ayuda a sumar todos los elementos de un arreglo
    #La doble linea redondea la division a un numero entero
    #Len calcula la longitud del arreglo
    m=sum(x)//len(x)
    return m

def QuickSort(x):
    #Se define el caso base, que dice que cuando un arreglo solo tenga un elemento pues ya estara ordenado
    if len(x)<=1:
        return x
    #Se define el pivote, que ya se calculo anteriormente en la funcion media
    m=Media(x)
    p=m
    #Se definen los arreglos donde clasificaremos los elementos luego de las comparaciones
    izq=[]
    der=[]
    igual=[]
    #Cilco que asigna cada valor del arreglo original a los arreglos resultantes de la divison
    for e in x:
        if e<p:
            izq.append(e)
        elif e>p:
            der.append(e)
        else:
            #Se crea tambien un arreglo igual para el caso en que haya numeros repetidos
            #O iguales al pivote
            igual.append(e)
    #Se definen los dos arreglos en una variable al momento de volverlas a llamar
    izq_ordenado=QuickSort(izq)   
    der_ordenado=QuickSort(der) 
    #Se regresan los arreglos resultantes de las divisiones del arreglo original  
    return izq_ordenado + igual + der_ordenado

#Funcion para calcular el tiempo de ejecucion de una funcion
def TiempoEjecucion(func, *args):
    #Tomamos el tiempo de ejecucion incial
    inicio=time.time()
    #Llama a la funcion de la que queremos el tiempo de ejecucion
    func(*args)
    #Tomamos el tiempo de ejecucion final
    fin=time.time()
    #Calculamos el tiempo de ejecucion real
    TiempoReal=fin-inicio
    #Regresamos como resultado de la funcion el tiempo de ejecucion
    return TiempoReal 

print("\n\t\t\tQuickSort")
n=Tam()
#Lista que contiene cada arreglo
x=Arreglos()

#Imprime cada elemento de la lista
print("\n-> Arreglos generados aleatoriamente")
Tamaños=[]
for i in x:
    print(f"   El arreglo {x.index(i)} es: {i}")
    Tamaños.append(len(i))

#Manda cada arreglo a la funcion QuickSort para que ordene de uno por uno 
print("\n-> Arreglos ordenados")
ArregloOrdenado=[]
for i in x:
    m=Media(i)
    #Cada arreglo ordenado lo guarda en una variable
    ordenado=QuickSort(i)
    ArregloOrdenado.append(ordenado)
    #Imprime cada arreglo uno por uno ordenado
    print(f"   El arreglo {x.index(i)} ordenado es: {ordenado}")

#Manda cada ejecucion de la funcion QuickSort    
print("\n-> Tiempos de ejecucion") 
Tiempos=[]
Resultados=[]
for i in x:
    #Cada tiempo de ejecucion lo guardaremos en la variable tiempo
    Tiempo=TiempoEjecucion(QuickSort,i)
    #Imprime el tiempo de ejecucion de cada arreglo generado
    print(f"   Tiempo tardado en ordenar el arreglo {x.index(i)}: {Tiempo}")
    #Se guarda cada tiempo de ejecucuion en un arreglo
    Tiempos.append(Tiempo)
    Resultados.append((Tiempo, i, QuickSort(i)))

Resultados = sorted(Resultados, key=lambda x: x[0])

print("\n-> Arreglos con menor tiempo de ejecución")
for i, (tiempo, arreglo_original, arreglo_ordenado) in enumerate(Resultados[:3], 1):
    print(f"   El arreglo original {x.index(arreglo_original)} es: {arreglo_original}")
    print(f"   El arreglo ordenado {x.index(arreglo_original)} es: {arreglo_ordenado}")

print("\n-> Arreglos con mayor tiempo de ejecución")
for i, (tiempo, arreglo_original, arreglo_ordenado) in enumerate(Resultados[-3:], 1):
    print(f"   El arreglo original {x.index(arreglo_original)} es: {arreglo_original}")
    print(f"   El arreglo ordenado {x.index(arreglo_original)} es: {arreglo_ordenado}")

plt.xlabel('Tamaño del arreglo (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Gráfico del algoritmo QuickSort')

# Usamos n como el tamaño del arreglo en el eje X y Tiempos en el eje Y
plt.plot(Tiempos)
plt.show()
