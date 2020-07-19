print("""
039) Faça um programa que leia o ano de nascimento de um jovem e informe, de
acordo com sua idade: 
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
""")
anodenascimento = int(input('Digite seu ano de nascimento: '))
anoatual = 2020
idadeparasealistar = anoatual - anodenascimento
tempoquefalta = (18-idadeparasealistar)*12
tempoquepassou = (idadeparasealistar - 18)*12
if idadeparasealistar < 18:
    print(f'Você ainda irá se alistar, faltam ainda {tempoquefalta} meses')
elif idadeparasealistar > 18:
    print(f'Já passou {tempoquepassou} meses do prazo de alistamento')
elif idadeparasealistar == 18:
    print('É a hora de se alistar')