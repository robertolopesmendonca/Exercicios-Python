print("""
050) Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o  
""")
somapares = 0
for c in range (0,6):
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        somapares += n
print(f'A soma dos números pares é: {somapares}')




