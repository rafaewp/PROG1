# Faça um programa que gere números inteiros aleatórios entre 1 e 10 e calcule a soma desses números, até que seja gerado um número alvo que foi informado pelo usuário anteriormente.

import random

target = int(input('Digite um valor alvo --> '))
soma = 0
contador = 0 

while soma != target:
    soma += random.randint(1, 10)
    contador += 1
    if soma == target:
        print(f'ALVO ENCONTRADO! Geramos {contador} números até encontrar seu resultado.')
    elif soma > target:
        print(f'ALVO NÃO ENCONTRADO!')
        print(f'Geramos {contador} números aleatórios e não encontramos seu resultado.')
        break