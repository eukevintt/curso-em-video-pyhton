print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 1.250, calcule um aumento de 10%. para os inferiores ou igual, o aumento é de 15%')

salario = float(input('Qual o seu salário? '))

if salario > 1250:
    print('Seu aumento vai ser de R${}'.format(salario + salario * 0.1))
else:
    print('Seu aumento vai ser de R${}'.format(salario + salario * 0.15))
