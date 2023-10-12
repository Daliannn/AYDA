def Burbuja1(Burbuja, n):
    for i in range (0,n):
        for j in range (0,n-1):
            if(Burbuja[j]>Burbuja[j+1]):
                AUX=Burbuja[j]
                Burbuja[j]=Burbuja[j+1]
                Burbuja[j+1]=AUX
    return Burbuja

Burbuja=[3,5,7,6,2]
print("El algoritmos original es:", Burbuja)
n=len(Burbuja)
print("El algoritmos ordenado es:", Burbuja1(Burbuja,n))
