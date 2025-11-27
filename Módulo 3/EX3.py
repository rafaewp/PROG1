# Faça um programa que leia um número inteiro de 5 dígitos e indique se ele é palíndromo. Um número palíndromo é aquele que se lido da esquerda para a direita ou da direita para a esquerda possui o mesmo valor (ex.: 15451).

X = input('Digite um valor com 5 algarismos --> ')

if len(X) != 5:
    print('Eu disse 5... tente novamente!')
    X = input('Digite um valor com 5 algarismos --> ')
else:
    primeira_metade = X[:2]
    segunda_metade = X[3:][::-1]
    if primeira_metade == segunda_metade:
        print('É PALÍNDROMO')
    else:
        print('NÃO É PALÍNDROMO')