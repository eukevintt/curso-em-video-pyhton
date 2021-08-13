print('Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7 reais por cada km acima do limite')

velCarro = float(input('Qual foi a velocidade do carro? '))

if velCarro > 80:
    multa = (velCarro - 80) * 7
    print('Você ultrapassou a velocidade limite, sua multa foi de R${}'.format(multa))
