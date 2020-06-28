print('[-- Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado. --]\n')

kmpercorridos = float(input('Qual a quantidade de Km percorridos? '))
qtdededias = int(input('Qual a quantidade de dias de aluguel? '))
preçoapagar = (qtdededias*60) + (0.15*kmpercorridos)
print(f'O valor a ser pago será R${preçoapagar:.2f}')

