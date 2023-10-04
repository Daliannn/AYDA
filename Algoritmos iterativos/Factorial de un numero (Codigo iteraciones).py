print('Factorial de un numero')
#Leemos el numero del que vamos a sacar el factorial
n=int(input('\nIngrese un numero: '))

#Creamos una funcion para calcular el factorial
def Factorial(n):
    #Inicializamos la variable que va a hacer la multiplicacion
    Fac=1
    #Definimos el for que ira de 1 hasta n porque el factorial no cuenta el 0
    for i in range(1,n+1):
        #Se crea la variable que guardara las multiplicaciones hasta llegar al numero
        Fac=Fac*i
    print('El factorial del numero es:', Fac)

#Se declara la funcion y se le da n como parametros 
Factorial(n)
