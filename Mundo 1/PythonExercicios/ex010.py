print('===== EXERCICIO 010 =====')
print('- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar -')
print('Dados: \n US$1.00 = R$3,27')

dolar = 3.27
carteira = float(input('Quanto você tem na sua carteira? '))
final = carteira / float(dolar)

print('Atualmente você tem R${} na carteira e isso resulta em US${:.2f}'.format(carteira, final))
