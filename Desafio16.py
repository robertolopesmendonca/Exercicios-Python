print('[-- Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6. --]\n')
from math import trunc
numero = float(input('Digite um número: '))
print(f'O número digitado é {trunc(numero)}')


