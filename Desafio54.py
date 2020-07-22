print("""
054) Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
""")
from datetime import date
anoatual = date.today().year
totmaioridade = 0
totmenoridade = 0
for contador in range (1, 8):
    anodenascimento = int(input('Informe seu ano de nascimento: '))
    if (anoatual-anodenascimento) > 21:
        totmaioridade += 1
    else:
        totmenoridade += 1
print(f'{totmaioridade} pessoas já atingiram a maior idade')
print(f'{totmenoridade} pessoas não atingiram a menor idade')




    
