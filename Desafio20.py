print('[-- O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. --]\n')
from random import shuffle
primeiroaluno = input('Qual o primeiro aluno? ')
segundoaluno = input('Qual o segundo aluno? ')
terceiroaluno = input('Qual o terceiro aluno? ')
quartoaluno = input('Qual o quarto aluno? ')
alunos = [primeiroaluno, segundoaluno, terceiroaluno, quartoaluno]
shuffle(alunos)
print(f' A ordem de apresentação dos alunos será: {alunos} ')

