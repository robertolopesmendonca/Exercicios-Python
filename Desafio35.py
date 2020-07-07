print("""
035) Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo.
""")
L1 = int(input('Digite do primeiro lado: '))
L2 = int(input('Digite o segundo lado: '))
L3 = int(input('Digite o terceiro lado: '))

if L1+L2>L3 and L1+L3>L2 and L2+L3>L1:
    print('É UM TRIÂNGULO') 
else:   
    print('NÃO É UM TRIÂNGULO')
