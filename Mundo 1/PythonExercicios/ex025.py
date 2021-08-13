print('===== Exercicio 025 =====')
print('- Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome -')

nome = input('Digite o nome de uma pessoa: ')

nomeFormated = nome.lower()

if nomeFormated.find('silva') == -1:
    print('Seu nome não tem Silva')
else:
    print('Seu nome tem Silva!')
