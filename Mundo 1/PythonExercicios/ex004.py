print('===== EXERCICIO 004 ====')
print('- Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele. -')

algo = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É algabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())
