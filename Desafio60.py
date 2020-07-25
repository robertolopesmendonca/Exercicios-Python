print("""
060) Faça um programa que leia um número qualquer
e mostre o seu fatorial.
""")
#from math import factorial
#n = int(input('Digite um número: '))
#fatorial = factorial(n)
#print(fatorial)

### Outro método, sem uso do módulo math !!

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando  {}! = '.format(n), end='')
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print (' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

