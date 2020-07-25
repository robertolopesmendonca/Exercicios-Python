print("""
059) Criar um programa que leia dois valores e mostre um menu como o 
abaixo:
Seu programa deverá realizar a operação solicitada em cada caso.
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
""")
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''Digite a opção desejada: 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opção = int(input('Digite a opção desejada: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A Soma entre {n1} e {n2} é: {soma} ')
    elif opção == 2:
        multiplicação = n1*n2
        print(f'A Multiplicação entre {n1} e {n2} será {multiplicação}')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}') 
        elif n2 > n1:
            print(f'O maior valor é {n2}')
    elif opção == 4:
        print('Digite os valores novamente')
        n1 = int(input('Digite um novo valor para n1: '))
        n2 = int(input('Digite um novo valor para n2: '))
    else:
        print('Opção inválida, tente novamente')
print('SAIR DO PROGRAMA')        






