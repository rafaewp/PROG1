# Faça um programa para montar a tabela de multiplicação de números de 1 a 10 (ex.: 1 x 1 = 1, 1 x 2 = 2, etc.).

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in valores:
    print('-' * 20)
    for j in range(1, 11):
        print(f'{i} X {j} = {i * j}')