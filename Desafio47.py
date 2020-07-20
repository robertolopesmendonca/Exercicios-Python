print("""
047) Crie um programa que mostre na tela todos os números pares que estão no intervalo
entre 1 e 50.
""")
for contador in range (1, 50):
    if contador % 2 == 0:
        print(contador)

### Outra forma

for contador in range (2, 50, 2):
    print(contador)

