print("""
061) Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
""")
print('Gerador de PA')
print('-=' * 10)
primeirotermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeirotermo
contador = 1
while contador <=10:
    print(f'{termo}', end=' ')
    termo += razão
    contador += 1
print('FIM')







