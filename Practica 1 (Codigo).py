def PedirDatos():
    n=int(input('\n   ¿De cuantos números será el arreglo?: '))
    N=[0]*n
    for i in range(n):
        num=int(input(f'   Ingrese el número en la posicion {i}: '))
        N[i]=num
    print('\n   Arreglo antes de ser ordenado:')
    print('   ',N)
    #Indicamos cual es el valor que nosotros returnaremos de esta funcion
    return N

def Mostrar(N):
    print('\n   Arreglo después de ser ordenado:')
    #Indicamos cual es el valor que nosotros returnaremos de esta funcion
    print('   ',N)
    
def BubbleSort(N):
    L=len(N)
    #Dara el recorrido de las comparaciones
    for i in range (0,L):
        #Hara las comparaciones de los números
        for j in range (0,L-1):
            #Hacemos las comparaciones
            if N[j]>N[j+1]:
                #Guardamos el valor de la posicion j+1
                AUX=N[j]
                #Cambiamos de lugar el numero en la poisicion j
                N[j]=N[j+1]
                #Guardamos el siguiente valor que cambiaremos
                N[j+1]=AUX
    #Indicamos cual es el valor que nosotros returnaremos de esta funcion
    return N
    
def BubbleSortOptimized(N):
    L=len(N)
    #Esta variable revisara cuando ya se han hecho comparaciones
    C=False
    T=L
    for i in range (0,L):
        if C==True:
            break
        for j in range (0,T-1):
            C==True
            if N[j]>N[j+1]:
                C==False
                AUX=N[j]
                N[j]=N[j+1]
                N[j+1]=AUX
        T=T-1
    return N

opc=0
while opc!=3:
    print('\n    Metodos de ordenamiento')
    print('''
    1. Bubble Sort
    2. Bubble Sort Optimized
    3. Salir''')
    print('\nSeleccione un número: ') 
    opc=int(input())
    if opc==1:
        print('\n-> Bubble Sort')
        #Igualamos nuestras funciones al arreglo que usaremos
        N=PedirDatos()
        #Nuestro arreglo sera igual al nuevo arreglo que nos returne la funcion
        N=BubbleSort(N)
        #Mandamos llamar nuestra funcion que mostrara los datos ya ordenados
        Mostrar(N)
    if opc==2:
        print('\n-> Bubble Sort Optimized')
        #Igualamos nuestras funciones al arreglo que usaremos
        N=PedirDatos()
        #Nuestro arreglo sera igual al nuevo arreglo que nos returne la funcion
        N=BubbleSortOptimized(N)
        #Mandamos llamar nuestra funcion que mostrara los datos ya ordenados
        Mostrar(N)
    if opc==3:
        print('\nHa salido del programa')