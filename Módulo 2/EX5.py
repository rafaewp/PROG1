# Faça um programa que a partir de um valor informado em centavos, indique a menor quantidade de moedas que representa esse valor.
# Obs: Considere moedas de 1, 5, 10, 25 e 50 centavos, e 1 real.
# Exemplo: para o valor 290 centavos, a menor quantidade de moedas é 2 moedas de 1 real, 1 moeda de 50 centavos, 1 moeda de 25 centavos, 1 moeda de 10 centavos e 1 moeda de 5 centavos.

X = int(input('Digite um valor em centavos --> '))

valores = [100, 50, 25, 10, 5, 1]

for i in valores:
    qtd = X // i 
    print(f'{qtd} moeda(s) de {i} centavo(s)')
    X = X % i 