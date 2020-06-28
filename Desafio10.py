print('[-- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00=R$3,27 --]\n')
dinheiro = float(input('Quanto você tem na carteira? R$ '))
dolar = dinheiro/3.27
print(f'Com R${dinheiro} reais, posso comprar ${dolar:.2f} dólares')
