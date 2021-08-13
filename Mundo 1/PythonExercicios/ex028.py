import random

print('Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador, o programa deverá escrever na tela se o usuário venceu ou perder')

numShuffle = random.randint(0, 5)
numUser = int(input('Tente adivinhar o número de 0 a 5 que o computador escolheu: '))

if numUser == numShuffle:
    print('Caramba, você conseguiu acertar! O número escolhido pelo computador é {}'.format(numShuffle))
else:
    print('Aff, que pena você não acertou. O número que o computador escolheu foi {} e você escolheu o {}'.format(numShuffle, numUser))
