print("""
042) Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que
tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
""")

print("""
Este programa recebe o valor de três retas e verifica se, com elas,
é possível formar um triângulo. Para isso é importante saber que a
a soma de quaisquer dois lados de um triângulo deve, SEMPRE, ser 
maior que o terceiro lado restante.
""")
L1 = int(input('Digite o primeiro lado: '))
L2 = int(input('Digite o segundo lado: '))
L3 = int(input('Digite o terceiro lado: '))
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Os segmentos formam um triângulo')
    if L1 == L2 == L3:
        print('O triângulo é equilátero ')
    elif L1 == L2 or L1 == L3 or L2 == L3:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Os segmentos não formam um triângulo')







