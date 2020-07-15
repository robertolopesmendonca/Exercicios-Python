print("""
029) Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
quilômetro acima do limite.
""")
velocidadeaferida = float(input('Qual a velocidade aferida (Km/h) ? '))
valordamulta = (velocidadeaferida - 80)* 7
if velocidadeaferida > 80:
    print('Você foi multado, pois ultrapassou a velocidade de 80 Km/h')
    print(f'O valor da multa foi: R${valordamulta:.2f}')
else:
    print('Você não ultrapassou a velocidade limite')