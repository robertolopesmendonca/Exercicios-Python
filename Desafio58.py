print("""
058) Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
""")
palpite = 0
from random import randint
usuario = int(input('Digite um número: '))
print(f'O número escolhido pelo usuário foi:{usuario}')
computador = randint(0, 10)
print(f'O número escolhido pelo computador foi:{computador}')
while usuario != computador:
    palpite += 1
    usuario = int(input('Digite um número: '))
    computador = randint(0, 10)
    print(f'O número escolhido pelo computador foi:{computador}')
print(f'USUÁRIO VENCEU e o número de palpite(s) foi/foram {palpite}!!')








