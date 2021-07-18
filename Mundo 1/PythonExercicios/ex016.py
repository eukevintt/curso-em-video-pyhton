from math import trunc

print('===== EXERCICIO 016 =====')
print('- Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira -')

num = float(input('Digite um número real: '))
numFormated = trunc(num)

print('O número {} tem a parte inteira {}'.format(num, numFormated))
