print("""
056) Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do 
programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
""")
somaidade = 0
mediaidade = 0
maioridadedehomem = 0
nomevelho = ''
totmulher20 = 0

for pessoa in range (1, 5):
    print('-----{pessoa}a PESSOA -----')
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input(f'Digite a {pessoa}a idade: '))
    sexo = str(input(f'Digite o sexo [M/F]: ').strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = somaidade/4
print(f'A média de idade do grupo é de {maioridade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'No total temos {totmulher20} mulheres com menos de 20 anos')

