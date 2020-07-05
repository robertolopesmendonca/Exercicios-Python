print("""
028) Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário vendeu ou perdeu.
""")

from random import randint

usuario = int(input('Digite um número: '))
print('O número escolhido pelo usuário foi:{}  '.format(usuario))
computador = randint(0, 5)
print('O número escolhido pelo computador foi:{} '.format(computador))
if usuario == computador:
    print('USUÁRIO VENCEU!!')
else:
    print('USUÁRIO PERDEU!!') 



