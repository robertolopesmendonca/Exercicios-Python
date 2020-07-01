print('[-- Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. --]\n')
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f' O valor do seno de {angulo}graus é: {seno:.2f} ', end=' ')
print(f' O valor do cosseno de {angulo}graus é: {cosseno:.2f} ', end=' ')
print(f' O valor da tangente de {angulo}graus é: {tangente:.2f} ')

