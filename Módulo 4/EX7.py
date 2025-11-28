# Escreva um programa que verifica números perfeitos. Um número perfeito é aquele que é igual à soma dos seus divisores. Por exemplo, 6 = 1 + 2 + 3.

N = int(input('Digite um valor! --> '))
soma = 0

for divisor in range(1, N):
    if N % divisor == 0:
        soma += divisor

if soma == N:
    print(f'{N} É número perfeito!')
else:
    print(f'{N} NÃO É número perfeito!')