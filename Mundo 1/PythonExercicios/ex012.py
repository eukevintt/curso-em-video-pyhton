print('===== EXERCICIO 012 ython, While Loops is used to execu=====')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.')

preco = float(input('Qual o preço? '))
desc = preco * float(0.05)
vf = preco - desc

print('O preço do produto foi {}, o desconto foi de 5%, logo você pagará {:.2f}'.format(preco, vf))
