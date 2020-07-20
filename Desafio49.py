print("""
049) refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
""")
n = int(input('Digite um número: '))
print (f'Tabuada do número {n}')
print('-='*10)
for c in range (1,11):
    print(f'{n} x {c} = {n*c} ')
print('-='*10)




