print("""
052) Faça um programa que leia um número inteiro e diga se
ele é ou não um número primo.
""")
total = 0
numero = int(input('Digite o número: '))
for contador in range (1, numero + 1):
    if numero % contador == 0:
        total += 1
print(f'O número {numero} foi divisível {total} vezes')
if total == 2:
    print(f'O número {numero} é PRIMO')
else:
    print(f'O número {numero} não é PRIMO')


