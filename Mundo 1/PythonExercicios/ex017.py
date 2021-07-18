from math import sqrt

print('===== EXERCICIO 017 =====')
print('Faça um programa que leia o comprimeito do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa')

catOposto = float(input('Qual o valor do cateto oposto? '))
catAdjacente = float(input('Qual o valor do cateto adjacente? '))

hipotenusa = sqrt(catOposto ** 2 + catAdjacente ** 2)

print('O triãngulo retângulo cujo lados são {} e {} tem a hiponetusa valendo {:.2f}'.format(catOposto, catAdjacente, hipotenusa))
