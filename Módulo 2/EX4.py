# Faça um programa que informe a distância em quilômetros de um raio para o observador.
# O observador deve informar o tempo (em segundos) transcorrido entre ver o raio e ouvir o trovão.
# Assuma que a velocidade do som seja 340 m/s.

X = int(input('Digite o tempo transcorrido em SEGUNDOS entre ver o raio e ouvir o trovão! --> '))
distancia = (X * 340) / 1000

print(f'A distância em KM entre você e o raio é de {distancia}Km')