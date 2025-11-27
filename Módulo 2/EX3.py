# Faça um programa que leia dois pontos num espaço bidimensional e calcule a distância entre esses pontos.

X, Y = map(float, input('Digite 1 valor para o ponto X, e outro para o ponto Y :   ').split())

if Y > X:
    distancia = Y - X 
else:
    distancia = X - Y 

print(f'A distância entre os dois pontos é de {distancia:.1f}m')