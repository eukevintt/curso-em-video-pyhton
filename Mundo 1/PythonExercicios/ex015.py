print('===== EXERCICIO 015 =====')
print('- Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. \n Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. -')

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

precoF = (60 * dias) + (0.15 * km)

print('O total a pagar é de R${}'.format(precoF))
