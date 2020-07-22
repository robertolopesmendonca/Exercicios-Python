print("""
055) Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso lidos.
""")
maiorpeso = 0
menorpeso = 0
for contador in range (1, 6):
    peso = float(input(f'Digite o peso da {contador}a pessoa: '))
    if contador == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if  peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso é {maiorpeso}kg')
print(f'O menor peso é {menorpeso}kg')    
    
    




