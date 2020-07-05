print('[-- Faça um programa que leia uma frase pelo teclado e mostre: a) Quantas vezes aparece a letra "A"; b) Em que posição ela aparece a primeira vez; c) Em que posição ela aparece a última vez. --]\n')

frase = str(input('Digite a frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição {}'.format(frase.find('A')))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')))

