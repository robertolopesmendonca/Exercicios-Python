print("""
053) Crie um programa que leia uma frase qualquer e diga se ela é um
políndromo, desconsiderando os espaços.
""")
frase = str(input('Digite uma frase: ')).strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('TEMOS UM PALÍNDROMO')
else:
    print('NÃO TEMOS UM PALÍNDROMO')
