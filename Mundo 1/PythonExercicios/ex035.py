print('Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo')

comp1 = float(input('Digite o comprimento 1: '))
comp2 = float(input('Digite o comprimento 2: '))
comp3 = float(input('Digite o comprimento 3: '))

if comp1 + comp2 > comp3:
    print('Sim, é um triangulo')
else:
    print('Não, não é um triangulo')
