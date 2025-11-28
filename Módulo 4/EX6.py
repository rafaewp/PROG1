#Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês a mês, sem usar a fórmula de juros compostos. O usuário deve informar quanto será investido por mês e qual será a taxa de juros mensal. O programa deve informar o saldo do investimento após um ano (soma das aplicações mês a mês considerando os juros compostos), e perguntar ao usuário se ele deseja que seja calculado o ano seguinte, sucessivamente.

saldo = 0.0

while True:
    try:
        X = float(input('Digite a Taxa Mensal --> ')) / 100
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    valor_mensal = float(input('Qual valor será investido por mês? R$ '))
    
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    print(f'--- Calculando Saldo Anual... ---')
    
    for i in meses:
        rendimento = saldo * X
        saldo += rendimento
        saldo += valor_mensal

    print(f'SALDO AO FINAL DESTE ANO = R$ {saldo:.2f}')
    
    confirmacao = input('Deseja processar mais um ano? (S/N) --> ').strip().upper()
    if confirmacao == 'N':
        print(f'SALDO FINAL : R$ {saldo:.2f}')
        print('Até a próxima!')
        break