print('[-- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. --]\n')
from math import hypot
catetooposto = float(input('Digite o valor do cateto oposto: '))
catetoadjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(catetooposto, catetoadjacente)
print(f'O valor da hipotenusa é {hipotenusa:.2f}')

