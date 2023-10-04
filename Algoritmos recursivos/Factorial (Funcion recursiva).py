def Factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        Fact=n*(Factorial(n-1))
        return Fact
        
print('\n   Factorial de un numero')
n=int(input('\nIngrese un numero: '))
Fact=Factorial(n)
print('El factorial del numero es:',Fact)
