print('===== EXERCICIO 009 =====')
print('- Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada -')

n = int(input('Digite um valor inteiro: '))
i = -1

while i < 10:
    i += 1
    m = n * i
    print('{} x {} = {} \n'.format(n, i, m))
