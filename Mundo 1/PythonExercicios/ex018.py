from math import sin, cos, tan, radians

print('===== EXERCICIO 018 =====')
print('- Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo -')

angulo = int(input('Qual o ângulo? '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O angulo de {} tem o SENO de {:.2f}, COSSENO de {:.2f} e TANGENTE de {:.2f}".format(angulo, seno, cosseno, tangente))

