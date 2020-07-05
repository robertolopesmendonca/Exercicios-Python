print('[-- Crie um programa que leia o nome completo de uma pessoa e mostre: a) O nome com todas as letras maiúsculas; b) O nome com todas as letras minúsculas; c) Quantas letras ao todo (sem considerar espaços); d) Quantas letras tem o primeiro nome --]\n')
nome = str(input('Digite o nome completo: '))
print(f' O nome com todas as letras maiúsculas é: {nome.upper()}')
print(f' O nome com todas as letras minúsculas é: {nome.lower()}') 
print(' A quantidade de letras ao todo (sem considerar espaço) é: {}'.format(len(nome.replace(' ',''))))
print(len(nome.split()[0]))

