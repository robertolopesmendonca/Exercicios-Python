print("""
034) Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
""")
salario = float(input('Digite o seu salário: R$ '))
if salario > 1250:
    novosalario = salario * 110/100
else:
    novosalario = salario * 115/100

print(f'Seu novo salário é: R${novosalario:.2f}')
