print('===== Exercicio 027 =====')
print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente')

nome = input('Qual seu nome completo? ').strip().split()

print('Seu primeiro nome é {} e o ultimo é {}'.format(nome[0], nome[-1]))
