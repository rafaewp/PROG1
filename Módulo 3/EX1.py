# Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado ao quadrado) e informe a sua classificação segundo a tabela obtida na Wikipedia.

massa = float(input('Digite seu peso em KG --> '))
altura = float(input('Digite sua altura em Centímetros --> '))

imc = massa / (altura / 100) ** 2

if imc >= 40.0:
    print(f'IMC = {imc:.1f} // CLASSIFICAÇÃO : OBESIDADE Grau 3 (Mórbida)')
elif 35.0 <= imc <= 39.9:
    print(f'IMC = {imc:.1f} // CLASSIFICAÇÃO : OBESIDADE Grau 2 (Severa)')
elif 30.0 <= imc <= 34.9:
    print(f'IMC = {imc:.1f} // CLASSIFICAÇÃO : OBESIDADE Grau 1')
elif 25.0 <= imc <= 29.9:
    print(f'IMC = {imc:.1f} // CLASSIFICAÇÃO : Peso em Excesso')
elif 18.6 <= imc <= 24.9:
    print(f'IMC = {imc:.1f} // CLASSIFICAÇÃO : Saudável')
else:
    print(f'IMC = {imc:.1f} // CLASSIFICAÇÃO : Abaixo do Peso')