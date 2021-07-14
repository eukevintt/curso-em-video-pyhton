print('===== EXERCICIO 013 =====')
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.')

sala = float(input('Qual o seu salário? '))
aumento = sala * float(0.15)
vf = sala + aumento

print('Seu salário é de {} e aumentou para {:.2f}'.format(sala, vf))
