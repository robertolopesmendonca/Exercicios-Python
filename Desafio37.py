print("""
037) Escreva um programa que leia um número inteiro qualquer e peça ao usuário para
escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
""")
numero = int(input('Digite o número inteiro: '))
print('''Escolha a base para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal ''')
opção = int(input('Digite a sua opção: '))
if opção == 1:
    print(f'O número em binário será: {bin(numero)[2:]}')
elif opção == 2:
    print(f'O número em octal será: {oct(numero)[2:]}')
elif opção == 3:
    print(f'O número em hexadecimal será: {hex(numero)[2:]}')
else:
    print('Opção inválida, tente novamente')





