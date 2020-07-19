print("""
043) Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
""")
peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))
IMC = peso / (altura**2)
if IMC < 18.5:
    print(f'Seu IMC é {IMC:.2f}, portanto você está abaixo do Peso')
elif 18.5 <= IMC <= 25: 
    print(f'Seu IMC é {IMC:.2f}, portanto seu peso está ideal')
elif 25 < IMC < 30: 
    print(f'Seu IMC é {IMC:.2f}, portanto você está com sobrepeso')
elif 30 <= IMC <= 40:
    print(f'Seu IMC é {IMC:.2f}, portanto você está com Obesidade')
else:
    print(f'Seu IMC é {IMC:.2f}, portanto você com Obesidade Mórbida')

