print("""
027) Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza.
primeiro=Ana
último: Souza.
""")
nome = str(input('Digite o nome completo: ')).strip()
separacaodonome = nome.split()
primeironome = separacaodonome[0]
ultimonome = separacaodonome[len(separacaodonome)-1]
print(primeironome)
print(ultimonome)

