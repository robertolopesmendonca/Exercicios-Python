print("""
031) Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.
""")
distanciadaviagem = float(input('Digite a distância da viagem (Km): '))
valordapassagemate200km = 0.50*distanciadaviagem
valordapasagemacimade200km = 0.45*distanciadaviagem
if distanciadaviagem > 200:
    print(f'O valor da passagem será de R${valordapasagemacimade200km:.2f}')
else:
    print(f'O valor da passagem será de R${valordapassagemate200km:.2f}')

