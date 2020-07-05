print('[-- Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. --]\n')

nome = str(input('Digite o nome: ')).strip()
print('O nome tem Silva? {}'.format('silva' in nome.lower()))