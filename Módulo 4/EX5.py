# Faça um programa para listar todos os divisores de um número ou dizer que o número é primo caso não existam divisores. 
# Ao final, verifique se o usuário deseja analisar outro número.

while True:
    try:
        N = int(input('Digite um número para começar! --> '))
        divisores = []

        for i in range(1, N+1):
            if (N % i) == 0:
                divisores.append(i)

        if len(divisores) == 2:
            print(f'Seu número É PRIMO! Com os seguintes divisores : {divisores}')
        else:
            print(f'Seu número NÃO É PRIMO! Apresenta os seguintes divisores : {divisores}')
            
        confirmacao = input('Deseja verificar outro número? Digite S ou N --> ').strip().upper()
        if confirmacao == 'N':
            print('Até a próxima!')
            break

    except ValueError:
        N = print('Digite um número válido para começar! --> ')