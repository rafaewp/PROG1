# Faça um programa que leia três valores e indique se formam um triângulo, juntamente com o seu tipo (equilátero, isósceles e escaleno).
A, B, C = map(int, input('Digite 3 valores, A, B, C para representar os lados de um Triângulo --> ').split())

while A != 0 and B != 0 and C != 0:

    if A + B > C and A + C > B and C + B > A:
        if A == B and B == C and C == A:
            print('EQUILÁTERO // Para encerrar digite 0 0 0')
        elif A == B or B == C or C == A:
            print('ISÓSCELES // Para encerrar digite 0 0 0')
        else:
            print('ESCALENO // Para encerrar digite 0 0 0')
        
        A, B, C = map(int, input('Digite 3 valores, A, B, C para representar os lados de um Triângulo --> ').split())
    else:
        print('NÃO É POSSÍVEL FORMAR ESSE TRIÂNGULO!')
        print('TENTE DIGITAR NOVOS VALORES!')
        A, B, C = map(int, input('Digite 3 valores, A, B, C para representar os lados de um Triângulo --> ').split())