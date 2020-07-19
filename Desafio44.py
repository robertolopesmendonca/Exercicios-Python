print("""
044) Elabore um programa que calcule o valor a ser pago por um produto.
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2xno cartão: preço normal
- 3x ou mais no cartão: 20% de juros
""")

print('LOJAS ROBERTO MENDONCA, VENHAM COMPRAR !!!!')
preconormaldoproduto = float(input('Digite o preço do produto: '))
valordoprodutoavista = preconormaldoproduto*90/100
valordoprodutoavistanocartao = preconormaldoproduto*95/100
valoremtresvezesnocartao = preconormaldoproduto*120/100

print(''' FORMAS DE PAGAMENTO:
[ 1 ] PAGAMENTO A VISTA 
[ 2 ] A VISTA NO CARTÃO
[ 3 ] EM ATÉ 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO
''')
opção = int(input('Digite a opção desejada: '))
if opção == 1:
    print(f'O valor a ser pago pelo produto será: {valordoprodutoavista}')
elif opção == 2:
    print(f'O valor a ser pago pelo produto será: {valordoprodutoavistanocartao}')
elif opção == 3:
    print(f'O valor a ser pago pelo produto será: {preconormaldoproduto}')
elif opção == 4:
    print(f'O valor a ser pago pelo produto será: {valoremtresvezesnocartao}')

