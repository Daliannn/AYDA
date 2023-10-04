def Fibonacci(n):
    Fibo=[None]*50
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        Fibo=Fibonacci(n-2)+Fibonacci(n-1)
        return Fibo

print('\t\tSerie de Fibonacci')
n=int(input('\nIngrese la posicion del numero que desea ver: '))
Fibo=Fibonacci(n)
print('El numero en la posicion que ingreso es:',Fibo)
