print("""
057) Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto
""")
sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados incorretos, favor digite seu sexo corretamente [M/F]: ')).strip().upper()[0]
print(f'O sexo informado foi {sexo}')









