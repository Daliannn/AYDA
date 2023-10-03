def Hanoi(n, A, B, AUX):
    if n==1:
        print(f'El disco {n} se moverá del {A} al {B}')
    else:
        Hanoi(n-1, A, AUX, B)
        print(f'El disco {n} se moverá del {A} al {B}')
        Hanoi(n-1, AUX, B, A)

print('\nTorres de Hanoi')
A='origen'
B='destino'
AUX='auxiliar'
n=int(input('\nIngrese el número de discos que tendrá su torre: '))
Hanoi(n, A, B, AUX)  