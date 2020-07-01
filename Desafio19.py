print('[-- Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. --]\n')
from random import choice
primeiroaluno = input('Digite o nome do Primeiro Aluno: ')
segundoaluno = input('Digite o nome do Segundo Aluno: ')
terceiroaluno = input('Digite o nome do Terceiro Aluno: ')
quartoaluno = input('Digite o nome do Quarto Aluno: ')
alunos = [primeiroaluno, segundoaluno, terceiroaluno, quartoaluno]
alunosorteado = choice(alunos)
print(f'O aluno sorteado foi: {alunosorteado} ')

