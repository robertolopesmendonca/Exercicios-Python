print("""
036) Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
então o empréstimo será negado.
""")
valordacasa = float(input('Qual o valor da casa? '))
salariodocomprador = float(input('Qual o salário do comprador? '))
qtosanosirapagar = float(input('Em quantos anos irá pagar o empréstimo? '))
valordaprestacao = valordacasa/(qtosanosirapagar*12)
print(f'O valor da prestação será {valordaprestacao}')
if valordaprestacao >  (30/100)*salariodocomprador:
    print('Seu empréstimo não foi autorizado')
else:
    print(f'Seu empréstimo foi aprovado e o da sua mensalidade será {valordaprestacao:.2f}')
    

