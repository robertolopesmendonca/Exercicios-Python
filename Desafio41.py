print("""
041) A Confederação Nacional precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo
com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
""")
anodenascimento = int(input('Digite o ano do seu nascimento: '))
anoatual = 2020
idade = anoatual - anodenascimento
print(f'A sua idade é {idade} anos')
if idade <= 9:
    print('A sua categoria é MIRIM')
elif  9 < idade <= 14:
    print('A sua categorai é INFANTIL')
elif 14 < idade <= 19:
    print('A sua categoria é JUNIOR')
elif 19 < idade <=20: 
    print('A sua categoria é: SÊNIOR')
elif idade > 20:
    print('A sua categoria é MASTER')


